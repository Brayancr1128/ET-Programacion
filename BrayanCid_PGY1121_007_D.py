from os import system
system ("cls")

total=0
cant=0
entrada=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]]
run=[]

platinum=120000
gold=80000
silver=50000

while True:
    print("""
    1. Comprar entrada
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganacias totales
    5. Salir
    """)
    op=input("Ingrese opcion deseada: ")
    match op:
        case "1":
            while True:
                cant=int(input("Ingrese la cantidad de entradas: "))
                if cant >=1 and cant <=3:
                    print(entrada)
                    asiento=int(input("Ingrese el numero de asiento: "))
                    if asiento >=1 and asiento <=20:
                            total=cant*platinum
                    elif asiento >=21 and asiento <=50:
                            total=cant*gold
                    elif asiento >=51 and asiento <=100:
                            total=cant*silver

                    entrada.remove(asiento)

                    asistente=input("Ingrese su run sin punto ni digito verificador: ")
                    run=[asistente]
                    break

                else:
                    print("Solo de 1 a 3 entradas")

        case "2":
              print(entrada)


        case "3":

            run.sort()
            print(run)

        case "4":
              print(f"Gnanacias totales= {total}")

        case "5":
            print("""
            Salio del Sistema
            Brayan Cid
            10/07/2023
            """)
            break