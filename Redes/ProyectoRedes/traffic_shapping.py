import pyshark

# Paquetes capturados de cada uno
result = [1690, 20, 143, 1575]
mean = sum(result) / len(result)

# Mostrar el Threshold
print(f" Threshold : {mean}")

# Función para detectar anomalias
def detect_traffic_alteration(pcapng_file):
    # Capturar el paquete
    cap = pyshark.FileCapture(pcapng_file)
    packets = 0

    # Sumar todos los paquetes encontrados
    for pkt in cap:
        try:
            packets += 1 

        except AttributeError:
            pass

    # Analizar los paquetes UDP capturados
    threshold = mean  # Promedio de los paquetes

    # Verificar si los paquetes son menor a los threshold
    if packets < threshold:
        return "Posible alteración de tráfico detectada en la transmisión UDP"
    else:
        return "No se detecta alteración de tráfico en la transmisión UDP"


# Llamar a la función y pasar la ruta del archivo de captura .pcapng
result = detect_traffic_alteration('Captura tmuyalto 15s.pcapng')
print(result)