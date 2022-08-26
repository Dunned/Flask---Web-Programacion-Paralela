from .entities.Orden import Orden


class ModeloOrden():

    @classmethod
    def listar_ordenes(self, conexion):
        try:
            cursor = conexion.cursor()
            print('ga0')
            sql = "SELECT * FROM public.orden order by 2 desc"
            cursor.execute(sql)
            registros = cursor.fetchall()
            ordenes = []
            for row in registros:
                orden = Orden(row[0], row[1], row[2], row[3], row[4], row[5])
                ordenes.append(orden)
            return ordenes
        except Exception as ex:
            raise Exception(ex)
        finally:
            conexion.close()
            cursor.close()
