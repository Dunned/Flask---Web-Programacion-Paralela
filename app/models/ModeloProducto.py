from .entities.Producto import Producto
from .entities.Marca import Marca


class ModeloProducto():

    @classmethod
    def listar_ordenes(self, conexion):
        try:
            cursor = conexion.cursor()
            sql = "select p.sku,p.nombre_producto,p.descripcion_producto ,p.costo_producto ,p.precio_producto ,m.id_marca ,m.nombre_marca ,m.descripcion_marca  from producto as p left join marcas as m  ON p.id_marca =m.id_marca"
            cursor.execute(sql)
            registros = cursor.fetchall()
            print(registros)
            productos = []
            for row in registros:
                marca = Marca(row[5], row[6], row[7])
                producto = Producto(
                    row[0], row[1], row[2], row[3], row[4], marca)
                marca = Marca(row[5])
                productos.append(producto)
            
            return productos

        except Exception as ex:
            raise Exception(ex)
        finally:
            conexion.close()
            cursor.close()
