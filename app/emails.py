from threading import Thread
from flask_mail import Message
from flask import current_app, render_template


def confirmacion_email(app, mail, usuario=None, producto=None):
    try:
        # message = Message('Confirmacion de Orden', sender=current_app.config['MAIL_USERNAME'],
        #                   recipients=['eduardojaureguir@gmail.com'])
        thread = Thread(target=envio_email_async, args=[app, mail])
        thread.start()
    except Exception as e:
        raise Exception(e)


def envio_email_async(app, mail):
    with app.app_context():
        mensaje = Message('Confirmacion de Orden', sender=current_app.config['MAIL_USERNAME'],
                          recipients=['eduardojaureguir@gmail.com'])
        mensaje.html = render_template(
            'emails/confirmacion_edicion.html'
        )
        mail.send(mensaje)
