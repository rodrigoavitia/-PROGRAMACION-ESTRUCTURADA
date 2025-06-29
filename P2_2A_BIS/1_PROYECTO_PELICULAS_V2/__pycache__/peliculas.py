peliculas=[]

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")


#Diccionario que permite almacenar los siguientes atributos (nombre, categoria, clasificacion, genero e idioma) de peliculas.

pelicula={}

def CrearPeliculas():
    while respuesta := input("\n\t\t\t\t ..:::CREAR PELICULA:::.. \n\n\t ¿Desea crear una pelicula? (Si/No): ").upper().strip():
        if respuesta == "SI":
            borrarPantalla()
            print("\n\t\t\t\t ..:::CREAR PELICULA:::.. \n")
            pelicula.update({"nombre": input("Ingresa el nombre de la pelicula: ").upper().strip()})
            print("toy story")
            pelicula.update({"categoria":input("Ingresa la categoria de la pelicula: ").upper().strip()})
            pelicula.update({"clasificación":input ("Ingresa la clasificación: ").upper().strip()})
            pelicula.update({"genero":input ("Ingresa el genero: ").upper().strip()})   
            pelicula.update({"idioma":input ("Ingresa el idioma: ").upper().strip()})
            print("\n\t\t La operación se realizo con exito...")
        elif respuesta == "NO":
           print("\n\t\t ..:::SALIENDO:::.. \n")
           borrarPantalla()
           break
                
        
        
        
           
def mostrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t ..:::MOSTRAR PELICULAS:::.. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
    else:
        print("\n\t\t No hay peliculas para mostrar en el sistema...")



def borrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t ..:::BORRAR PELICULA:::.. \n")
    if len(pelicula) > 0:
        input("¿Que pelicula desea borrar?")
        pelicula.clear()
        print("\n\t\t La operación se realizo con exito...")
    else:
        print("\n\t\t No hay peliculas para borrar en el sistema...")

def espereTecla():
        input("\n\t Presione una tecla para continuar...")


def agregarCaract():
    borrarPantalla()
    print("\n\t\t\t\t ..:::AGREGAR CARACTERISTICA:::.. \n")
    atributo= input("Ingrese el nombre de la caracteristica a agregar: ").lower().strip()
    valor_atributo = input(f"Ingrese el valor de la caracteristica '{atributo}': ").upper().strip()
    pelicula.update({atributo: valor_atributo})
    print(f"\n\t Caracteristica '{atributo}' con valor '{valor_atributo}' agregada exitosamente.")

def modificarCaract():
    borrarPantalla()
    print("\n\t\t\t\t ..:::MODIFICAR CARACTERISTICA:::.. \n")
    if len(pelicula)>0:
        print("El nombre de la pelicula es:", pelicula.get("nombre"))
        respuesta = input("Deseas modificar el nombre de la pelicula? (Si/No): ").upper().strip()
        if respuesta == "SI":
            nombre_pelicula = input("Ingrese el nuevo nombre de la pelicula: ").upper().strip()
            pelicula.update({"nombre": nombre_pelicula})
            print("El nombre de la pelicula ha sido modificado.")
            
        print("La categoria de la pelicula es:", pelicula.get("categoria"))
        categoria_pelicula = input("¿Desea modificar la categoria de la pelicula? (Si/No): ").upper().strip()
        if categoria_pelicula == "SI":
            nueva_categoria = input("Ingrese la nueva categoria de la pelicula: ").upper().strip()
            pelicula.update({"categoria": nueva_categoria})
            print("La categoria de la pelicula ha sido modificada.")
        
        print("La clasificación de la pelicula es:", pelicula.get("Clasificación"))
        clasificacion_pelicula = input("¿Desea modificar la clasificación de la pelicula? (Si/No): ").upper().strip()
        if clasificacion_pelicula == "SI":
                nueva_clasificacion = input("Ingrese la nueva clasificación de la pelicula: ").upper().strip()
                pelicula.update({"Clasificación": nueva_clasificacion})
                print("La clasificación de la pelicula ha sido modificada.")

            
        print("El genero de la pelicula es:", pelicula.get("Genero"))
        genero_pelicula = input("¿Desea modificar el genero de la pelicula? (Si/No): ").upper().strip()
        if genero_pelicula == "SI":
            nuevo_genero = input("Ingrese el nuevo genero de la pelicula: ").upper().strip()
            pelicula.update({"Genero": nuevo_genero})
            print("El genero de la pelicula ha sido modificado.")

                
        print("El idioma de la pelicula es:", pelicula.get("Idioma"))
        idioma_pelicula = input("¿Desea modificar el idioma de la pelicula? (Si/No): ").upper().strip()
        if idioma_pelicula == "SI":
            nuevo_idioma = input("Ingrese el nuevo idioma de la pelicula: ").upper().strip()
            pelicula.update({"Idioma": nuevo_idioma})
            print("El idioma de la pelicula ha sido modificado.")
                        
        print("\n\t\t La operación se realizo con exito...")
        print("\n\t Las nuevas caracteristicas de la pelicula son:",
                "\n\t", pelicula.get("nombre"),
                "\n\t", pelicula.get("categoria"),
                "\n\t", pelicula.get("Clasificación"),      #SE USA LA FUNCION .GET PARA OBTENER EL DATO ACTUALIZADO QUE TIENE LA PELICULA
                "\n\t", pelicula.get("Genero"),             # DE ESA MANERA PODEMOS PONER COMO QUEDO YA ACTUALIZADO
                "\n\t", pelicula.get("Idioma"),
            )
    else:
        print("\n\t\t No hay peliculas para modificar en el sistema...")


        
def borrarCaract():
    borrarPantalla()
    print("\n\t\t\t\t ..:::BORRAR CARACTERISTICA:::.. \n")
    if len(pelicula) > 0:
        print("Las caracteristicas actuales de la pelicula son:",
                "\n\t nombre ", pelicula.get("nombre"),
                "\n\t categoria", pelicula.get("categoria"),
                "\n\t clasificación", pelicula.get("Clasificación"),
                "\n\t genero",pelicula.get("Genero"),
                "\n\t idioma", pelicula.get("Idioma"),
            )
        atributo = input("Ingrese el nombre de la caracteristica a borrar: ").lower().strip()
        if atributo in pelicula:
            del pelicula[atributo]
            print(f"\n\t Caracteristica '{atributo}' borrada exitosamente.")
        else:
            print(f"\n\t La caracteristica '{atributo}' no existe en la pelicula.")
    else:
        print("\n\t\t No hay peliculas para borrar caracteristicas en el sistema...")






