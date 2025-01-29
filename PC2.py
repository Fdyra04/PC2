class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = set()

class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = {}
    
    def asignar_ruta(self, ruta):
        self.ruta = ruta
        print(f"✅ Ruta '{ruta}' asignada al bus {self.id_bus}.")

    def asignar_horario(self, hora, conductor):
        if hora in self.horarios:
            print(f"❌ El horario {hora}:00 ya está asignado a otro conductor.")
        else:
            self.horarios[hora] = conductor
            conductor.horarios.add(hora)
            print(f"✅ Horario {hora}:00 asignado a {conductor.nombre} en el bus {self.id_bus}.")

class Admin:
    def __init__(self):
        self.buses = {}
        self.conductores = {}

    def agregar_bus(self):
        id_bus = input("Ingrese el ID del bus: ")
        self.buses[id_bus] = Bus(id_bus)
        print(f"✅ Bus {id_bus} agregado.")

    def agregar_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        self.conductores[nombre] = Conductor(nombre)
        print(f"✅ Conductor {nombre} agregado.")

    def asignar_ruta_a_bus(self):
        id_bus = input("Ingrese el ID del bus: ")
        if id_bus in self.buses:
            ruta = input("Ingrese la ruta: ")
            self.buses[id_bus].asignar_ruta(ruta)
        else:
            print("❌ Bus no encontrado.")

    def asignar_horario_a_bus(self):
        id_bus = input("Ingrese el ID del bus: ")
        nombre = input("Ingrese el nombre del conductor: ")
        if id_bus in self.buses and nombre in self.conductores:
            hora = int(input("Ingrese el horario (formato 24h): "))
            self.buses[id_bus].asignar_horario(hora, self.conductores[nombre])
        else:
            print("❌ Bus o conductor no encontrado.")

    def menu(self):
        while True:
            print("\n1. Agregar Bus\n2. Agregar Conductor\n3. Asignar Ruta a Bus\n4. Asignar Horario a Bus\n5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_bus()
            elif opcion == "2":
                self.agregar_conductor()
            elif opcion == "3":
                self.asignar_ruta_a_bus()
            elif opcion == "4":
                self.asignar_horario_a_bus()
            elif opcion == "5":
                print("👋 Saliendo...")
                break
            else:
                print("❌ Opción inválida.")

admin = Admin()
admin.menu()