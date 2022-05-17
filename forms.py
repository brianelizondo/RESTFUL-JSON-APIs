"""Forms for Cupcakes aplication"""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired

class AddCupcakeForm(FlaskForm):
    """Form for adding Cupcakes"""
    flavor = StringField("Flavor:", validators=[InputRequired(message='Enter the cupcake Flavor')])
    size = StringField("Size:", validators=[InputRequired(message='Enter the cupcake Size')])
    rating = FloatField("Rating:", validators=[InputRequired(message='Enter the cupcake Flavor')])
    image = StringField("Image URL:", validators=[InputRequired(message='Enter the cupcake Image URL')])
