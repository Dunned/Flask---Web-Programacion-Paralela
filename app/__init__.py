from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
import psycopg2 as bd


def obtener_bd():
    conexion = bd.connect(user='postgres', password='eduardojr',
                          database='bd_malmo')
    return conexion


app = Flask(__name__)

cstf = CSRFProtect()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    print(request.method)
    print(request.form('usuario'))
    print(request.form('password'))
    '''
    if request.method == 'POST':
        if (request.form['usuario'] == 'eduardo' and
           request.form['password'] == 'eduardo'):
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/ordenes')
def ordenes():
    try:
        conexion = obtener_bd()
        cursor = conexion.cursor()
        sentencia = 'SELECT * FROM orden'
        cursor.execute(sentencia)
        registros = cursor.fetchall()
        print(registros)
        data = {
            "ordenes": registros
        }
        return render_template('ordenes.html', data=data)
    except Exception as ex:
        raise Exception(ex)
    finally:
        conexion.close()
        cursor.close()


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    cstf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
