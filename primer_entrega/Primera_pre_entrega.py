import json

bd_usuarios = {}
bd_usuarios["Usuarios"] = []

menu_opciones = [
    "1: Crear Usuarios",
    "2: Alta Clientes",
    "3: Ver lista de usuarios:",
    "4: Login:",
    "5: Exit:"
]

def menu_option():
    for valor in menu_opciones:
        print(valor)

def __ingreso_datos__():
    print("\nALTA DE USUARIOS")
    nombre = input("Ingrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ")
    email = input("Ingrese su EMail: ")
    telefono = input("Ingrese su telefeno: ")
    alta_usuario = input("Ingrese un nuevo Usuario: ")
    alta_clave = int(input("Ingrese una nueva Clave: "))

    def guardar_usuarios(nombre, apellido, email, telefono, alta_usuario, alta_clave):    
        bd_usuarios["Usuarios"].append({
            'Nombre': nombre,
            'Apellido': apellido,
            'email': email,
            'telefono': telefono,
            'usuario': alta_usuario,
            'password': alta_clave
        })
    guardar_usuarios(nombre, apellido, email, telefono, alta_usuario, alta_clave)        
     

    with open("bd_usuarios.json", "w") as file:
        json.dump(bd_usuarios, file, indent=4)

def listado_usuarios():
    print("\nLISTADO DE USUARIOS CREADOS: ")
    with open("bd_usuarios.json", "r") as file:
        datalectura = json.load(file)

        for user in datalectura["Usuarios"]:
            print('Usuario: ', user["usuario"])
            print('Password: ', user["password"])

def login(input_user):
    with open("bd_usuarios.json", "r") as file:
        datalectura = json.load(file)
            
    for user in datalectura["Usuarios"]:
        if input_user == user["usuario"]:
            input_pass = int(input("Ingrese su Password: "))
            if input_pass == user["password"]:
               print(f'\n" INGRESASTE CON LAS CREDENCIALES CORRECTAS !! "\n')
               return
            else:
                print(f"\n LA CLAVE INGRESADA ES INCORRECTA !! \n")
                menu()
                return 

    print(f"\n EL USUARIO '{input_user}' ES INCORRECTO !! \n")
    menu()
    return 


print("Bienvenido !!!! estas son tus opciones...\n")
def menu ():
    try:
        for opcion in menu_opciones:
            print(opcion)
        opcion = int(input("Ingrese una opción: "))
    
    except: ValueError( 
            print("\nEL VALOR A INGRESAR DEBE SER UN 'NUMERO ENTERO' ENTRE 1 y 4 \n INTENTALO NUEVAMENTE...\n"),
            menu()
        )
   
    else:
        if opcion == 1: 
            __ingreso_datos__()
            print('\n" EL USUARIO SE CREO EXITOSAMENTE "\n')
            menu()

        elif opcion == 2: 
            listado_usuarios()
            print()
            menu()
        
        elif opcion == 3: 
            try:
                listado_usuarios()
                print()
                menu()

            except json.decoder.JSONDecodeError:(
                print("\nLA LISTA ESTA VACIA...\n"),
                menu()
            )
                  
        elif opcion == 4:
            print("\nINGRESO AL SISTEMA")
            input_user = input("Ingrese su Usuario: ")
            login(input_user)
            
        elif opcion == 5:
            print('\n" HASTA PRONTO !! \n')
            exit()

        elif opcion < 1 or opcion > 5:
            print("\nEL VALOR A INGRESAR DEBE SER ENTRE 1 y 5 \n INTENTALO NUEVAMENTE...\n"),
            menu()
    return opcion
menu()
