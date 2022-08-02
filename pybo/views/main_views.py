#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return '상상특허 블루프린트 적용 예제 main_views.py'

@bp.route('/')
def index():
    #return "상상특허 로그인 페이지 적용 예정"
    #return redirect(url_for('question._list'))
    return redirect(url_for('auth.login'))

