from tabnanny import check
from werkzeug.security import generate_password_hash, check_password_hash
from .entities.Usuario import Usuario


class ModeloUsuario():

    @classmethod
    def login(self, conexion, usuario):
        try:
            cursor = conexion.cursor()

            sql = f"""SELECT id_usuario,nombre_usuario,contraseña 
            FROM usuario where nombre_usuario = '{usuario.nombre_usuario}' """
            cursor.execute(sql)
            data = cursor.fetchone()
            coincide = check_password_hash(data[2], usuario.contrasenia)
            if coincide:
                usuario_logueado = Usuario(data[0], data[1], None, None)
                return usuario_logueado
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            conexion.close()
            cursor.close()
