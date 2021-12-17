from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect
from todo.models import Todo
from todo import db
from todo.forms import TodoForm


bp = Blueprint("main", __name__, url_prefix='/')

#-- ORM 연습
"""
db.session.qeury(Todo).filter(Todo.complete == False).all()
db.session.query(Todo).filter_by(conplete = Fasle).all()
Todo.query.filter(Todo.complete == False).all
"""

#-- 리스트 보기
@bp.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template("todo/todo_list.html", incomplete=incomplete, complete=complete)

#-- 생성
@bp.route("/add", methods=["POST","GET"])
def create():
    form = TodoForm()
    if request.method == "POST" and form.validate_on_submit():
        t = Todo(title=form.title.data, desc=form.desc.data, user_id= g.user.id, complete = False)
        db.session.add(t)
        db.session.commit()
        # Blueprint에서 url_for 사용할 땐 <블루프린트 명.함수명>으로 써야 한다.
        return redirect(url_for('main.index'))
    return render_template('todo/todo_create.html', form=form)

#-- 세부사항 보기
@bp.route("/detail/<int:id>")
def detail(id):
    t = Todo.query.filter_by(id=id).first()
    return render_template("todo/todo_detail.html", t=t)

#-- 수정
@bp.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
    t = Todo.query.filter_by(id=id).first()
    form = TodoForm(obj=t)
    if request.method =="POST":
        if form.validate_on_submit():
            t.title = form.title.data
            t.desc = form.desc.data
            t.complete = not t.complete
            print(form.desc)
            db.session.commit()
            return redirect(url_for('main.index'))
    else:
        return render_template('todo/todo_update.html',form=form, t=t)

#-- 삭제
@bp.route("/delete/<int:id>")
def delete_todo(id):
    t = Todo.query.filter_by(id=id).first()
    db.session.delete(t)
    db.session.commit()
    return redirect(url_for('main.index'))

