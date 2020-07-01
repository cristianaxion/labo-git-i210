from io import open

filchers = open( 'personas.txt','r', encoding= "utf8" )
linear = filchers.readline()
filchers.close()

personas = []
for line in linear:
    # borramos los saltos de linea y separamos
    campos = line.replace("\n", "").split(";")
    persona = {"id":campos[0], "nombre":campos[1],
              "apellido":campos[2], "nacimiento":campos[3]}
    personas.append(persona)
    
    for p in personas:
        print("(id={}) {} {} => {} ".format(p['id'], p['nombre'],
                                            p['apellido'], p['nacimiento']))