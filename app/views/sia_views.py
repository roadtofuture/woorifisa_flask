from flask import Blueprint

sia = Blueprint('sia', __name__, url_prefix='/sia')

@sia.route('/about_me')
def about_me():
    return f'저는 {__name__}입니다'

@sia.route('/hello')
def hello():
    return f'안녕하세요'

@sia.route('/bye')
def bye():
    return f'잘가세요'