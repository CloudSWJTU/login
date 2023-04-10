import string
from flask import Blueprint,render_template,jsonify,redirect,url_for,session
from exts import mail,db
from flask_mail import Message
from flask import request
import random
from models import EmailCaptchaModel
from blueprints.forms import RegisterForm
from models import UserModel
from werkzeug.security import generate_password_hash,check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return '注册成功!'


@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            # return redirect(url_for('auth.register'))
            return '注册失败!'

@bp.route('/get_email_captcha')
def get_email_captcha():
    email = request.args.get('email')
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha =''.join(captcha)
    if not email:
        return '邮箱不能为空!'
    message = Message(subject='云上交大注册验证码', recipients=[email], body=f'您的验证码是：{captcha}')
    mail.send(message)
    #用数据库保存验证码
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({'code':200, 'message':'', 'data':None})

@bp.route('/mail/test')
def mail_test():
    message = Message(subject='测试邮件', recipients=['2021110398@my.swjtu.edu.cn'], body='这是一封测试邮件')
    mail.send(message)
    return '邮件发送成功!'