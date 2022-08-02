#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, User

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list')
def _list():
    page = request.args.get('page', type=int, default=1) #페이지
    question_list=Question.query.order_by(Question.create_date) #엑셀 데이터 최상단을 위로 하기위해서..
    #question_list=Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)

#@bp.route('/detail/<int:question_id>/')
#이하 내용은 아직 적용하지 않는다.

