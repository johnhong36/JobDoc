from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired,Length,NumberRange


class InputForm(FlaskForm):
    name = StringField('Company Name',validators=[DataRequired(),Length(min=1,max=40)])
    date = StringField('Date Applied (m/d/yy)',validators=[DataRequired()])
    importance = IntegerField('Importance (1-5)',validators=[DataRequired(),NumberRange(min=1,max=5)])
    languages = StringField('Languages (Python, Java, etc.)',validators=[DataRequired()])
    website = TextAreaField('Website (optional)',validators=None)
    submit = SubmitField('Submit',validators=None)

class ExcelForm(FlaskForm):
	excelName = StringField('Excel File Name',validators=[DataRequired()])
	excelSubmit = SubmitField('Submit',validators=None)

class OrgButton(FlaskForm):
	nameButton = SubmitField('Name',validators=None)
	dateButton = SubmitField('Date',validators=None)
	importanceButton = SubmitField('Importance',validators=None)
