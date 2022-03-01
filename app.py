from config import Config
from flask import url_for, request, render_template, flash, Flask
from flask_login import logout_user, login_required, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect
from extension import db, login_manager
from model import User, MovieRating


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from model import User
    @login_manager.user_loader
    def load_user(user_id):  # reload user object from the user ID stored in the session
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    extension(app)
    return app


def extension(app):
    """
    Register 0 or more extensions (mutates the app passed in).
    :param app: Flask application instance
    :return:
    """
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'


app = create_app(Config)
with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])  # define login page path
def login():  # define login page fucntion
    if request.method == 'GET':  # if the request is a GET we return the login page
        return render_template('login.html')
    else:  # if the request is POST the we check if the user exist and with te right password
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user:
            flash('Please sign up before!')
            return redirect(url_for('signup'))
        elif not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))  # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('profile'))


@app.route('/signup', methods=['GET', 'POST'])  # we define the sign up path
def signup():  # define the sign up function
    if request.method == 'GET':  # If the request is GET we return the sign up page and forms
        return render_template('signup.html')
    else:  # if the request is POST, then we check if the email doesn't already exist and then we save data
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        username = request.form.get('username')
        user = User.query.filter_by(
            email=email).first()  # if this returns a user, then the email already exists in database
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('signup'))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, username=username,
                        password=generate_password_hash(password, method='sha256'))  #
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))


@app.route('/logout')  # define logout path
@login_required
def logout():  # define the logout function
    logout_user()
    return redirect(url_for('main.index'))


@app.route('/submit-rating', methods=['POST'])
@login_required
def user_rating_submission():
    if request.method == 'POST':
        movie_id = request.form.get('movieId')
        rating = request.form.get('rating')
        comment = request.form.get('comments')
        movie_rating_obj = MovieRating(movie_id=movie_id, comment=comment, rating=rating, user_id=current_user.id)

        db.session.add(movie_rating_obj)
        db.session.commit()
        return redirect(url_for('movie_rating_list'))


@app.route('/movie-ratings')
@login_required
def movie_rating_list():
    data = db.session.query(MovieRating, User).join(User).all()
    context = {"data": data}
    return render_template('ratings.html', **context)


@app.route('/profile')  # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)


if __name__ == '__main__':
    app.run(template_folder='templates')
