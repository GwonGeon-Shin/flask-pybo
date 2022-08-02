#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm
from pybo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET','POST'))
def signup():
    form = UserCreateForm()
    if request.method =='POST' and form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        # 기존에는 username=form.username.data 였지만 우리는 email 값으로 비교한다.
        user_02 = User.query.filter_by(username = form.username.data).first()
        if not user:
            user=User(username=form.username.data,
                     password=generate_password_hash(form.password1.data),
                     email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            if(user):
                flash('이미 존재하는 e메일 계정 입니다.')
            elif(user_02):
                flash('이미 존재하는 사용자 입니다.')
            else:
                flash('이미 존재하는 사용자, 사용중인 메일 입니다.')
            #flash('이미 존재하는 e메일 계정 입니다.')
    return render_template('auth/signup.html', form=form)

