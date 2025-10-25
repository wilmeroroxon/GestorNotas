historial= [] #Se guarda el historial de eliminacion de curso y modificacion de nota

lista_cursos=[] #lista principal para los cursos

def nuevo_curso(nombre,nota):
    if nota >=60: # para aprobar la nota debe ser mayor o igual a 60
        aprobado = "Aprobado"
    else:
        aprobado = "Reprobado"
        
    return [nombre,nota, aprobado]

#debe recibir una lista con al menos 1 nota
def mostrar_lista(lista):
    for i,curso in enumerate(lista,1): 
        nombre, nota, aprobado = curso
        print(f"{i} Curso: {nombre}, Nota: {nota}, {aprobado}.")
            
#la lista debe tener al menos 1 nota
#Devolvera el promedio de todas las notas registradas
def promedio_general(lista):  
    suma_notas = 0
    cantidad = 0

    for curso in lista:
        nota = curso[1]
        suma_notas += nota 
        cantidad += 1 
        
    resultado = suma_notas / cantidad 
    promedio = round(resultado, 2)#unicamente se necesecitan dos decimales en el promedio

    return promedio

#La lista debe tener al menos 1 curso
#Retornará cursos aprobados y reprobados
def cursos_aprobados(lista):
    aprobado = 0
    reprobado = 0
    for curso in lista:          
        estado = curso[2]
        if estado == "Aprobado": 
            aprobado +=1
        else:
            reprobado +=1
    
    return aprobado,reprobado 

def buscar_curso(lista, busqueda):
    busqueda= busqueda.lower() #normalizamos el dato a buscar
    encontrados = [] 
    
    for curso in lista:
        nombre, nota, estado = curso 
        if busqueda in nombre.lower():#normalizamos el nombre para comparar con la busqueda
            encontrados.append(curso)

    return encontrados

#Mostrará resultados de una busqueda
def mostrar_busqueda(lista,busqueda):
    if lista:
        print(f"\nCursos encontrados con '{busqueda}':")
        for curso in lista:
            nombre, nota, aprobado = curso 
            print(f"- Nombre: {nombre}, Nota: {nota}, {aprobado}\n")
    else:
            print(f"\nNo se encontraron cursos que coincidan con '{busqueda}'.\n")

#Actulizar nota se agrega al historial
def actualizar_nota(lista,nueva_nota):
    for curso in lista:
        nombre, nota_anterior, aprobado = curso
        curso[1] = nueva_nota
        curso[2] = "Aprobado" if nueva_nota >= 60 else "Reprobado"  #Actualizar tambien el estado
        print("Nota actualizada exitosamente")
        historial.append(f"Se actualizó: {nombre} - Nota anterior: {nota_anterior} -> Nueva nota: {nueva_nota}")
        
def eliminar_curso(lista, busqueda):
    busqueda = busqueda.lower()
    encontrados = [] 
    #Se busca el curso que se desea eliminar
    for curso in lista:
        nombre, nota, estado = curso
        if busqueda in nombre.lower():
            encontrados.append(curso)

    if not encontrados:
        print(f"No se encontraron cursos que coincidan con '{busqueda}'.\n")
        return

    print(f"\nCurso encontrado con '{busqueda}':")
    for curso in encontrados:
        nombre, nota, aprobado = curso
        print(f"- Nombre: {nombre}, Nota: {nota}, Estado: {aprobado}")
        print()

    curso_a_eliminar = encontrados[0]

    confirmacion = input(f"¿Está seguro que desea eliminar el curso '{curso_a_eliminar[0]}'? (sí/no): ").strip().lower()
    if confirmacion in ['sí', 'si', 's']:
        lista.remove(curso_a_eliminar)
        historial.append(f"Se eliminó: {curso_a_eliminar[0]} - {curso_a_eliminar[1]}")
        print(f"Curso '{curso_a_eliminar[0]}' eliminado exitosamente.\n")
    else:
        print("Eliminación cancelada.\n")
