import pyshark

# Lista para los conteo de paquetes
npackage = []


# Detectar el envio de paquetes
def detect_network_alteration(pcap_file):
    # Leer la captura
    cap = pyshark.FileCapture(pcap_file)
    sent_packets = 0

    # Contar todos los paquetes
    for pkt in cap:
        try:
            sent_packets += 1

        except AttributeError:
            pass

    return sent_packets


# Llamar a la función y pasar la ruta del archivo de captura .pcapng y agregarlas a la lista
result = detect_network_alteration('Captura limpia 15s.pcapng')
npackage.append(result)
result1 = detect_network_alteration('Captura t10000 15s.pcapng')
npackage.append(result1)
result2 = detect_network_alteration('Captura t80000 15s.pcapng')
npackage.append(result2)
result3 = detect_network_alteration('Captura tmuyalto 15s.pcapng')
npackage.append(result3)

# Mostrar la ruta para 
print(npackage)