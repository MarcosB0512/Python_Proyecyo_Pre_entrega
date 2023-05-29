from primer_paquete.alta_cliente import AdminCliente
from primer_paquete.Segunda_pre_entrega import Cliente

# Creo el cliente
AdminCliente.__nuevo_cliente__("Marcos", "Benavide", "mbena@mail.com", "1234-5678")
print()
cliente = AdminCliente.listado_cliente()[0]

# Muestro el cliente
print(f"\nel cliente creado es:\n{cliente}\n")

# Modificar Cliente
cliente_moificado = Cliente.actualizar_datos(cliente, "Marcos", "Benavide", "marcosbenavide72@gmail.com", "999-9999")

# Agrego al carrito del cliente 
compra = Cliente.agregar_carrito(cliente,"Zapatillas", 2)

