from PIL import Image
import numpy
import random

def convertirImagenAArchivo(nombreImagen, nombreDestino):
    imagen = Image.open(nombreImagen)
    imagen = imagen.convert('RGB')
    matrizNumpy = numpy.array(imagen)
    archivo = open(nombreDestino, 'w')
    for fila in matrizNumpy:
        for pixel in fila :
            for componente in pixel :
                archivo.write(' ' + str(componente))
            archivo.write(',')
        archivo.write('\n')
    archivo.close()
    return True

def leerArchivo(nombreEntrada):
    archivo = open(nombreEntrada,'r')
    matriz = []
    for i in archivo:
        lista = []
        fila = []
        lista = i.strip(",\n").split(',')
        for pixel in lista :
            aux = pixel.split()
            for e in range(3) :
                aux[e] = int(aux[e])
            fila.append(aux)
        matriz.append(fila)
    return matriz

def convertirMatrizAImagen(matriz, nombreSalida):
    arr = numpy.array(matriz)
    im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
    im.save(nombreSalida)
    return True

def espejo_vertical(nombreEntrada):
    a=leerArchivo(nombreEntrada)
    a.reverse()
    convertirMatrizAImagen(a,'espejo_vertical.jpg')
    return True
            
def espejo_horizontal(nombreEntrada):
    a=leerArchivo(nombreEntrada)
    lista=[]
    for i in range(len(a)):
        b=a[i]
        b.reverse()
        lista.append(b)
    convertirMatrizAImagen(lista,'espejo_horizontal.jpg')
    return True    
    
def escala_grises(nombreEntrada):
    a=leerArchivo(nombreEntrada)
    lista=[]    
    for fila in a:
        lista2=[]
        for r,g,b in fila:
            Nr=r/3
			Ng=g/3
			Nb=b/3
            lista2.append([Nr,Ng,Nb])
        lista.append(lista2)
    convertirMatrizAImagen(lista,'escala_grises.jpg')
    return True

def escala_negativos(nombreEntrada):
    a=leerArchivo(nombreEntrada)
    lista=[]    
    for fila in a:
        lista2=[]
        for r,g,b in fila:
            r=255-r
            g=255-g
            b=255-b
            lista2.append([r,g,b])
        lista.append(lista2)
    convertirMatrizAImagen(lista,'escala_negativos.jpg')
    return True
    
def rotar_90(nombreEntrada):
    a=leerArchivo(nombreEntrada)
    lista=[]
    columnas=range(len(a[0]))
    for i in columnas:
        fila=[]
        for j in range(len(a)):
            r,g,b=a[j][i]
            fila.append([r,g,b])
        lista.append(fila)
    lista2=[]
    for i in range(len(lista)):
        b=lista[i]
        b.reverse()
        lista2.append(b)
    convertirMatrizAImagen(lista2,'rotar_90.jpg')
    return True
    
def todos_somos_chile(nombreEntrada):
    a=leerArchivo(nombreEntrada)
    lista=[]
    filas=len(a)
    columnas=len(a[0])
    az=columnas/3
    rr,rg,rb=232,5,5
    ar,ag,ab=14,7,175
    for i in range(filas/2):
        fila=[]
        for j in range(columnas):
            r,g,b=a[i][j]
            if j in range(az):
                r=(r+ar)/2                
                g=(g+ag)/2
                b=(b+ab)/2
            else:
                r+=100
                g+=100
                b+=100
            fila.append([r,g,b])
        lista.append(fila)
    for i in range(filas/2,filas):
        fila=[]
        for j in range(columnas):
            r,g,b=a[i][j]
            g=(g+rg)/2
            b=(b+rb)/2            
            r=(r+rr)/2              
            fila.append([r,g,b])
        lista.append(fila)
    convertirMatrizAImagen(lista,'todos_somos_chile.jpg')
    return True

def intercambia_color(nombreEntrada,color):
    a=leerArchivo(nombreEntrada)
    lista=[]    
    for fila in a:
        lista2=[]
        for pixel in fila:
            if pixel==color:
                r,g,b=pixel
                lista2.append([r,g,b])
            else:
                r,g,b=pixel
                bn=(r+g+b)/3
                lista2.append([bn,bn,bn])
        lista.append(lista2)
    convertirMatrizAImagen(lista,'intercambia_color.jpg')
    return True	
def glitch(nombreEntrada):
	a = leerArchivo(nombreEntrada)
	pix = [0,0,0] 
	c = 0
	esp = random.randrange(1,40)
	list = []
	mov = random.randrange(1,30)
	flag = True
	for linea in a:
		if esp != c:
			if flag == True:
				for count in range(mov -1):
					linea.append(pix)
				flag = False 
				list.append(linea)
			else:
				linea.reverse()
				for count in range(mov -1):
					linea.append(pix)
				flag = True 
				linea.reverse()
				list.append(linea)
		else:
			c = 0
			esp =random.randrange(1,40)
			for count in range(mov -1):
					linea.append(pix)
			list.append(linea)
		c+=1
	convertirMatrizAImagen(list,'GLICHT.jpg')
	return True
				
				
			

	
	
	
	
	

 