from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
import psycopg2 as bd
from flask_login import LoginManager, login_user, logout_user, login_required

from .consts import *

from .models.ModeloProducto import ModeloProducto
from .models.ModeloUsuario import ModeloUsuario

from .models.entities.Usuario import Usuario


def obtener_conexion():
    conexion = bd.connect(user='postgres', password='eduardojr',
                          database='bd_malmo')
    return conexion


app = Flask(__name__)

cstf = CSRFProtect()

login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id_usuario):
    return ModeloUsuario.obtener_por_id(obtener_conexion(), id_usuario)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/password/<password>')
def generar_password(password):
    encriptado = generate_password_hash(password)
    valor = check_password_hash(encriptado, password)
    return f'Encriptado: {encriptado}, coiciende: {valor}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None)

        usuario_logueado = ModeloUsuario.login(obtener_conexion(), usuario)
        if usuario_logueado != None:
            login_user(usuario_logueado)
            flash(MENSAJE_BIENVENIDA, 'success')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_CREDENCIALES_INVALIDAS, 'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@app.route('/ordenes')
@login_required
def ordenes():
    try:
        productos = ModeloProducto.listar_ordenes(obtener_conexion())
        data = {
            'productos': productos
        }
        print(productos)
        return render_template('ordenes.html', data=data)
    except Exception as e:
        print(e)


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def pagina_no_autorizada(error):
    return redirect(url_for('login'))


def inicializar_app(config):
    app.config.from_object(config)
    cstf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, pagina_no_autorizada)
    return app
