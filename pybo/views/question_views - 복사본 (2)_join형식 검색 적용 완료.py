#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
from re import search

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, User

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list')
def _list():
    page = request.args.get('page', type=int, default=1) #페이지
    kw = request.args.get('kw', type=str, default='')
    question_list=Question.query.order_by(Question.create_date) #엑셀 데이터 최상단을 위로 하기위해서 .decs()제거
    #question_list=Question.query.order_by(Question.create_date.desc())
    # 이하 검색을 위한 기능 구현
    # 기존 예제는 outerjoin 이였지만 우리는 Quesiton 모델 하나만 쓰기에
    # join 형식으로 검색 구현을 해본다.
    if kw:
        search = '%%{}%%' .format(kw)
        question_list = question_list \
            .filter(Question.p_name.ilike(search) | # 질문 제목 subject => 국문 명칭자료 p_name
                    Question.req_name.ilike(search) | # 의뢰인 자료 기준 검색 req_name
                    Question.our_ref.ilike(search) # 관리번호 기준 검색 our_ref
                    )
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list, page=page, kw=kw)

#@bp.route('/detail/<int:question_id>/')
#이하 내용은 아직 적용하지 않는다.

#.outerjoin(sub_query, sub_query.c.question_id == Question.id) \
#.outerjoin(sub_query, sub_query.c.question_id == Question.id) \

