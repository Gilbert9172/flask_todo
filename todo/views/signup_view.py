from flask import Blueprint, render_template, url_for, flash, session, request, g
from werkzeug.utils import redirect
# from werkzeug.security import generate_password_hash
from todo.models import User
from todo import db
from todo.forms import UserCreationForm, UserLoginForm
from todo import bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=["GET","POST"])
def signup():
    form = UserCreationForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(
                username = form.username.data,
                # password = generate_password_hash(form.password1.data),
                # password = form.password1.data,
                password =  bcrypt.generate_password_hash(form.password1.data),
                email = form.email.data
            )
            print(user.password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash("이미 있는 사용자")
    else:
        form = UserCreationForm()
    return render_template('signup/main_signup.html', form=form)


@bp.route('/login/', methods=["GET","POST"])
def login():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username = form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif user.password != form.password.data:
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('signup/login.html', form=form) 

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
        # print(g.user.id, g.user.password, g.user.email, sep="\n")
        """
        g.user에는 User객체의 정보가 들어간다.
        
        ***************출력값**************
        * 1 / wjdrlfwns / admin@admin.com *
        ***********************************
        """

@bp.route("/logout")
def logout():
    session.clear()
    print("로그아웃 완료")
    return redirect(url_for('auth.login'))
