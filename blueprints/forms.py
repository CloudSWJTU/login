import wtforms
from wtforms.validators import Email, Length,EqualTo
from models import UserModel,EmailCaptchaModel
from exts import db
import datetime

class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=0, max=20, message='用户名格式错误')])
    password = wtforms.StringField(validators=[Length(min=3, max=20, message='密码格式错误')])
    email = wtforms.StringField(validators=[Email(message='邮箱格式错误')])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message='验证码格式错误')])

    #邮箱是否已经注册
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message='邮箱已经注册')

    #验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        email_captcha = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not email_captcha:
            raise wtforms.ValidationError(message='邮箱验证码错误')
        # else:
        #     db.session.delete(email_captcha)
        #     db.session.commit()

        #定期删除过期的验证码
    # def delete_email_captcha(self):
    #     now = datetime.datetime.now()
    #     email_captchas = EmailCaptchaModel.query.filter(EmailCaptchaModel.create_time < now - datetime.timedelta(minutes=5)).all()
    #     for email_captcha in email_captchas:
    #         db.session.delete(email_captcha)
    #         db.session.commit()




