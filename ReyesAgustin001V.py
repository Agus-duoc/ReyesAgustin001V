def mostrar_menu():
    print("1. Unidades por categoría")
    print("2. Búsqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    
#===================================================================

def leer_opcion():
    while True:
        try:
            opcion=int(input('ingrese opcion: '))
            if opcion >=1 and opcion <=6:
                return opcion
            else:
                print('opcion invalida, ingrese una opcion disponible entre 1 y 6')
                mostrar_menu()
        except ValueError:
            print('valor incorrecto, debe ingresar un numero entero')
            
#=========================================================================

def buscar_codigo(prendas,bodega,codigo):
    codigo = codigo.strip().upper()
    for key in prendas:
        if codigo == key.upper():
            return True
    return False

#============================================================================
def unidades_categoria(prendas,bodega,categoria):
    categoria=categoria.strip().lower()
    acumulador=0
    encontrada=False
    for cod,datos in prendas.items():
        if  datos[1] == categoria:
            if cod in bodega:
                med = bodega[cod]
                acumulador+= bodega[cod][1]
                            
    print(f'la categoria {categoria} tiene un total de: {acumulador}')
   
        
#=============================================================================
def eliminar_prenda(prendas, bodega, codigo):
    if buscar_codigo(prendas,bodega,codigo):
        del prendas[codigo]
        del bodega[codigo]
        return True
    return False

#==========================================================================
def actualizar_precio(codigo,nuevo_precio,prendas,bodega):
    codigo=codigo.strip().upper()
    if buscar_codigo(prendas,bodega,codigo):
        bodega[codigo][0] = nuevo_precio
        return True
    return False
#============================================================================
def agregar_prenda(nuevo_codigo,nuevo_nombre, nueva_categoria, nueva_talla,nuevo_color,nuevo_material,es_unisex, nuevo_precio,nuevas_unidades,prendas,bodega):
    prendas[nuevo_codigo] = [nuevo_nombre,nueva_categoria,nueva_talla,nuevo_color,nuevo_material,es_unisex]
    bodega[nuevo_codigo] = [nuevo_precio,nuevas_unidades]
    return True
    

#==================================================================================
def busqueda_precio(prendas, bodega, min, max):
    resultado = []
    

    for codigo_producto, datos in bodega.items():
  
        if datos[0] >= min and datos[0] <= max and datos[1] != 0:
            ropa = prendas[codigo_producto]
            resultado.append({
                'codigo' : codigo_producto,
                'nombre' : ropa[0],
                'categoria':ropa[1],
                'talla' :   ropa[2],
                'color' : ropa[3],
                'material' : ropa[4] ,
                'unisex' : ropa[5] ,
                'precio' : datos[0] ,
                'unidades': datos[1]
            })

    if len(resultado) == 0:
        print('No hay productos con ese rango de precio.')
    else:
        for i in resultado:
            print(f'codigo: {i["codigo"]}')
            print(f'nombre: {i["nombre"]}')
            print(f'categoria: {i["categoria"]}')
            print(f'talla: {i["talla"]}')
            print(f'color: {i["color"]}')
            print(f'material: {i["material"]}')
            print(f'unisex: {i["unisex"]}')
            print(f'precio: {i["precio"]}')
            print(f'unidades: {i["unidades"]}')
            print('--------------------------------------')
    return

#=======================================================================================
def texto_no_vacio(texto):
    return texto.strip() != ''
#=======================================================================================
def validar_nuevocodigo(nuevo_codigo,prendas,bodega):
    nuevo_codigo =nuevo_codigo.strip().upper()
    if nuevo_codigo == '':
        return False
    if buscar_codigo(prendas,bodega,nuevo_codigo):
        return False
    return True
#=======================================================================================
def validar_unisex(texto):
    return texto.strip().lower() in ("s" , "n")
#======================================================================================

def validar_precio(precio):
    if precio <= 0:
        return False
    return True
#========================================================================================
def validar_unidades(nuevas_unidades):
    if nuevas_unidades < 0:
        return False
    return True
#=========================================================================================
def main():
    prendas = {
    'S001': ['polera', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['jeans', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['chaqueta', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['polar', 'abrigo', 'S', 'rojo', 'lino', False],
    'S005': ['poleron', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['camisa', 'camisa', 'M', 'blanco', 'algodon', False],
}
    bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
}


    
    while True:
        mostrar_menu()
        opcion=leer_opcion()
        match opcion:
            case 1:
                categoria=input('ingrese categoria a buscar: ').strip().lower()
                unidades_categoria(prendas,bodega,categoria)                
                
            case 2:
                while True:
                    try:
                        min=int(input('ingrese cantidad minima: '))
                        if min < 0:
                            print('debe ser un valor mayor a cero')
                        else:
                            break
                    except ValueError:
                        print('valor no valido')
                while True:                    
                    try:
                        max=int(input('ingrese cantidad maxima: '))
                        if max < min:
                            print('el maximo no puede ser menor que el minimo')
                        else:
                            break
                    except ValueError:
                        print('valor no valido')
                busqueda_precio(prendas,bodega,min,max)
                                
            case 3:
                while True:
                    codigo=input('ingrese codigo de la prenda: ')
                    try:
                        nuevo_precio=int(input('ingrese nuevo precio: '))
                        if nuevo_precio <= 0:
                            print('el precio debe ser un entero mayor a cero')
                        else:
                            if actualizar_precio(codigo,nuevo_precio,prendas,bodega):
                                print('precio actualizado')
                            else:
                                print('codigo no existe')
                    except ValueError:
                        print('error, debe ingresar un numero positivo')
                        
                    respuesta=input('¿desea agregar otro precio(s/n)?: ').strip().lower()
                    if respuesta != 's':
                        break
            case 4:
                nuevo_codigo=input('ingrese nuevo codigo: ')
                nuevo_nombre=input('ingrese nuevo nombre: ')
                nueva_categoria=input('ingrese nueva categoria: ')
                nueva_talla=input('ingrese nueva talla: ')
                nuevo_color=input('ingrese nuevo color: ')
                nuevo_material=input('ingrese nuevo material: ')
                es_unisex=input('ingrese si prenda es unisex(s/n): ')
               
                while True:
                    try:
                        nuevo_precio=int(input('ingrese nuevo precio: '))
                        break
                    except ValueError:
                        print('error, debe ingresar un numero entero')
                        
                while True:
                    try:
                        nuevas_unidades=int(input('ingrese nuevas unidades: '))
                        break
                    except ValueError:
                        print('error, debe ingresar numero entero')
                        
                if not validar_nuevocodigo(nuevo_codigo,prendas,bodega):
                    print('error, el codigo no es valido ')
                elif buscar_codigo(prendas,bodega,nuevo_codigo):
                    print('el codigo ya existe')
                elif not texto_no_vacio(nuevo_nombre):
                    print('error, no debe estar el texto vacio')
                elif not texto_no_vacio(nueva_categoria):
                    print('error, no debe ingresar texto vacio')
                elif not texto_no_vacio(nueva_talla):
                    print('error, no debe ingresar texto vacio')
                elif not texto_no_vacio(nuevo_color):
                    print('error, no debe ingresar texto vacio')
                elif not texto_no_vacio(nuevo_material):
                    print('error, no debe ingresar un texto vacio')
                elif not validar_unisex(es_unisex):
                    print('error, debe ingresar s o n')
                elif not validar_precio(nuevo_precio):
                    print('error, debe ingresar un numero entero mayor a cero')
                elif not validar_unidades(nuevas_unidades):
                    print('error, debe ingresar un numero entero positivo')
                else:
                    agregar_prenda(nuevo_codigo,nuevo_nombre,nueva_categoria,nueva_talla,nuevo_color,nuevo_material,es_unisex,nuevo_precio,nuevas_unidades,prendas,bodega)
                    print('prenda agregada con exito')        
                        
            case 5:
                codigo=input('ingrese codigo: ').strip().upper()  
                if eliminar_prenda(prendas,bodega,codigo):
                    print('prenda eliminada con exito')
                else:
                    print('prenda no encontrada')
            case 6:
                print('Programa finalizado.')
                break
main()


     

    

    


        
    