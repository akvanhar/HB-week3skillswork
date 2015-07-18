from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/application-form')
def application_form():
	return render_template('application-form.html')

@app.route('/application', methods=['POST'])
def take_application():
	first_name = request.form.get('firstname')
	last_name = request.form.get('lastname')
	salary = request.form.get('salary')
	job_choice = request.form.get('jobtype')

	return render_template('app-acknowledge.html', 
							firstname = first_name, 
							lastname=last_name, 
							salary=salary,
							jobchoice=job_choice)

if __name__ == "__main__":
	app.run(debug=True)