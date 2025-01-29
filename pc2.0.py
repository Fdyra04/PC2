class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = set()  # Guardamos horarios como un conjunto para evitar duplicados

    def asignar_horario(self, hora):
        """Asigna un horario si está disponible."""
        if hora in self.horarios:
            print(f"❌ El conductor {self.nombre} ya tiene asignado el horario {hora}:00.")
            return False
        self.horarios.add(hora)
        print(f"✅ Horario {hora}:00 asignado a {self.nombre}.")
        return True


class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = set()
        self.conductor = None

    def asignar_ruta(self, ruta):
        """Asigna una ruta al bus."""
        self.ruta = ruta
        print(f"✅ Ruta '{ruta}' asignada al bus {self.id_bus}.")

    def asignar_horario(self, hora):
        """Asigna un horario al bus."""
        if hora in self.horarios:
            print(f"❌ El bus {self.id_bus} ya tiene el horario {hora}:00.")
            return False
        self.horarios.add(hora)
        print(f"✅ Horario {hora}:00 asignado al bus {self.id_bus}.")
        return True

    def asignar_conductor(self, conductor, hora):
        """Asigna un conductor validando que no tenga otro bus en el mismo horario."""
        if conductor in self.horarios:
            print(f"❌ El conductor {conductor.nombre} ya tiene un bus a las {hora}:00.")
            return False
        if hora not in conductor.horarios:
            print(f"❌ El conductor {conductor.nombre} no tiene el horario {hora}:00 asignado.")
            return False
        self.conductor = conductor
        self.horarios.add(hora)
        print(f"✅ Conductor {conductor.nombre} asignado al bus {self.id_bus} a las {hora}:00.")
        return True


class Admin:
    def __init__(self):
        self.buses = {}
        self.conductores = {}

    def agregar_bus(self):
        """Agrega un nuevo bus."""
        id_bus = input("Ingrese el ID del bus: ")
        if id_bus in self.buses:
            print("❌ Ese bus ya existe.")
            return
        self.buses[id_bus] = Bus(id_bus)
        print(f"✅ Bus {id_bus} agregado correctamente.")

    def agregar_conductor(self):
        """Agrega un nuevo conductor."""
        nombre = input("Ingrese el nombre del conductor: ")
        if nombre in self.conductores:
            print("❌ Ese conductor ya existe.")
            return
        self.conductores[nombre] = Conductor(nombre)
        print(f"✅ Conductor {nombre} agregado correctamente.")

    def agregar_ruta_a_bus(self):
        """Asigna una ruta a un bus."""
        id_bus = input("Ingrese el ID del bus: ")
        if id_bus not in self.buses:
            print("❌ Ese bus no existe.")
            return
        ruta = input("Ingrese la ruta: ")
        self.buses[id_bus].asignar_ruta(ruta)

    def registrar_horario_a_bus(self):
        """Registra un horario a un bus."""
        id_bus = input("Ingrese el ID del bus: ")
        if id_bus not in self.buses:
            print("❌ Ese bus no existe.")
            return
        hora = int(input("Ingrese el horario (solo hora, formato 24h): "))
        self.buses[id_bus].asignar_horario(hora)

    def agregar_horario_a_conductor(self):
        """Agrega un horario disponible a un conductor."""
        nombre = input("Ingrese el nombre del conductor: ")
        if nombre not in self.conductores:
            print("❌ Ese conductor no existe.")
            return
        hora = int(input("Ingrese el horario (solo hora, formato 24h): "))
        self.conductores[nombre].asignar_horario(hora)

    def asignar_bus_a_conductor(self):
        """Asigna un bus a un conductor en un horario validando disponibilidad."""
        id_bus = input("Ingrese el ID del bus: ")
        if id_bus not in self.buses:
            print("❌ Ese bus no existe.")
            return
        nombre = input("Ingrese el nombre del conductor: ")
        if nombre not in self.conductores:
            print("❌ Ese conductor no existe.")
            return
        hora = int(input("Ingrese el horario (solo hora, formato 24h): "))
        
        bus = self.buses[id_bus]
        conductor = self.conductores[nombre]

        if conductor.asignar_horario(hora):  # Verifica si el conductor tiene el horario
            bus.asignar_conductor(conductor, hora)

    def mostrar_menu(self):
        """Menú interactivo para gestionar los buses y conductores."""
        while True:
            print("\n--- MENÚ ---")
            print("1️⃣ Agregar Bus")
            print("2️⃣ Agregar Conductor")
            print("3️⃣ Asignar Ruta a Bus")
            print("4️⃣ Registrar Horario a Bus")
            print("5️⃣ Agregar Horario a Conductor")
            print("6️⃣ Asignar Bus a Conductor")
            print("7️⃣ Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_bus()
            elif opcion == "2":
                self.agregar_conductor()
            elif opcion == "3":
                self.agregar_ruta_a_bus()
            elif opcion == "4":
                self.registrar_horario_a_bus()
            elif opcion == "5":
                self.agregar_horario_a_conductor()
            elif opcion == "6":
                self.asignar_bus_a_conductor()
            elif opcion == "7":
                print(" Saliendo del sistema...")
                break
            else:
                print("❌ incorrecto. Intentelo de nuevo.")


# Crear el sistema y ejecutar el menú
admin = Admin()
admin.mostrar_menu()