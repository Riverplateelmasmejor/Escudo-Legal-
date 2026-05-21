<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Escudo Real - Asistente Legal</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>🛡️ Escudo Real</h1>
        <p class="subtitle">Selecciona el procedimiento que enfrentas:</p>
        
        <div class="menu-botones">
            <button class="btn" onclick="seleccionarEscenario('control_vehicular')">🚗 Control Vehicular</button>
            <button class="btn" onclick="seleccionarEscenario('detencion_policial')">🚨 Detención Policial</button>
            <button class="btn" onclick="seleccionarEscenario('control_identidad')">🪪 Control de Identidad</button>
            <button class="btn" onclick="seleccionarEscenario('ingreso_domicilio')">🏠 Ingreso al Domicilio</button>
            <button class="btn" onclick="seleccionarEscenario('abuso_autoridad')">⚠️ Abuso de Autoridad</button>
        </div>

        <div id="pantalla-informacion" class="hidden">
            <button class="btn-volver" onclick="volverAlMenu()">⬅️ Volver al Menú</button>
            <div id="contenido-legal"></div>
        </div>
    </div>
    <script src="app.js"></script>
</body>
</html>
