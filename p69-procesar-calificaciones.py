## Procesar calificaciones de estudiantes 

estudiante = {
    "nombre" : "Brandon Carrillo",
    "edad"   : 22,
    "correo" : "bcarrillo@msn.com",
    "carrera":"Robotica"
}

print(f"\nDiccionario original: \n {estudiante}")
estudiante["calificacion"] = 9.5
estudiante["correro"] = "juanp@gmail.com"
print(f"\nDiccionario actualizao : \n {estudiante}")

print("\nLas llaves :")
for k in estudiante.keys():
    print(k, end=" ")
    
print("\nLos valores:")
for v in estudiante.values():
    print(v, end=" ")

print("\nLlaves y valores a la vez :")
for k, v in estudiante.items():
    print(f"{k:<12} : {v}")