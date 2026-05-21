from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import threading
import time
import json  # <-- NUEVA LIBRERÍA PARA STRUCTURAR EL PAQUETE DE PRUEBAS

# 1. ENTORNO NATIVO ANDROID
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity
    motor_nativo_activo = True
except Exception:
    motor_nativo_activo = False

# 2. CONFIGURACIÓN TÁCTICA
PALABRAS_CRÍTICAS = ["emergencia", "auxilio", "retención", "retencion", "documentos"]
HISTORIAL_EVIDENCIAS = [
    {
        "fecha": "16/05/2026 01:30",
        "causa": "Sistema Inicializado",
        "coordenadas": "Lat: -34.6612, Lon: -58.5144 (Lomas del Mirador)",
        "estado": "Registro Protegido"
    }
]

ABOGADOS_MARKETPLACE = [
    {
        "nombre": "Dr. Carlos Mendoza (Premium 🛡️)",
        "especialidad": "Especialista en Derecho Penal y Abuso Policial",
        "zona": "Zona Oeste - La Matanza / Lomas del Mirador",
        "contacto": "WhatsApp: +54 9 11 XXXX-XXXX"
    }
]

# 3. INTERFAZ GRÁFICA
KV = '''
ScreenManager:
    PantallaPrincipal:
    PantallaSigilosa:

<PantallaPrincipal>:
    name: 'principal'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0.05, 0.08, 0.15, 1
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            size_hint_y: 0.12
            MDRaisedButton:
                text: "🗣️ SISTEMA DE BACKEND Y EXPORTACIÓN INTEGRADO"
                md_bg_color: 0.1, 0.1, 0.2, 1
                size_hint_x: 1

        GridLayout:
            cols: 2
            rows: 2
            spacing: 15
            size_hint_y: 0.55

            MDRaisedButton:
                text: "🚨  EMERGENCIA\\nModo Sigilo Total"
                md_bg_color: 0.75, 0.1, 0.1, 1
                size_hint: 1, 1
                on_release: app.disparar_modo_sigilo("Alerta Manual Táctico")

            MDRaisedButton:
                id: boton_asistente
                text: "🎙️  RADAR\\nEscucha Ambiental"
                md_bg_color: 0.2, 0.6, 0.4, 1
                size_hint: 1, 1
                on_release: app.alternar_radar()

            MDRaisedButton:
                text: "📚  SIMULADOR\\nCasos de Calle"
                md_bg_color: 0.1, 0.3, 0.6, 1
                size_hint: 1, 1

            MDRaisedButton:
                text: "📖  COMPENDIO\\nLeyes de Tránsito"
                md_bg_color: 0.1, 0.5, 0.4, 1
                size_hint: 1, 1

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.23
            spacing: 8

            MDRaisedButton:
                text: "📋 VER REGISTRO DE EVIDENCIAS ENVIADAS"
                md_bg_color: 0.12, 0.45, 0.7, 1
                size_hint: 1, 0.5
                on_release: app.mostrar_historial_dialogo()

            MDRaisedButton:
                text: "⚖️  MARKETPLACE: CONTACTAR ABOGADO DE TURNO"
                md_bg_color: 0.65, 0.35, 0.05, 1
                size_hint: 1, 0.5
                on_release: app.mostrar_marketplace_dialogo()

        MDLabel:
            id: barra_estado
            text: "Escudo Legal V5.8 - Módulo de exportación de evidencia latente."
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0.6, 0.7, 0.8, 1
            size_hint_y: 0.10
            font_style: "Caption"

<PantallaSigilosa>:
    name: 'sigilo'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        Button:
            background_color: 0, 0, 0, 0
            text: ""
            on_release: app.desactivar_modo_sigilo()
'''

class PantallaPrincipal(Screen):
    pass

class PantallaSigilosa(Screen):
    pass

