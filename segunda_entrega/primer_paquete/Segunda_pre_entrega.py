from primer_paquete.alta_cliente import AdminCliente

class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        
    def agregar_carrito(self, producto, cantidad):
        print(
            f"\nEl cliente: {self[0]}, {self[1]}. \n ha agregado al carrito {cantidad} unidades de {producto}\n"
        )
        
    def actualizar_datos(self, nombre, apellido, email, telefono):
        if self[0] != nombre:
            print(
                f" se ha modificado el nombre {self[0]} por el nombre: {nombre} \n"
            )
        if self[1] != apellido:
            print(
                f" se ha modificado el apellido {self[1]} por el apellido: {apellido} \n"
            )
        
        if self[2] != email:
            print(
                f" el mail {self[2]} se da de baja. \n la nueva direccion de mail es:{email}.\n"
            )
        if self[3] != telefono:
            print(
                f" el telefono: {self[3]} se da de baja. \n el nuevo telefono es:{telefono}.\n"
            )
        return self







