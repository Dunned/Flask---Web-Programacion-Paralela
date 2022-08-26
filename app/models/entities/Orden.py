class Orden:
    def __init__(self, id_orden, fecha_orden, tipo_delivery, id_usuario, ticket_full_price, descuento_aplicado):
        self.id_orden = id_orden
        self.fecha_orden = fecha_orden
        self.tipo_delivery = tipo_delivery
        self.id_usuario = id_usuario
        self.ticket_full_price = ticket_full_price
        self.descuento_aplicado = descuento_aplicado
