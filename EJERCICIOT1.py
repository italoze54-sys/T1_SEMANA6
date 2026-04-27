class Puesto_de_Trabajo():
    def __init__(self, codigo="", descripcion ="",area_solicitante="",plazas_requeridas=0,sueldo=float):
        self.codigo = codigo
        self.descripcion = descripcion
        self.area_solicitante = area_solicitante
        self.plazas_requeridas = plazas_requeridas
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} - {self.area_solicitante} - {self.plazas_requeridas} - S/({self.sueldo})"
    
    def __repr__(self):
        return f"{self.codigo} - {self.descripcion} - {self.area_solicitante} - {self.plazas_requeridas} - S/({self.sueldo})"


#•	1 – AgregaPuesto(): Registrar un nuevo Puesto de trabajo, para lo cual buscará linealmente tal que debe validar que no haya otro Puesto de trabajo con el mismo código, descripcion o areaSolicitante e insertará el nuevo Puesto de trabajo. Valide que los datos string tengan por lo menos 3 letras y los datos numéricos sean mayor a cero.
def AgregarPuesto(lista, puesto):
    if len(puesto.codigo) < 3 or len(puesto.descripcion) < 3 or len(puesto.area_solicitante) < 3:
        print("Los campos de texto deben tener al menos 3 caracteres.")
        return False
    if puesto.plazas_requeridas <= 0 or puesto.sueldo <= 0:
        print("Los campos numéricos deben ser mayores a cero.")
        return False
    
    for p in lista:
        if p.codigo == puesto.codigo or p.descripcion == puesto.descripcion or p.area_solicitante == puesto.area_solicitante:
            print("Ya existe un puesto con el mismo código, descripción o área solicitante.")
            return False
    
    lista.append(puesto)
    return True


def MostrarPuestos(lista):
    for p in lista:
        print(p)
        
        

#•	3 – BorraPuesto(): Pedirá un codigo, luego ordenará por método de burbuja usando el código de más a menos y mediante búsqueda lineal buscará el Puesto de trabajo cuyos codigos coincidan y los eliminará de la lista.
def OrdenarBurbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j].codigo < lista[j+1].codigo:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(lista)


#•	4 – BuscaSueldo(): Ordenará la lista por sueldo usando método de inserción de más a menos. Luego preguntará un sueldo a buscar, y usando la búsqueda binaria encontrará todos los Puesto de trabajo con ese sueldo.
def OrdenarInsercion(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i-1
        while j >= 0 and key.sueldo > lista[j].sueldo:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    print(lista)

#•	5 – PuestosAContratar(): Preguntará cuánto dinero en total se invertirá en salarios de puestos nuevos y mostrará la lista de puestos que podrían contratarse hasta cubrir el monto. Nótese que cada puesto tiene asociada una cantidad plazasRequeridas y, multiplicado por el sueldo de cada plaza, se obtiene el total requerido en dinero para ese puesto de trabajo. Ordene la lista de Puesto de trabajo con el método de selección según de más a menos según el total requerido en dinero y muestre los puestos que se cubrirán hasta cubrir el monto que se invertirá en salarios.
def OrdenarSeleccionTotal(lista):
    n = len(lista)
    for manoizq in range(n-1):
        posmay = manoizq
        for ver in range(manoizq+1,n):
            total_ver = lista[ver].plazas_requeridas * lista[ver].sueldo
            total_posmay = lista[posmay].plazas_requeridas * lista[posmay].sueldo
            if total_ver > total_posmay:
                posmay = ver
        lista[manoizq], lista[posmay] = lista[posmay], lista[manoizq]
    
    print(lista)
    
lista = []
print("================= MENÚ =================")

while True:
    opcion = int(input("1. Agregar Puesto de Trabajo\n2. Mostrar todos los puestos\n3. Borrar puesto\n4. Buscar sueldo\n5. Puestos a contratar\nElige una opción: "))
    if(opcion == 1):
        codigo = input("Ingrese el codigo del puesto: ")
        descripcion = input("Ingrese la descripcion del puesto: ")
        area_solicitante = input("Ingrese el area solicitante del puesto: ")
        plazas_requeridas = int(input("Ingrese las plazas requeridas del puesto: "))
        sueldo = float(input("Ingrese el sueldo del puesto: "))
        
        nuevo_puesto = Puesto_de_Trabajo(codigo, descripcion, area_solicitante, plazas_requeridas, sueldo)
        if AgregarPuesto(lista, nuevo_puesto):
            print("Puesto agregado exitosamente.")
        else:
            print("El código del puesto ya existe. No se pudo agregar.")
    elif (opcion == 2):
        MostrarPuestos(lista)
    elif (opcion == 3):        
        print("Ordenado de mayor a menor por código: ")
        OrdenarBurbuja(lista)
        cod = input("Ingrese el código del puesto a eliminar: ")
        for idx, q in enumerate(lista):
            if q.codigo == cod:
                del lista[idx] 
                print("Puesto eliminado exitosamente.")
                break
    elif (opcion == 4):
        print("Ordenado de mayor a menor por sueldo: ")
        OrdenarInsercion(lista)
        sueldo_buscar = float(input("Ingrese el sueldo a buscar: "))
        # Aquí se implementaría la búsqueda binaria para encontrar los puestos con el sueldo especificado
    elif (opcion == 5):
        print("Ordenado de mayor a menor por total requerido en dinero: ")
        OrdenarSeleccionTotal(lista)
        monto_invertir = float(input("Ingrese el monto total a invertir en salarios: "))
        # Aquí se mostrarían los puestos que se podrían contratar hasta cubrir el monto especificado
    elif(opcion == 6):
        print("Saliendo del programa.")
        break
    
    
        