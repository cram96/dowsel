from db import connection
import os 
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash 
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
import gc
app= Flask(__name__)
app.config.from_object(__name__)
app.secret_key="ramoslq6785_lolipop990"

app.config.from_envvar('FLASKR_SETTINGS',silent=True)

@app.route('/in/')
def show_in():
	return render_template('in.html')


@app.route('/')
def show_homepage():
	return render_template('homepage.html')




@app.route('/login/',methods=['GET','POST'])
def show_login():
	error=''
	try:
		if request.method=="POST":
			attempted_username=request.form['username']
			attempted_password=request.form['password']
			c,conn=connection()
			usuario=str(attempted_username)
			contrasena=str(attempted_password)
			query="Select * from users where name="+usuario+" and password="+contrasena
			c.execute(query)
			if (len(c))>0:
				return redirect(url_for('show_in'))
			else:
				error="Usuario o contraseña incorrectos"


		return render_template('login.html',error=error)
	except Exception as e:
		flash(e)
		return render_template('login.html',error=error)

class RegistrationForm(Form):
	username= TextField('Username',[validators.Length(min=4,max=20)])
	password= PasswordField('Password',[validators.Required(),validators.EqualTo('confirm',message="Password must match")])
	confirm=PasswordField('Repeat Password')
	accept_tos= BooleanField('I accept the <a href="/tos/">Terms of Service</a> and the <a href="/privacy/">Privacy Notice</a>',[validators.Required()])


@app.route('/register/',methods=["GET","POST"])
def show_register():
	try:
		form= RegistrationForm(request.form)
		if request.method == "POST" and form.validate():
			username= form.username.data
			password= sha256_crypt.encrypt(str(form.password.data))
			c, conn= connection()
			c.execute("SELECT count(*) from users WHERE name like %s ",(username,))
			x=c.fetchall()
			if x:
				flash("That username is already taken, please choose another")
				return render_template('register.html',form=form)


			else:
				flash("HIII")
				c.execute("INSERT INTO users(username,password) values (&s,&s)",(username),(password))
				
				conn.commit()
				flash("Thanks for registering")
				c.close()
				conn.close()
				gc.collect()
				session['logged_in']=True
				session['username']=username
				return render_template("/in.html/")
		return render_template("register.html",form=form)
	except Exception as e:
		return (str(e))


