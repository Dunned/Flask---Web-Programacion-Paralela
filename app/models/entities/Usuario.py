from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin):
    def __init__(self, id_usuario, username, contrasenia, tipo_usuario, nombre_usuario, foto_usuario):
        self.id_usuario = id_usuario
        self.username = username
        self.contrasenia = contrasenia
        self.tipo_usuario = tipo_usuario
        self.nombre_usuario = nombre_usuario
        self.foto_usuario = foto_usuario

    @classmethod
    def verificar_password(self, encriptado, password):
        coincide = check_password_hash(encriptado, password)
        return coincide

    def get_id(self):
        return (self.id_usuario)
