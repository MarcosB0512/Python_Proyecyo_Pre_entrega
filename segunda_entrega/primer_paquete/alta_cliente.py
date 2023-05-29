import json

bd_clientes = {}
bd_clientes["Clientes"] = []

class AdminCliente: 
    def __nuevo_cliente__(nombre, apellido, email, telefono):
        nombre = nombre
        apellido = apellido
        email = email
        telefono = telefono

        def guardar_cliente(nombre, apellido, email, telefono):    
            bd_clientes["Clientes"].append({
                'Nombre': nombre,
                'Apellido': apellido,
                'email': email,
                'telefono': telefono            
            })
        guardar_cliente(nombre, apellido, email, telefono)
        
        with open("bd_clientes.json", "w") as file:
            json.dump(bd_clientes, file, indent=4)

    def listado_cliente():
        with open("bd_clientes.json", "r") as file:
            datalectura = json.load(file)
            
            clientes = []
            for user in datalectura["Clientes"]:
                cliente = (
                    user["Nombre"],
                    user["Apellido"],
                    user["email"],
                    user["telefono"]
                )
                clientes.append(cliente)
            return clientes

