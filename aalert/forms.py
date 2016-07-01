from flask_wtf import Form 
from wtforms import BooleanField, StringField, PasswordField, DateField, IntegerField, TextAreaField, TextField
from wtforms.validators import DataRequired, Length

#signin
class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

#adding entries
class AddEntry(Form):
    firstname = StringField('First Name', validators = [DataRequired()])
    lastname = StringField('Last Name', validators = [Length(min=0, max=50),
                                        DataRequired()])
    age = IntegerField('Age', validators = [DataRequired()])
    height = IntegerField('Height', validators = [DataRequired()])
    last_loc = TextAreaField('Last Known Location', validators = [DataRequired()])
    missing_since = DateField('Missing Since', validators = [DataRequired()])
    contact_info = TextField('Number')
    home_address = TextAreaField('Home Address', validators = [DataRequired()])
    

#entry query (search bar type)
class SearchForm(Form):
    query = StringField('Search Query', validators = [DataRequired()])


#register
class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
