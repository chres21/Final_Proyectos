import psycopg2
#paso 1: crear conexion con BD
conn = psycopg2.connect(
    host = 'localhost',
    database = 'bd1',
    user = 'postgres',
    password = '1'
)
print("Conexion exitosa")

#Paso 2: crear cursor
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS PROGRAMA4")

sql1 = """CREATE TABLE AEROLINEA(
    CLASE CHAR(100),
    SERVICIO CHAR(100),
    TOTAL CHAR(100)
)"""


cursor.execute(sql1)
conn.commit()

print("Tabla creada con exito")





#Paso final
conn.close()