from tabnanny import check
from werkzeug.security import generate_password_hash, check_password_hash
from .entities.Usuario import Usuario
from .entities.Tipo_Usuario import TipoUsuario


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
            #raise Exception(ex)
            return None
        finally:
            conexion.close()
            cursor.close()

    @classmethod
    def obtener_por_id(self, conexion, id):
        try:
            cursor = conexion.cursor()

            sql = f"""SELECT us.id_usuario,us.nombre_usuario,tp.id_tipo_usuario,tp.nombre_tipo_usuario
            FROM usuario us
            LEFT JOIN tipo_usuario tp
            ON us.tipo_usuario = tp.id_tipo_usuario
            where us.id_usuario = {id} """
            cursor.execute(sql)
            data = cursor.fetchone()
            print('gaaa2')
            tipo_usuario = TipoUsuario(data[2], data[3])
            usuario_logueado = Usuario(data[0], data[1], None, tipo_usuario)
            print('gaaa2')
            return usuario_logueado
        except Exception as ex:
            raise Exception(ex)
        finally:
            conexion.close()
            cursor.close()
