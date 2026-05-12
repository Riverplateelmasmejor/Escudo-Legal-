import os

def limpiar():
    os.system('clear')

# --- MÓDULOS DE NAVEGACIÓN ---
def pantalla_ubicacion():
    limpiar()
    print("📍 [ MÓDULO GPS ACTIVO ]")
    print("-------------------------------")
    print("🛰️ Estado: Satélites Conectados")
    print("📍 Ubicación: Lomas del Mirador")
    print("🧭 Coordenadas: -34.68, -58.53")
    print("-------------------------------")
    print("✅ Reporte enviado a Vanessa.")
    input("\n[ Presioná ENTER para volver ]")

def pantalla_auxilio():
    limpiar()
    print("🚨 [ MODO EMERGENCIA ] 🚨")
    print("-------------------------------")
    print("🎙️ Grabando audio encriptado...")
    print("⚠️ Alerta total disparada.")
    print("-------------------------------")
    input("\n[ Presioná ENTER para desactivar ]")

def mostrar_menu():
    limpiar()
    print("-------------------------------")
    print(" [ ☰ ]    ESCUDO LEGAL    [🔍] ")
    print("-------------------------------")
    print("Usuario: GASTÓN")
    print("\n  1. [  PROTECCIÓN ACTIVA  ]  ")
    print("  2. [  ASISTENCIA LEGAL   ]  ")
    print("\n-------------------------------")
    print(" 🎤 Escuchando: 'Escudo...' ")
    print("-------------------------------")

# --- BUCLE PRINCIPAL (EL CEREBRO) ---
while True:
    mostrar_menu()
    orden = input("Comando de voz: ").lower()

    if "ubicación" in orden or "donde estoy" in orden:
        pantalla_ubicacion()
    
    elif "auxilio" in orden:
        pantalla_auxilio()
        
    elif "salir" in orden:
        print("Cerrando sistema... ¡Cuidate Gastón!")
        break
