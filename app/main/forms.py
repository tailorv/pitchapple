from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('APPLE PITCH TITLE',validators=[Required()])
    post = TextAreaField('Write Your ApplePitch')
    category = SelectField(u'Choose Category', choices=[('Athletics', 'ATHLETICS'), 
                                                ('Technology', 'TECHNOLOGY'),
                                                ('Music', 'MUSIC'),
                                                ('Fashion', 'FASHION'),
                                                ('Inspirational', 'INSPIRATIONAL'),
                                                ('Other', 'OTHER') ])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself")
    submit = SubmitField("Update")