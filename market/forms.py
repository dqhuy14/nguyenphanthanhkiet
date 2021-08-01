from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Tên đăng kí đã được sử dụng! Vui lòng thử một tên người dùng khác ')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Địa chỉ email đã tồn tại! Vui lòng thử một địa chỉ email khác ')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:',  validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Tạo tài khoản')


class LoginForm(FlaskForm):
        username = StringField(label='User Name:', validators=[DataRequired()])
        password = PasswordField(label='Password:', validators=[DataRequired()])
        submit = SubmitField(label='Đăng nhập')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Mua hàng ')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Trả hàng')