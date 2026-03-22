from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired
#import validators for file type

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

#UploadForm class, Accepts only jpg,jpeg,png files to be uploaded
class UploadForm(FlaskForm):
    upfile = FileField(
        'Upload An Image',
        validators =[FileRequired(), FileAllowed(['jpg', 'jpeg','png'],'Only Images Allowed!')
        ]
    )
    
