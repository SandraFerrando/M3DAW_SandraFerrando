class Compte:
    def __init__(self, nom, telefon, email, quantitat):
        self.nom = nom
        self.telefon = telefon
        self.email = email
        self.quantitat = quantitat

    def mostrar_dades(self):
        return f"Nom: {self.nom}, Telèfon: {self.telefon}, Email: {self.email}, Quantitat: {self.quantitat}"

class Fixe(Compte):
    def __init__(self, nom, telefon, email, quantitat, plaç, interès):
        super().__init__(nom, telefon, email, quantitat)
        self.plaç = plaç
        self.interès = interès

    def obtenir_interès(self):
        return self.quantitat * self.interès / 100

    def mostrar_informacio(self):
        interès_total = self.obtenir_interès()
        return (f"Dades del titular: {self.mostrar_dades()}, Plaç: {self.plaç} anys, "
                f"Interès: {self.interès}%, Total amb interès: {self.quantitat + interès_total}")

class Estalvi(Compte):
    def mostrar_estalvis(self):
        return f"Dades del titular: {self.mostrar_dades()}, Estalvis: {self.quantitat}"

def mostrar_menu():
    print("\nMenú:")
    print("1. Afegir un client")
    print("2. Llistar clients")
    print("3. Mostrar les dades d'un client")
    print("4. Buscar client")
    print("5. Modificar un client")
    print("6. Eliminar un client")
    print("7. Sortir")

clients = []

# Creació d'objectes de cada subclasse
client_fixe = Fixe("Joan", "123456789", "joan@example.com", 1000, 5, 3)
client_estalvi = Estalvi("Maria", "987654321", "maria@example.com", 5000)

clients.append(client_fixe)
clients.append(client_estalvi)

while True:
    mostrar_menu()
    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        nom = input("Nom: ")
        telefon = input("Telèfon: ")
        email = input("Email: ")
        quantitat = float(input("Quantitat: "))
        tipus = input("Tipus de compte (fixe/estalvi): ").lower()
        if tipus == "fixe":
            plaç = int(input("Plaç (en anys): "))
            interès = float(input("Interès: "))
            clients.append(Fixe(nom, telefon, email, quantitat, plaç, interès))
        elif tipus == "estalvi":
            clients.append(Estalvi(nom, telefon, email, quantitat))
        else:
            print("Tipus de compte no vàlid.")
    
    elif opcio == "2":
        for client in clients:
            print(client.mostrar_dades())
    
    elif opcio == "3":
        nom = input("Introdueix el nom del client: ")
        for client in clients:
            if client.nom == nom:
                if isinstance(client, Fixe):
                    print(client.mostrar_informacio())
                elif isinstance(client, Estalvi):
                    print(client.mostrar_estalvis())
                break
        else:
            print("Client no trobat.")
    
    elif opcio == "4":
        nom = input("Introdueix el nom del client a buscar: ")
        for client in clients:
            if client.nom == nom:
                print(client.mostrar_dades())
                break
        else:
            print("Client no trobat.")
    
    elif opcio == "5":
        nom = input("Introdueix el nom del client a modificar: ")
        for client in clients:
            if client.nom == nom:
                client.telefon = input("Nou telèfon: ")
                client.email = input("Nou email: ")
                client.quantitat = float(input("Nova quantitat: "))
                print("Client modificat amb èxit.")
                break
        else:
            print("Client no trobat.")
    
    elif opcio == "6":
        nom = input("Introdueix el nom del client a eliminar: ")
        for client in clients:
            if client.nom == nom:
                clients.remove(client)
                print("Client eliminat amb èxit.")
                break
        else:
            print("Client no trobat.")
    
    elif opcio == "7":
        print("Sortint...")
        break
    
    else:
        print("Opció no vàlida. Prova de nou.")
