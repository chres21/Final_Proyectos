import psycopg2

conexion1 = psycopg2.connect(database="bd1", user="postgres", password="1")
cursor1=conexion1.cursor()
sql="INSERT INTO aerolinea(CLASE, SERVICIO, TOTAL) values (%s,%s,%s)"



conexion1.commit()
conexion1.close()

#conexion1.commit()

#Definicion de los precios

c1 = 50 #comida en 1ra clase
c2 = 40 #comida en 2da clase
c3 = 25 #comida e 3ra clase

b1 = 35 #bebida en 1era clase
b2 = 25 #bebida en 2da clase
b3 = 10 #bebida en 3ra clase

p1 = 70 #pelicula en 1ra clase
p2 = 55 #pelicula en 2da clase
p3 = 25 #pelicula en 3ra clase

print("Bienvenido a la aerolinea Yisus \n")
print("Primera clase: 1\n")
print("Segunda clase: 2\n")
print("Tercera clase: 3\n")
while(True):
	try:
		clase = int(input("Elija una clase:\n"))
		if clase == 1:
            
			print("Elijio primera clase \n")
			break
		if clase == 2:
            
			print("Elijio segunda clase \n")
			break
		if clase == 3:
            
			print("Elijio tercera clase \n")
			break

		elif clase >= 4:
			print("No existe esa categoria \n")

	except ValueError as e:
		print("caracter no valido")

while(True):

	print("Comida: 1\n")
	print("Bebida: 2\n")
	print("Pelicula: 3\n")
	try:
		servicio = int(input("Elija un servicio especial: \n"))
		if servicio == 1: 
			print("Ha elejido comida como un servicio especial\n")
			break
		if servicio == 2:
			print("Ha elejido bebida como un servicio especial\n")
			break
		if servicio == 3:
			print("Ha elejido pelicula como un servicio especial\n")
			break
		elif servicio >= 4:
			print("No existe ese servicion especial, porfavor vuelva a elegir")

	except ValueError as e:
		print("caracter no valido")
while (True):

	try:
		n = int(input("Cuantas unidades de este servicio desea agregar?: \n"))
		break
	except ValueError as e:
		print("caracter no valido")

servicio1 = n*servicio
print("Usted ha elejido la clase: " + str(clase) + " y una cantidad de: " + str(servicio1) + " servicios espciales. \n")

if clase == 1 & servicio ==1: #1ra clase y comidita
	t1 = c1*servicio1
	print("El total es de: " + str(t1) + " Q\n")

if clase == 2 & servicio == 2: #2da clase y bebidita
	t1 = (c2*servicio1)/2
	print("El total es de: " + str(t1) + " Q\n")

if clase == 3 & servicio == 3: #3ra clase y una peliculita
	t1 = (c3*servicio1)/3
	print("El total es de: " + str(t1) + " Q\n")

if clase == 2 & servicio == 1: #2da clase y bebidita
	t1 = (c2*servicio1)
	print("El total es de: " + str(t1) + " Q\n")

conexion1.close()
