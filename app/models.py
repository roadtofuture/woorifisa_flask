from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True) #자동 auto-increment 생성
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True) #자동 auto-increment 생성
    #Foreign Key 로 걸려있는 테이블에서 삭제가 발생했을 때 
        # 1) Answer도 같이 지운다
        # 2) Answer는 남겨놓는다
            # Question의 id를 남겨놓는다
            # Question의 id를 삭제한다
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)