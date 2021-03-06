from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired,Length,NumberRange
from datetime import date

class InputForm(FlaskForm):
    name = StringField('Company Name',validators=[DataRequired(),Length(min=1,max=40)])
    date =  DateField('Date Applied (mm/dd/yy)',validators=[DataRequired()],format='%m/%d/%y',default=date.today())
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

class AutoForm(FlaskForm):
	website = StringField('Website',validators=[DataRequired()])
	importance = IntegerField('Importance (1-5)',validators=[DataRequired(),NumberRange(min=1,max=5)])
	submit = SubmitField('Enter',validators=None)
