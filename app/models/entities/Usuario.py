from werkzeug.security import generate_password_hash, check_password_hash


class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasenia, tipo_usuario):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.tipo_usuario = tipo_usuario

    def encriptar_password(password):
        encriptado = generate_password_hash(password)
        coincide = check_password_hash(encriptado, password)
        return coincide