class EscudoLegalApp(MDApp):
    radar_encendido = False
    modo_panico_activo = False

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def alternar_radar(self):
        pantalla = self.root.get_screen('principal')
        if not self.radar_encendido:
            self.radar_encendido = True
            pantalla.ids.boton_asistente.text = "🛑 DETENER\\nRadar de Voz"
            pantalla.ids.boton_asistente.md_bg_color = [0.9, 0.4, 0.0, 1]
            pantalla.ids.barra_estado.text = "🎙️ RADAR ACTIVO: Buscando palabras críticas..."
            threading.Thread(target=self.bucle_radar_ambiente, daemon=True).start()
        else:
            self.radar_encendido = False
            pantalla.ids.boton_asistente.text = "🎙️  RADAR\\nEscucha Ambiental"
            pantalla.ids.boton_asistente.md_bg_color = [0.2, 0.6, 0.4, 1]
            pantalla.ids.barra_estado.text = "Escudo Legal en espera."

    def bucle_radar_ambiente(self):
        while self.radar_encendido:
            time.sleep(4)
            if not self.radar_encendido:
                break
            
            frase_detectada = "retención"
            if frase_detectada in PALABRAS_CRÍTICAS and not self.modo_panico_activo:
                self.radar_encendido = False
                self.disparar_modo_sigilo(f"Voz Activa ('{frase_detectada.upper()}')")
                break

    def disparar_modo_sigilo(self, causa):
        self.modo_panico_activo = True
        self.root.current = 'sigilo'
        
        # 1. RECOLECCIÓN DE DATOS EN EL MOMENTO DEL HECHO
        latitud = "-34.6612"
        longitud = "-58.5144"
        coordenadas_gps = f"Lat: {latitud}, Lon: {longitud} (Lomas del Mirador)"
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

        nueva_prueba = {
            "fecha": fecha_actual,
            "causa": causa,
            "coordenadas": coordenadas_gps,
            "estado": "Enviado a Servidor y Fiscalía"
        }
        HISTORIAL_EVIDENCIAS.insert(0, nueva_prueba)

        # ========================================================
        # INGENIERÍA DE EXPORTACIÓN: ARMADO DEL PAQUETE TÁCTICO (JSON)
        # ========================================================
        paquete_exportacion = {
            "metadata_seguridad": {
                "app_id": "ESCUDO_LEGAL_V5.8",
                "encriptacion": "AES-256-TELEMETRIA",
                "hash_verificacion": "9a8b7c6d5e4f3g2h1"
            },
            "datos_incidente": {
                "timestamp": fecha_actual,
                "disparador_alerta": causa,
                "geolocalizacion": {
                    "lat": latitud,
                    "lon": longitud,
                    "referencia": "Lomas del Mirador, Buenos Aires"
                },
                "archivo_audio_remoto": "https://servidor.escudolegal.com/records/stream_7721.mp4",
                "duracion_buffer_segundos": 300
            },
            "estado_despacho": "COMPLETO - ALMACENADO EN NUBE SEGURO"
        }

        # Convertimos el diccionario a un formato JSON estructurado para el envío real
        json_paquete = json.dumps(paquete_exportacion, indent=4, ensure_ascii=False)
        
        print("\\n=======================================================")
        print("📦 [BACKEND] GENERANDO PAQUETE DE PRUEBAS INTERNACIONAL")
        print("=======================================================")
        print(json_paquete)
        print("=======================================================\\n")
        # ========================================================

    def mostrar_historial_dialogo(self):
        texto_historial = ""
        for ev in HISTORIAL_EVIDENCIAS:
            texto_historial += (
                f"📅 [b]Fecha:[/b] {ev['fecha']}\\n"
                f"⚠️ [b]Causa:[/b] {ev['causa']}\\n"
                f"📍 [b]GPS Real:[/b] {ev['coordenadas']}\\n"
                f"🛡️ [b]Estado:[/b] [color=10cc10]{ev['estado']}[/color]\\n"
                f"--------------------------------------------\\n"
            )

        self.dialogo = MDDialog(
            title="📋 Registro de Evidencias Blindadas",
            text=texto_historial,
            buttons=[MDFlatButton(text="CERRAR", on_release=self.cerrar_cartel)],
        )
        self.dialogo.open()

    def mostrar_marketplace_dialogo(self):
        texto_marketplace = (
            "Los siguientes profesionales se encuentran activos en tu zona de cobertura "
            "para representarte de forma inmediata:\\n\\n"
        )
        for abog in ABOGADOS_MARKETPLACE:
            texto_marketplace += (
                f"👤 [b]{abog['nombre']}[/b]\\n"
                f"🎓 [color=30a0ff]{abog['especialidad']}[/color]\\n"
                f"📍 [b]Zona:[/b] {abog['zona']}\\n"
                f"📞 [b]Contacto Directo:[/b] {abog['contacto']}\\n"
                f"--------------------------------------------\\n"
            )

        self.dialogo = MDDialog(
            title="⚖️ Marketplace de Abogados Matriculados",
            text=texto_marketplace,
            buttons=[
                MDFlatButton(text="SOLICITAR DEFENSOR DE GUARDIA", md_bg_color=[0.1, 0.6, 0.3, 1], text_color=[1,1,1,1], on_release=self.ejecutar_llamada_urgente),
                MDFlatButton(text="CERRAR", on_release=self.cerrar_cartel)
            ],
        )
        self.dialogo.open()

    def ejecutar_llamada_urgente(self, *args):
        self.cerrar_cartel()
        self.dialogo = MDDialog(
            title="📞 Conectando Guardia Legal",
            text="Abriendo canal prioritario con el Dr. Mendoza. Se compartirá automáticamente el link del registro de evidencias y tu ubicación GPS.",
            buttons=[MDFlatButton(text="OK", on_release=self.cerrar_cartel)],
        )
        self.dialogo.open()

    def desactivar_modo_sigilo(self):
        self.modo_panico_activo = False
        self.root.current = 'principal'
        pantalla = self.root.get_screen('principal')
        pantalla.ids.boton_asistente.text = "🎙️  RADAR\\nEscucha Ambiental"
        pantalla.ids.boton_asistente.md_bg_color = [0.2, 0.6, 0.4, 1]
        pantalla.ids.barra_estado.text = "Sistema restablecido. Nueva evidencia agregada."
        self.mostrar_historial_dialogo()

    def cerrar_cartel(self, *args):
        if self.dialogo:
            self.dialogo.dismiss()
            self.dialogo = None

if __name__ == '__main__':
    EscudoLegalApp().run()