#se aplica el ordenamiento por burbuja
def ordenamiento_por_nota(lista):
    n = len(lista)
    comps =swaps = 0
    changed =True
    while changed:
        changed = False
        for i in range (n - 1):
            comps += 1
            if lista[i][1] < lista [i+1][1]:
                lista [i], lista[i+1] = lista[i+1], lista[i]
                swaps += 1
                changed = True

        n -= 1
    return comps, swaps, lista


#Funcion para ordenar lista por nombre con ordenamiento por insercion
def ordenamiento_por_nombre(lista):
    comps = moves = 0

    for i in range(1, len(lista)):
        curso = lista[i]             
        clave = curso[0].lower()    
        j = i - 1

        while j >= 0:
            comps += 1
            if lista[j][0].lower() > clave:     
                lista[j + 1] = lista[j]   
                moves += 1        
                j -= 1
            else:
                break
        lista[j + 1] = curso       
    return comps, moves, lista

def busqueda_por_nombre_binario(lista, busqueda):
    min = 0
    max = len(lista) - 1
    busqueda = busqueda.lower()#se normaliza la busqueda

    while min <= max:
        medio = (min + max) // 2
        nombre_curso = lista[medio][0].lower()#Para hacer las comparaciones normalizamos el nombre del curso

        if busqueda in nombre_curso:
            return lista[medio]
        elif busqueda < nombre_curso:
            max = medio - 1
        else:
            min = medio + 1

    return -1 


def solicitud_de_revision():
    solicitudes = []
    while True:
        n= input("Ingrese curso para revisión (escriba 'fin' para terminar): ").upper()
        if n == "FIN":
            break
        else:
            solicitudes.append(n)
    if len(solicitudes) <= 0:
        print("No hay solicitudes ingresadas.")
    else:
        print("Procesando solicitudes: ")
        for i in solicitudes:
            print(f"Revisando: {i}")

def mostrar_historial():
    if not historial:
        print("No hay historial de cambios registrado.\n")
    else:
        print("Historial de cambios:")
        for cambio in historial:
            print("- " + cambio +"\n")
             
