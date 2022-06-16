from todolist import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_dis = db.Column(db.String(300) , nullable=False)
    posts = db.relationship('Post', backref='author' , lazy=True)

def __rep__(self):

    return f"Post('{self.task_dis}')"
