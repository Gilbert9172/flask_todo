from flask import Blueprint, render_template, url_for, flash, request
from werkzeug.utils import redirect
# from werkzeug.security import generate_password_hash
from todo.models import User
from todo import db
from todo.forms import UserCreationForm

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
                password = form.password1.data,
                email = form.email.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash("이미 있는 사용자")
    else:
        form = UserCreationForm()
    return render_template('signup/main_signup.html', form=form)