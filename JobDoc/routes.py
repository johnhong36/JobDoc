from flask import render_template, flash, redirect, session, url_for
from JobDoc import app, db
from JobDoc.forms import InputForm, ExcelForm, OrgButton, AutoForm
from JobDoc.excel import addJob, sortExcel
from JobDoc.database import Company, Skill


@app.route("/", methods=['GET','POST'])
def home():
	form = InputForm()
	exForm = ExcelForm()
	autoForm = AutoForm()

	orgButton = OrgButton()

	if "org" not in session:
		session["org"] = "date"

	if form.validate_on_submit():
		flash('{} Added!'.format(form.name.data),'success')
        # use this to clear test box
        # form.name.data = ""

		if "excel" in session:
			excel = session["excel"]
			inputData = {}
			inputData["name"] = form.name.data
			inputData["date"] = form.date.data
			inputData["importance"] = form.importance.data
			inputData["languages"] = form.languages.data
			inputData["website"] = form.website.data

			addJob(excel,inputData)

			sortExcel(session["excel"],session["org"])

			companyExample = Company(name = form.name.data)
			db.session.add(companyExample)
			db.session.commit()

		return redirect(url_for('home'))

	if exForm.validate_on_submit():
		session["excel"] = exForm.excelName.data
		flash('{}.xlsx Inputted!'.format(exForm.excelName.data),'success')

		return redirect(url_for('home'))

	if orgButton.validate_on_submit():
		if orgButton.nameButton.data:
			session["org"] = "name"
			sortExcel(session["excel"],session["org"])

		if orgButton.dateButton.data:
			session["org"] = "date"
			sortExcel(session["excel"],session["org"])

		if orgButton.importanceButton.data:
			session["org"] = "importance"
			sortExcel(session["excel"],session["org"])
		
	if autoForm.validate_on_submit():
		print("HI")

	return render_template("index.html",form=form,exForm=exForm,orgButton=orgButton,buttonSession=session["org"],autoForm=autoForm)