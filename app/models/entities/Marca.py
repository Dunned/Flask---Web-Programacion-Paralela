from tkinter.messagebox import NO


class Marca:
    def __init__(self, id_marca, nombre_marca=None, descripcion_marca=None):
        self.id_marca = id_marca
        self.nombre_marca = nombre_marca
        self.descripcion_marca = descripcion_marca
