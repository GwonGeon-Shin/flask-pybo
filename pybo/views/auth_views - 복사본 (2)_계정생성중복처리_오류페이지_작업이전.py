#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#from crypt import methods
from distutils.log import error
import email
from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import Question, User

import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view

@bp.route('/signup/', methods=('GET','POST'))
@login_required
def signup():
    form = UserCreateForm()
    if request.method =='POST' and form.validate_on_submit():
        email = User.query.filter_by(email = form.email.data).first()
        # 기존에는 username=form.username.data 였지만 우리는 email 값으로 비교한다.
        user = User.query.filter_by(username = form.username.data).first()
        if not email:
            email=User(username=form.username.data,
                     password=generate_password_hash(form.password1.data),
                     email=form.email.data)
            db.session.add(email)
            db.session.commit()
            return redirect(url_for('question._list'))
        else:
            if(user):
                flash('이미 존재하는 사용자 입니다.')
            elif(email):
                flash('이미 존재하는 e메일 계정 입니다.')
            else:
                flash('이미 존재하는 사용자, 사용중인 메일 입니다.')
            #flash('이미 존재하는 e메일 계정 입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(email=form.username.data).first()
        # 기존 (username=form.username.data).first() => (email=form.username.data).first() 변경
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error ="비밀번호가 올바르지 않습니다."
        if error is None: # 로그인 id와 비밀번호 맞을때
            session.clear()
            session['user_id'] = user.id # 세션에 키('user_id')와 키값(user.id)저장
            _next = request.args.get('next', '')
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('question._list'))
            #return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)




@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


