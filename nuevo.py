import os
import sys

# Base de datos de protocolos de emergencia (Argentina)
protocolos = {
    "1": {
        "titulo": "🚗 CONTROL VEHICULAR",
        "pasos": [
            "Mantén las manos sobre el volante en un lugar visible.",
            "Apaga el motor y enciende la luz interna si es de noche.",
            "Presenta únicamente Licencia, Cédula y Seguro obligatorio."
        ],
        "denuncia": "Línea 134 (Fuerzas Federales) o Fiscalía Local."
    },
    "2": {
        "titulo": "🚨 DETENCIÓN POLICIAL",
        "pasos": [
            "Pregunta inmediatamente el motivo exacto de la detención.",
            "Tienes derecho a guardar silencio hasta hablar con tu abogado.",
            "Exige hacer una llamada telefónica inmediata a un familiar."
        ],
        "denuncia": "Línea 0800-122-5878 (Secretaría de DD.HH.)"
    },
    "3": {
        "titulo": "🪪 CONTROL DE IDENTIDAD",
        "pasos": [
            "Exhibe tu DNI. No pueden retenértelo sin una causa legal.",
            "La demora para acreditar identidad tiene un límite de horas por ley.",
            "Anota discretamente el nombre y legajo del oficial."
        ],
        "denuncia": "Línea 134 o Ministerio de Seguridad de la Nación."
    },
    "4": {
        "titulo": "🏠 INGRESO AL DOMICILIO",
        "pasos": [
            "Exige ver la orden de allanamiento escrita y firmada por un juez.",
            "Verifica que la dirección en el documento sea exactamente la tuya.",
            "Busca testigos (vecinos) para que presencien todo el operativo."
        ],
        "denuncia": "Línea 0800-33-FISCAL (CABA) o llama a servicios de emergencia ante falsos oficiales."
    },
    "5": {
        "titulo": "⚠️ ABUSO DE AUTORIDAD",
        "pasos": [
            "Mantén la calma por completo y nunca te resistas físicamente.",
            "Graba video o audio de forma discreta si es seguro hacerlo.",
            "Identifica el número de patrullero, chaleco o la chapa del oficial."
        ],
        "denuncia": "Línea Nacional: 0800-122-5878 | WhatsApp: +54 11-4091-7352"
    }
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpiar_pantalla()
        print("=========================================")
        print("          🛡️  ESCUDO REAL v1.0          ")
        print("=========================================")
        print(" Selecciona el procedimiento que enfrentas:\n")
        print(" [1] Control Vehicular")
        print(" [2] Detención Policial")
        print(" [3] Control de Identidad")
        print(" [4] Ingreso al Domicilio")
        print(" [5] Abuso de Autoridad")
        print(" [0] Salir de la aplicación")
        print("=========================================")
        
        opcion = input("\nIngresa un número (0-5): ").strip()
        
        if opcion == "0":
            print("\nCerrando Escudo Real. Mantente a salvo.")
            sys.exit()
        elif opcion in protocolos:
            mostrar_protocolo(opcion)
        else:
            input("\n❌ Opción inválida. Presiona ENTER para intentar de nuevo...")

def mostrar_protocolo(id_opcion):
    info = protocolos[id_opcion]
    limpiar_pantalla()
    print("=========================================")
    print(f" {info['titulo']} ")
    print("=========================================")
    print("\nPASOS INMEDIATOS:")
    for paso in info['pasos']:
        print(f" 🔹 {paso}")
        
    print("\n-----------------------------------------")
    print(" 🚨 CANAL DE DENUNCIA:")
    print(f" {info['denuncia']}")
    print("=========================================")
    
    input("\n⬅️ Presiona ENTER para volver al menú principal...")

if __name__ == "__main__":
    menu_principal()
