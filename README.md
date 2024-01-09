# rpi-relay
<h2>Controlar un relé con una RaspberryPi mediante interface web.</h2>

Tan solo es necesario un sencillo script en Python (server.py) que controla un pin GPIO de la RaspberryPi.

Aquí se puede ver un esquema con la nomenclatura de los pines GPIO de una RaspberryPi:<br>

<img src="https://github.com/asinformatico/rpi-relay/blob/main/res/Rpi4-gpio.jpeg" alt="Pines GPIO de la RaspberryPi."><br>

El esquema de conexión es bien sencillo. Se conecta un pin de salida GPIO  (aquí he usado el 23) al pin de activación de un relé. En el ejemplo he usado un sencillo diodo led que se enciende o apaga según se actua con dicha salida digital. El polo positivo se conecta al pin 23,este va a una resistencia limitadora de corriente y de ahí al led (cable amarillo). El polo negativo se conecta a la masa (GND, cable negro).
Cuando se presione el botón ON  de la interface web, el led (o relé) se encenderá. Cuandose presione el botón OFF, el led se apagará.
Detalle de las conexiones:<br>

<img src="https://github.com/asinformatico/rpi-relay/blob/main/res/esquema-rpi.png" alt="Conexión del led a la rpi."><br>

Detalle de la interface web:<br>

<img src="https://github.com/asinformatico/rpi-relay/blob/main/res/interfce-web.png" alt="Interface web"><br>

Funcionamiento del servidor web:<br>
<p>Se levanta un sencillo server incluido en los módulos de Python. En el ejemplo se utiliza el puerto 8001 (puede ser cualquier otro que no esté ya en uso). Para acceder de forma local tan solo hay que acceder a la dirección localhost:8001 desde el navegador o si se accede desde otro equipo, sustituir localhost por la dirección IP de la RaspberryPi en la red, por ejemplo 192.168.0.17:8001</p><br>
<p>Para el acceso remoto, es necesario abrir el puerto en la configuracion del Firewall del dispostivo si se está utilizando alguno. Este repositorio es tan solo co fines didácticos y no se recomienda su uso en un entorno de producción ya que carece de ningún tipo de seguridad.
