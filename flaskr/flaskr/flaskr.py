from db import connection,getPruebas,insertUser,validarUser
import os 
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash,g
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
import gc
app= Flask(__name__)
app.config.from_object(__name__)
app.secret_key="ramoslq6785_lolipop990"

app.config.from_envvar('FLASKR_SETTINGS',silent=True)

validar=False
players=[]
titulos=[]
pruebas=[]
p=-1
j=-1

@app.before_request
def before_request():
	g.user=None
	if 'user' in session:
		g.user=session['user']



@app.route('/in/',methods=['POST','GET'])
def show_in():
	if g.user:
		return render_template('in.html')
	return redirect(url_for('show_login'))


@app.route('/in/add',methods=['POST','GET'])
def in_add():
	if g.user:
		gc.collect()
		if request.form['jugador']=='':
			return render_template('in.html',players=players)
		players.append(request.form['jugador'])
		return render_template('in.html',players=players)
	
	return redirect(url_for('show_login'))


@app.route('/in/del',methods=['GET','POST','DELETE'])
def in_del():
	gc.collect()
	if g.user:
		if len(players)>0:
			players.remove(request.form['delete'])
			redirect(request.path)		
			return render_template('in.html',players=players)
		else:
			return render_template('in.html',players=players)
	return redirect(url_for('show_login'))


@app.route('/play/',methods=['GET','POST'])
def show_play():
	global p
	global j
	if len(players)==0:
		flash("tiene que haber al menos un jugador")
		return redirect(url_for('show_in'))
	if g.user:
		getPruebas()
		if p+1>=len(players):
			p=-1
		p=p+1
		j=j+1
		return render_template('partida.html',player=players[p],prueba=pruebas[j],titulo=titulos[j])


@app.route('/',methods=['GET','POST'])
def show_homepage():

	return render_template('homepage.html')

@app.route('/login/',methods=['POST','GET'])
def show_login():
	error=''
	gc.collect()
	try:
		if request.method=="POST":
			session.pop('user',None)
			attempted_username=request.form['username']
			attempted_password=request.form['password']
			validarUser(attempted_username,attempted_password)
			if validar is True:
				session['user']=request.form['username']
				return redirect(url_for('show_in'))
			else:

				return render_template('login.html',error='usuario o contraseña incorrectos')
		return render_template('login.html',error=error)
	except Exception as e:
		flash(e)
		return render_template('login.html',error=error)


@app.route('/register/',methods=["GET","POST"])
def show_register():
	error=''
	try:
		if request.method=="POST":
			reg_user=request.form['reg_user']
			reg_password=request.form['reg_password']
			reg_password2=request.form['reg_password2']
			if reg_password==reg_password2:
				c,conn=connection()
				usuario="'"+reg_user+"'"
				password="'"+reg_password+"'"
				insertUser(usuario,password)
				return redirect(url_for('show_homepage'))
			else:
				return render_template("register.html",error="las contraseñas no coinciden")
		return render_template("register.html",error=error)
	except Exception as e:
		return render_template('register.html',error=error)


