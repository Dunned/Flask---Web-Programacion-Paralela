from Conexion import Conexion
from logger_base import log


class CursorDelPool:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        log.debug(f'Dsde metodo enter cursor')
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self._conn.rollback()
            log.error(
                f'Se produjo un error , se hizo rollback {exc_type},{exc_val},{exc_type}')
        else:
            self._conn.commit()
            log.debug(f'Se hizo commit')

        self._cursor.close()
        Conexion.liberarConexion(self._conn)
