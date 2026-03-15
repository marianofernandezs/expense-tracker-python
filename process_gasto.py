from gasto import Gasto
class ProccesGasto:
    def __init__ (self):
        self.contador = 0
        self.gasto = []
    def add_gasto (self, gasto):
        self.contador += 1
        gasto = {"id": self.contador, "title": gasto.title, "description": gasto.description, "amount": gasto.amount, "date": gasto.date} 
        self.gasto.append(gasto) 
        return f"Gasto succefully saved {self.gasto}"
    def show_gasto (self, id):
        for element in self.gasto:
            index = element.get("id")

            if(index == id):
                return print(f"Este es el gasto {element}")
        else:
            return print("Gasto no encontrado")
    def delete_gasto (self, id):
        for element in self.gasto:
            index = element.get("id")
            if (index == id):
                return self.gasto.remove(element)
        else:
            return "Gasto no encontrado"

