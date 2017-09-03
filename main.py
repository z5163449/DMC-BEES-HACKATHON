from flask import Flask, session, flash, redirect, render_template, request, url_for
from server import app

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("homepage.html")