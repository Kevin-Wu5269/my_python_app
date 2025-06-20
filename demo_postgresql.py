from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "postgresql://admin:123456@127.0.0.1:5432/testdb"

db = SQLAlchemy(app)

class Students(db.Model):

    __tablename__ = "Students"
    sid  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    tel  = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    email= db.Column(db.String(100))

    def __init__(self, name, tel, addr, email):
        self.name = name
        self.tel = tel
        self.addr = addr
        self.email= email

@app.route("/")
def index():
    db.create_all()
    return "資料庫連線成功"

@app.route("/insert")
def insert():
    student = Students("Apple","0911111111","新北市中和區中和路5號","apple@gmail.com")
    db.session.add(student)
    db.session.commit()
    return "新增一筆紀錄成功"

@app.route("/insertAll")
def insertAll():
    student1 = Students("Bill","0922222222","新北市中和區永和路5號","bill@gmail.com")
    student2 = Students("Cathy","0933333333","台北市中山區中山北路一段5號","cathy@gmail.com")
    student = (student1,student2)
    db.session.add_all(student)
    db.session.commit()
    return "新增多筆紀錄成功"

if __name__ == "__main__":
    app.run(debug=True, port=5002)









    



