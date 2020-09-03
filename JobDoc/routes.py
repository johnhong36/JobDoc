from flask import render_template, flash, redirect, session, url_for
from JobDoc import app, db
from JobDoc.forms import InputForm, ExcelForm, OrgButton, AutoForm
from JobDoc.excel import addJob, sortExcel
from JobDoc.database import Company, Skill
from JobDoc.webscrape import scrapeIndeed, scrapeZipRecruiter, scrapeLinkedin, scrapeAll
from datetime import date
import os.path


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

			companyList = {company.name for company in Company.query.all()}
			skillList = {skill.name for skill in Skill.query.all()}

			if form.name.data not in companyList:
				companyExample = Company(name = form.name.data)
				db.session.add(companyExample)
				db.session.commit()
			
			for skill in form.languages.data.split(","):
				if skill[0] == " ":
					skill = skill[1:]

				if skill.lower() not in skillList:
					skillExample = Skill(name = skill.lower())
					db.session.add(skillExample)
					db.session.commit()

		return redirect(url_for('home'))

	if exForm.validate_on_submit():
		if os.path.isfile(exForm.excelName.data+".xlsx"):
			session["excel"] = exForm.excelName.data
			flash('{}.xlsx Inputted!'.format(exForm.excelName.data),'success')

		else:
			session["excel"] = None
			flash('{}.xlsx Not Found!'.format(exForm.excelName.data),'danger')

		return redirect(url_for('home'))

	if orgButton.validate_on_submit():
		if orgButton.nameButton.data:
			session["org"] = "name"

		if orgButton.dateButton.data:
			session["org"] = "date"

		if orgButton.importanceButton.data:
			session["org"] = "importance"
		
		if session["excel"]:
			sortExcel(session["excel"],session["org"])
		
	if autoForm.validate_on_submit():
		if "indeed" in autoForm.website.data:
			name, skills = scrapeIndeed(autoForm.website.data)

		elif "ziprecruiter" in autoForm.website.data:
			name, skills = scrapeZipRecruiter(autoForm.website.data)
		
		elif "linkedin" in autoForm.website.data:
			name, skills = scrapeLinkedin(autoForm.website.data)

		else:
			flash('Job Not Added.','danger')
			return redirect(url_for('home'))

		companyList = {company.name for company in Company.query.all()}
		if name not in companyList:
			companyExample = Company(name = name)
			db.session.add(companyExample)
			db.session.commit()
		
		if "excel" in session:
			excel = session["excel"]
			inputData = {}
			inputData["name"] = name
			inputData["date"] = date.today()
			inputData["importance"] = autoForm.importance.data
			inputData["languages"] = skills
			inputData["website"] = autoForm.website.data

			addJob(excel,inputData)

			sortExcel(session["excel"],session["org"])

			flash('{} Added.'.format(name),'success')

		return redirect(url_for('home'))

	return render_template("index.html",form=form,exForm=exForm,orgButton=orgButton,buttonSession=session["org"],autoForm=autoForm)