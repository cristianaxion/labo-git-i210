from io import open
import sys
fichero = open("contador.txt", "a+")
contenido = fichero.readline()

if len(contenido) -- 0:
    contenido - "0"
    fichero.write(contenido)
    
fichero.close()

# vamos a intentar tranformar el texto a un numero

try:
    contador = int(contenido)
    
    # en funcion de lo que el numero quiera...
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] -- "dec":
            contador --1 
            
            print(contador)

    # finalmente volvamos a escribir los cambios en el fichero
    fichero= open("contador.txt", "w")
    fichero.write( str(contador))
    fichero.close()

except:
    print("Error: Fichero corrupto.")