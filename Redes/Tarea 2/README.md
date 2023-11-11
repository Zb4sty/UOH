Un chat online es un método de comunicación digital vía Internet que realiza intercambio de mensajes de forma instantánea, enviando mensajes de texto entre un emisor a un receptor, generalmente
mediante un servidor. Es quizá la aplicación más conocida de los sockets TCP/IP.
El objetivo de esta tarea es implementar un chat para granjeros de Stardew Fridi a través del cual, además de poder conversar, se puedan intercambiar artefactos coleccionables, 
así como consultar los artefactos que cada granjerx tiene. Este chat debe seguir la arquitectura cliente-servidor


Guía de comandos implementados:

• :q Permite que el usuario se desconecte del chat.<br>
• :p <Identificador> <Mensaje> Envía un mensaje privado al usuario. Este mensaje sólo debe ser recibido por este usuario, y desplegado en su chat.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo, :p nombre_granjero_conectado mensaje  <br>
&nbsp;&nbsp;&nbsp;&nbsp;   :p fulanito Hola, Como estas?         <br> 
• :u Muestra los usuarios que se encuentran conectados actualmente al chat. <br>
• :smile Envía la carita feliz :) a los demás usuarios conectados. <br>
• :angry Envía la carita enojada >:( a los demás usuarios conectados. <br>
• :combito Envía un emoticón bélico Q(’- ’Q) a los demás usuarios conectados. <br>
• :larva Envía una Larva (:o)OOOooo a los demás usuarios conectados. <br>
• :artefactos Entrega una lista de los artefactos que el usuario tiene en su cuenta. Esta información sólo es visible por quien envía el comando. <br>
• :artefacto <ArtefactoId> Obtiene el nombre del artefacto identificado por ArtefactoId. <br>
      Ejemplo, :artefacto 22 es respondido por el servidor con Trocitos de cristal.  <br>
      (Esta información sólo es visible por quien envía el comando.) <br>
• :offer <Identificador> <MiArtefactoId> <SuArtefactoId> Este comando inicia un intercambio con el usuario <Identificador>. A este usuario se le ofrece <MiArtefactoId> a cambio de <SuArtefactoId>.  <br>
      Ejemplo, :offer Gus 32 12 equivale a querer intercambiar una Espuela prehistórica por el Disco raro de Gus. <br>
• :accept Acepta la oferta recibida y realiza el intercambio de artefactos, actualizando las listas de artefactos de cada usuario involucrado. En ambos chats se muestra ¡Intercambio realizado! <br>
• :reject Rechaza la oferta. En ambos chats involucrados se muestra Intercambio rechazado. <br>

El listado de objetos disponibles se encuentra en  artefactos.JSON
