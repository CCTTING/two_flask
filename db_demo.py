from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config():
    """配置参数"""
    # sqlalchemy的配置参数
    SQLAlCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/one_flask"
    #  设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Role(db.Model):
    """用户角色表"""
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")


# 创建数据库模型类
class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库表名

    id = db.Column(db.INTEGER, primary_key=True)  # 整型的主键会默认设置为自增
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_role.id"))


if __name__ == '__main__':
    # 清除数据库里的所有数据
    db.drop_all()

    # 创建所有的表
    db.create_all()
