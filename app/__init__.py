from __future__ import print_function
from tkinter.messagebox import NO
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
import psycopg2 as bd
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail


from .consts import *
from .emails import confirmacion_email

# IMPORTANCION DE MODELOS PARA RECUPERAR DATA
from .models.ModeloProducto import ModeloProducto
from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloOrden import ModeloOrden
from .models.entities.Usuario import Usuario


def obtener_conexion():
    conexion = bd.connect(user='postgres', password='eduardojr',
                          database='bd_malmo')
    return conexion


app = Flask(__name__)

cstf = CSRFProtect()

login_manager_app = LoginManager(app)
mail = Mail()


@login_manager_app.user_loader
def load_user(id_usuario):
    return ModeloUsuario.obtener_por_id(obtener_conexion(), id_usuario)


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        ordenes = []
        data = {
            'Titulo': 'Ordenes Realizadas en los ultimos dias',
            'ordenes_hechas': ordenes
        }
        flash(LOGIN_CREDENCIALES_INVALIDAS, 'warning')
        return render_template('index.html', data=data)
    else:
        return redirect(url_for('login'))


@app.route('/password/<password>')
def generar_password(password):
    encriptado = generate_password_hash(password)
    valor = check_password_hash(encriptado, password)
    return f'Encriptado: {encriptado}, coiciende: {valor}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None, None, None)

        usuario_logueado = ModeloUsuario.login(obtener_conexion(), usuario)
        print(usuario_logueado.nombre_usuario, usuario.foto_usuario)
        if usuario_logueado != None:
            login_user(usuario_logueado)
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
        ordenes = ModeloOrden.listar_ordenes(obtener_conexion())
        data = {
            'ordenes': ordenes
        }
        return render_template('pages/ordenes.html', data=data)
    except Exception as e:
        print(e)


@app.route('/productos')
@login_required
def productos():
    try:
        productos = ModeloProducto.listarProductos(obtener_conexion())
        data = {
            'productos': productos
        }
        return render_template('pages/productos.html', data=data)
    except Exception as e:
        print(e)


@app.route('/editar')
@login_required
def editar():
    try:
        data = {
            'Titulo': 'Editar Producto',
            'productos': None
        }
        return render_template('editar.html', data=data)
    except Exception as e:
        print(e)


@app.route('/confirmar_edicion')
@login_required
def confirmar_edicion():
    try:
        confirmacion_email(app, mail, None, None)
        return redirect(url_for('index'))
    except Exception as e:
        flash('SE EDITO PRODUCTO', 'success')
        return redirect(url_for('index'))


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def pagina_no_autorizada(error):
    return redirect(url_for('login'))


def inicializar_app(config):
    app.config.from_object(config)
    cstf.init_app(app)
    mail.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, pagina_no_autorizada)
    return app
