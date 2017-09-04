from flask import Flask, session, flash, redirect, render_template, request, url_for
from server import app

@app.route("/", methods=["GET", "POST"])
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template("homepage.html")

@app.route('/login', methods = ['POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] == 'admin' and request.form['password'] == 'admin':
			session['logged_in'] = True
			return redirect(url_for("index"))
		else:
			flash('Invalid Login, Please try again.')
			return index()
	return redender_template('login.html')

@app.route('/logout')
def logout():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	session.pop('username', None)
	return redirect(url_for('index'))