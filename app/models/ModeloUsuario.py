from tabnanny import check
from .entities.Usuario import Usuario
from .entities.Tipo_Usuario import TipoUsuario


class ModeloUsuario():

    @classmethod
    def login(self, conexion, usuario):
        try:
            cursor = conexion.cursor()

            sql = f"""SELECT id_usuario,username,contraseña,nombre_usuario,foto_usuario
            FROM usuario where username = '{usuario.username}' and tipo_usuario = 1 """
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                coincide = Usuario.verificar_password(
                    data[2], usuario.contrasenia)
                if coincide:
                    usuario_logueado = Usuario(
                        id_usuario=data[0], username=data[1], contrasenia=None, tipo_usuario=None,
                        nombre_usuario=data[3], foto_usuario=data[4])
                    return usuario_logueado
                else:
                    return None
            return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            conexion.close()
            cursor.close()

    @classmethod
    def obtenerUsuarios(self, conexion):
        try:
            cursor = conexion.cursor()
            sql = f"""SELECT id_usuario,username,nombre_usuario,nombre_tipo_usuario,foto_usuario FROM usuario
            left join tipo_usuario ON usuario.tipo_usuario = tipo_usuario.id_tipo_usuario"""
            cursor.execute(sql)
            registros = cursor.fetchall()
            usuarios = []
            for row in registros:
                user = Usuario(row[0], row[1], None, row[3], row[2], row[4])
                usuarios.append(user)
            return usuarios
        except Exception as ex:
            raise Exception(ex)
        finally:
            conexion.close()
            cursor.close()

    @classmethod
    def obtener_por_id(self, conexion, id):
        try:
            cursor = conexion.cursor()

            sql = f"""SELECT us.id_usuario,us.username,us.nombre_usuario,us.foto_usuario,
            tp.id_tipo_usuario,tp.nombre_tipo_usuario
            FROM usuario us
            LEFT JOIN tipo_usuario tp
            ON us.tipo_usuario = tp.id_tipo_usuario
            where us.id_usuario = {id} and tipo_usuario = 1 """
            cursor.execute(sql)
            data = cursor.fetchone()
            tipo_usuario = TipoUsuario(data[4], data[5])
            usuario_logueado = Usuario(
                data[0], data[1], None, tipo_usuario, data[2], data[3])
            return usuario_logueado
        except Exception as ex:
            raise Exception(ex)
        finally:
            conexion.close()
            cursor.close()
