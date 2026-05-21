const protocolos = {
    control_vehicular: {
        titulo: "🚗 Control Vehicular",
        pasos: ["Mantén las manos sobre el volante.", "Apaga el motor y enciende la luz interna si es de noche.", "Presenta Licencia, Cédula y Seguro obligatorio."],
        denuncia: "Línea 134 (Fuerzas Federales) o Fiscalía Local."
    },
    detencion_policial: {
        titulo: "🚨 Detención Policial",
        pasos: ["Pregunta inmediatamente el motivo de la detención.", "Tienes derecho a guardar silencio hasta hablar con un abogado.", "Exige hacer una llamada telefónica a un familiar."],
        denuncia: "Línea 0800-122-5878 (Secretaría de DD.HH.)"
    },
    control_identidad: {
        titulo: "🪪 Control de Identidad",
        pasos: ["Exhibe tu DNI. No pueden retenértelo sin causa.", "La demora para acreditar identidad tiene un límite de horas legal.", "Anota el nombre y legajo del oficial que te lo solicita."],
        denuncia: "Línea 134 o Ministerio de Seguridad."
    },
    ingreso_domicilio: {
        titulo: "🏠 Ingreso al Domicilio",
        pasos: ["Exige ver la orden de allanamiento escrita y firmada por un juez.", "Verifica que la dirección en el papel sea exactamente la tuya.", "Busca testigos (vecinos) para que presencien el operativo."],
        denuncia: "Línea 0800-33-FISCAL (Si es en CABA) o emergencias ante falsos oficiales."
    },
    abuso_autoridad: {
        titulo: "⚠️ Abuso de Autoridad",
        pasos: ["Mantén la calma y no te resistas físicamente.", "Graba video o audio si es seguro hacerlo.", "Identifica número de patrullero, chaleco o placa."],
        denuncia: "Línea Nacional: 0800-122-5878 | WhatsApp: +54 11-4091-7352"
    }
};

function seleccionarEscenario(id) {
    const info = protocolos[id];
    const contenedorMenu = document.querySelector('.menu-botones');
    const pantallaInfo = document.getElementById('pantalla-informacion');
    const contenido = document.getElementById('contenido-legal');

    if (!info) return;

    contenedorMenu.style.display = 'none';
    pantallaInfo.classList.remove('hidden');

    contenido.innerHTML = `
        <h2>${info.titulo}</h2>
        <h3>Pasos inmediatos:</h3>
        <ul>${info.pasos.map(paso => `<li>${paso}</li>`).join('')}</ul>
        <div class="alerta-denuncia">
            <strong>Canal de Denuncia:</strong><br>${info.denuncia}
        </div>
    `;
}

function volverAlMenu() {
    document.querySelector('.menu-botones').style.display = 'flex';
    document.getElementById('pantalla-informacion').classList.add('hidden');
}
