from flask import Flask, render_template, flash, redirect, session, url_for
from forms import InputForm, ExcelForm
from excel import addJob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_stuff'

@app.route("/", methods=['GET','POST'])
def home():
	form = InputForm()
	exForm = ExcelForm()

	if form.validate_on_submit():
		print("WOW")
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

		return redirect(url_for('home'))

	if exForm.validate_on_submit():
		session["excel"] = exForm.excelName.data
		flash('{}.xlsx Inputted!'.format(exForm.excelName.data),'success')
		return redirect(url_for('home'))

	return render_template("index.html",form=form,exForm=exForm)


if __name__ == '__main__':
    app.run(debug=True)
