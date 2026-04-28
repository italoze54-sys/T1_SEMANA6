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


def AgregarPuesto(lista, puesto):
    if (len(puesto.descripcion) < 3 or len(puesto.area_solicitante) < 3):
        print("Los campos de texto deben tener al menos 3 caracteres.")
        return False
    elif puesto.plazas_requeridas <= 0 or puesto.sueldo <= 0:
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
        

def OrdenarBurbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j].codigo < lista[j+1].codigo:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(lista)

def OrdenarInsercion(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j].sueldo < key.sueldo:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    print(lista)

def BuscarSueldo(lista, sueldo):
    izq = 0
    der = len(lista) - 1
    
    while izq <= der:
        mid = (izq + der) // 2
        
        if lista[mid].sueldo == sueldo:
            print("Encontrados:")
            
            print(lista[mid])
            
            i = mid - 1
            while i >= 0 and lista[i].sueldo == sueldo:
                print(lista[i])
                i -= 1
            
            # derecha
            i = mid + 1
            while i < len(lista) and lista[i].sueldo == sueldo:
                print(lista[i])
                i += 1
            
            return
        
        elif lista[mid].sueldo < sueldo:
            der = mid - 1  
        else:
            izq = mid + 1
    
    print("No se encontró ese sueldo")


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
    
def PuestosAContratar(lista, monto):
    total_usado = 0
    
    print("Puestos que se pueden contratar:")
    
    for p in lista:
        costo = p.plazas_requeridas * p.sueldo
        
        if total_usado + costo <= monto:
            print(p)
            total_usado += costo
    
    print("Total usado:", total_usado)
    
lista = []
print("================= MENÚ =================")

while True:
    opcion = int(input("1. Agregar Puesto de Trabajo\n2. Mostrar todos los puestos\n3. Borrar puesto\n4. Buscar sueldo\n5. Puestos a contratar\n6. Salir\nElige una opción:"))
    
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
        BuscarSueldo(lista, sueldo_buscar)
    
    elif (opcion == 5):
        print("Ordenado de mayor a menor por total requerido en dinero: ")
        OrdenarSeleccionTotal(lista)
        monto_invertir = float(input("Ingrese el monto total a invertir en salarios: "))
        PuestosAContratar(lista, monto_invertir)
       
    elif(opcion == 6):
        print("Saliendo del programa.")
        break    
    
        