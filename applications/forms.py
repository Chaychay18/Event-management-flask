from flask_wtf  import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Length,DataRequired,Email,EqualTo


class RegistrationForm(FlaskForm):

   
    first_name=StringField(label='' ,validators=[Length(min=4,max=25),DataRequired()])
    last_name=StringField(label='' ,validators=[Length(min=1,max=25)])
    mobile_number=StringField(label='',validators=[Length(min=10,max=10),DataRequired()])
    email_address=StringField(label='' ,validators=[Email(),DataRequired()])
    address=StringField(label='',validators=[Length(min=10,max=50),DataRequired()])
    city = StringField(label='',validators=[Length(min=2,max=20),DataRequired()])
    password1=PasswordField(label='' ,validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='' ,validators=[EqualTo('password1'),DataRequired()])


    submit=SubmitField(label='create account')

class LoginForm(FlaskForm):
        email_address=StringField(label='' ,validators=[Email(),DataRequired()])
        password=PasswordField(label='' ,validators=[Length(min=6),DataRequired()])

        submit=SubmitField(label='SIGN UP')

      


