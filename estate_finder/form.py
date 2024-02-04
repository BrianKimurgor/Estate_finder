from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
        propertyImage = StringField('Property Image URL', validators=[DataRequired()])
        propertyStatus = SelectField('Property Status', choices=[('For Rent', 'For Rent'), ('For Sale', 'For Sale')], validators=[DataRequired()])
        propertyType = StringField('Property Type', validators=[DataRequired()])
        propertyPrice = StringField('Property Price', validators=[DataRequired()])
        propertyName = StringField('Property Name', validators=[DataRequired()])
        propertyLocation = StringField('Property Location', validators=[DataRequired()])
        propertySize = IntegerField('Property Size (Sqft)', validators=[DataRequired()])
        propertyBedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
        propertyBathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