menu = (
    "=======   GESTOR DE NOTAS ACADEMICAS ======\n"
    "1. Registrar nuevo curso.\n"
    "2. Mostrar todos los cursos y notas.\n"
    "3. Calcular promedio general.\n"
    "4. Contar cursos aprobados y reprobados.\n"
    "5. Buscar curso por nombre.\n"
    "6. Actualizar nota de un curso.\n"
    "7. Eliminar un curso.\n"
    "8. Ordenar cursos por nota.\n"
    "9. Ordenar cursos por nombre.\n"
    "10. Buscar curso por nombre.\n"
    "11. Simular cola de solicitudes de revision.\n"
    "12. Mostrar historial de cambios.\n"
    "13. Salir."
)
while True:
    print("\n"+menu)
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.\n")
        continue
    
    if opcion == 13:
        print("Gracias por usar el Gestor de notas. ¡Hasta pronto! \n")
        break
    elif opcion == 1:
        while True:
            print("====Registrando un nuevo curso===")
            nombre = input("Ingrese el nombre del curso: ").strip()
            while not nombre:
                nombre = input("Ingrese un nombre válido: ").strip()

            while True:
                try:
                    nota = int(input("Ingrese la nota del curso (0-100): "))
                    if 0 <= nota <= 100:
                        break
                    else:
                        print("La nota debe estar entre 0 y 100: ")
                except ValueError:
                    print("Error: Ingrese un número válido.")

            curso = nuevo_curso(nombre, nota)
            lista_cursos.append(curso)
            print("Curso registrado exitosamente.\n")
        
        
            repetir = input("¿Desea registrar otro curso? (sí/no): ").strip().lower()
            if repetir not in ['sí', 'si', 's']:
                break
    
    elif opcion == 2:
        if lista_cursos:
            print("====Cursos registrados====")
            mostrar_lista(lista_cursos)
        else:
            print("No hay cursos registrados")
        
    elif opcion == 3:
        if not lista_cursos:
            print("No hay cursos registrados.\n")
        else: 
            print("El promedio general es: ",promedio_general(lista_cursos),"\n")

    elif opcion == 4:
        if not lista_cursos:
            print("No hay cursos registrados.\n")
        else:
            aprobado, reprobado = cursos_aprobados(lista_cursos)
            print("Cursos aprobados: ",aprobado) 
            print("Cursos reprobados: ",reprobado,"\n")    

    elif opcion == 5:
        while True:
            if not lista_cursos:
                print("No hay cursos registrados.\n")
            else:
                print("====Buscar curso====")
                busqueda =input("Ingrese el nombre del curso que desea buscar: ")
                mostrar_busqueda(buscar_curso(lista_cursos, busqueda), busqueda)
            repetir = input("¿Desea buscar otro curso? (si/no): ").strip().lower()

            if repetir not in ['sí', 'si', 's']:
                break
            
    elif opcion == 6:
        while True:  #un ciclo infinito para realizar varias modificaciones si se necesitan
            if not lista_cursos:
                print("No hay cursos registrados. ")
            else:
                print("====Modificar nota====")
                busqueda =input("Ingrese el nombre completo del curso para modificar nota: ")
                encontrado=buscar_curso(lista_cursos, busqueda)
            if encontrado == []:
                print("No se encontraron coincidencias.\n")
            else:
                mostrar_busqueda(encontrado,busqueda) #El usuario pueda ver el curso encontrado en el cual se hara la modificacion
                while True:
                    try:
                        nueva_nota = int(input("Ingrese la nueva nota del curso (0-100): "))
                        if 0 <= nota <= 100:
                            break
                        else:
                            print("La nota debe estar entre 0 y 100: ")
                    except ValueError:
                        print("Error: Ingrese un número válido.")

                actualizar_nota(encontrado,nueva_nota)

            repetir = input("¿Desea modificar nota de otro curso? (si/no): ").strip().lower()
            if repetir not in ['sí', 'si', 's']:
                break
               
    elif opcion == 7:
        while True: #Para que el usuario pueda eliminar varios cursos si lo necesita
            if not lista_cursos:
                print("No hay cursos registrados. ")
            else:
                print("====Eliminar curso====")
                busqueda =input("Ingrese el nombre completo del curso que desea eliminar: ")
                eliminar_curso(lista_cursos,busqueda)

            repetir = input("¿Desea eliminar otro curso? (si/no): ").strip().lower()
            if repetir not in ['sí', 'si', 's']:
                break

    elif opcion == 8:
        if not lista_cursos:
            print("No hay cursos registrados. ")
        else:
            comps, swaps, listaOrdenada = ordenamiento_por_nota(lista_cursos) 
            print("====Cursos ordenados por nota====")
            mostrar_lista(listaOrdenada)

    elif opcion == 9:
        if not lista_cursos:
            print("No hay cursos registrados. ")
        else:
            comps, swaps, listaOrdenada = ordenamiento_por_nombre(lista_cursos) 
            print("====Cursos ordenados por nombre==== ")
            mostrar_lista(listaOrdenada)
        
    elif opcion == 10:
        while True:
            if not lista_cursos:
                print("No hay cursos registrados.")
            else:
                print("====Buscar curso===")
                ordenamiento_por_nombre(lista_cursos) 
                busqueda = input("Ingrese el nombre  del curso que desea buscar: ")
                resultado = busqueda_por_nombre_binario(lista_cursos, busqueda)

                if resultado:
                    nombre, nota, estado = resultado
                    print(f"\nCurso encontrado:\n- Nombre: {nombre}, Nota: {nota}, Estado: {estado}\n")
                else:
                    print(f"\nNo se encontró el curso con nombre '{busqueda}'.\n")
            
            repetir = input("¿Desea buscar otro curso? (si/no): ").strip().lower()
            if repetir not in ['sí', 'si', 's']:
                break

    elif opcion == 11:
        if not lista_cursos:
            print("No hay cursos registrados. ")
        else:
            solicitud_de_revision()

    elif opcion == 12:
        if not lista_cursos:
            print("No hay cambios realizados. ")
        else:
            mostrar_historial()
    
    
