Proyecto Realizado con : 

*[Cristian Herrera B.](https://github.com/Sphad7) 
*[Cristóbal Lagos V.](https://github.com/X4ero26)

El objetivo del presente proyecto es implementar una red IP que permita realizar un streaming de video. De esta forma, debemos definir e implementar desde el protocolo de ruteo hasta la configuración de los nodos de la red (incluyendo routers y máquinas virtuales). Adicionalmente, debemos realizar un análisis de desempeño de la red, mediante la aplicación de traffic shapping, y la implementación de un detector de alteración de tráfico.

## Herramientas necesarias:

* GNS3
* Wireshark
* VirtualBox
* VLC.

## Escenario de red 

Crear el proyecto en GNS3 y tiene que quedar de la siguiente manera:
[![Escenario-de-Red.png](https://i.postimg.cc/ZKYc6BLd/Escenario-de-Red.png)](https://postimg.cc/t7fWjgwq)

## Configuraciones de los routers
Iniciamos el entorno y a cada router se le deben hacer las siguientes configuraciones. (Escribir "config t" en el terminal y luego los comandos que aparecen a continuación)

### Asignación de las IPs de los routers

[![Asignacion-de-las-ips.png](https://i.postimg.cc/cCWNFMJZ/Asignacion-de-las-ips.png)](https://postimg.cc/BLmy6FDw)

### Asignación de las rutas de los routers

[![Rutas.png](https://i.postimg.cc/8zJnrf1b/Rutas.png)](https://postimg.cc/v4yvJBx1)

Para comprobar que todo está correcto, debería aparecer lo siguiente al ejecutar el comando "show ip route"

[![C.png](https://i.postimg.cc/bJNxk4xj/C.png)](https://postimg.cc/NyS2wJCN)

## Configuración de los routers

Al iniciar el entorno en GNS3 se nos debieron haber abierto nuestras maquinas virtuales con Lubuntu y Ubuntu, verificamos que nuestras preferencias de red de la máquina virtual se vean de la siguiente manera:

[![MV.png](https://i.postimg.cc/pLch3y83/MV.png)](https://postimg.cc/1863qmvK)

### Configuraciones de red

A cada máquina virtual le asignamos las siguientes configuraciones:

#### Lubuntu:
[![Lubu.png](https://i.postimg.cc/g0rSPw7h/Lubu.png)](https://postimg.cc/QBGkQMhN)
#### Ubuntu:
[![Ubuntu.png](https://i.postimg.cc/0QwVbTP2/Ubuntu.png)](https://postimg.cc/tZ93cmsL)

## Transmisión del video

* **Parte del servidor:** Abrir VLC media player, luego ir a Stream, añadimos el archivo .mp4 que queremos transmitir luego apretamos el botón Stream, Next, cambiamos el formato a UDP (legacy) y apretamos el botón Add, en Address agregamos la dirección a la cuál queremos enviar (En este caso es 192.168.60.60) y dejamos el puerto 1234, apretamos Next. Ahora en transcoding elegimos Video - H.264 + MP3 (MP4), apretamos el botón de Next y por último Stream. **A este punto ya se esta transmitiendo el video.**

* **Parte del cliente:** Abrir VLC media player, ir a Convert, opción Red, y en la URL, colocamos udp://1234 y por último en el combobox, elegimos Play. **Ahora se empezará a mostrar el video transmitido en el servidor**




