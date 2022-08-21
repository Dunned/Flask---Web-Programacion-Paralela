from threading import Thread
from flask_mail import Message
from flask import current_app, render_template


def confirmacion_email(app, mail, usuario, producto):
    try:
        message = Message('Confirmacion de Orden', sender=current_app.config['MAIL_USERNAME'],
                          recipients=['eduardojaureguir@gmail.com'])
        message.html = render_template(
            'emails/confirmacion_edicion.html'
        )
        mail.send(message)

    except Exception as e:
        raise Exception(e)


# def envio_email_async(app, mail):
#     with app.app_context():
#         message = Message('Confirmacion Edicion',
#                           sender=current_app.config['MAIL_USERNAME'],
#                           recipients='eduardojaureguir@gmail.com'
#                           )
#         message.html = render_template('emails/confirmacion_edicion.html')
#         # mail.send(message)
#         mail.send(message)
