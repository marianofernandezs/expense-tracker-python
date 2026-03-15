from gasto import Gasto
from process_gasto import ProccesGasto
from datetime import datetime

user_option = 0
procesator = ProccesGasto() 

while (user_option != 4 and user_option < 5):
    print("Menu de gastos")
    print("1.- Crear un gasto")
    print("2.- Ver gasto")
    print("3.- Eliminar gasto")
    print("4.- Salir ")

    user_option = (int(input("Ingresa opcion a realizar: ")))

    if (user_option == 1):
        title = str(input("El titulo del gasto: "))
        description = str(input("Ingresa la descripcion del gasto: "))
        while True:
            try:
                amount = float(input("Ingrese el monto del gasto en USD: "))        
                break
            except ValueError:
                print("Error: Debes ingresar un numero no una letra o palabras")
        date = str(input("Ingresar la fecha con el siguiente formato, YYYY-MM-DD: "))
        format_date = datetime.strptime(date, "%Y-%m-%d")

        new_gasto = Gasto(title,description,date,amount) #esto es un objeto

        procesator.add_gasto(new_gasto)
        

        print(f"El gasto ha sido creado exitosamente")

    elif (user_option == 2):
        ide = int(input("Ingresa el identificador unico de tu gasto: "))

        procesator.show_gasto(ide)
    elif (user_option == 3):
        index = int(input("Ingresa el identificador unico del gasto a eliminar: "))
        procesator.delete_gasto(index)

