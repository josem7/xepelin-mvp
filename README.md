# xepelin-mvp

## Parte 1 Razonamiento Lógico

Estas preguntas se encuentran dentro de la carpeta razonamiento

### encuentra_y_multiplica
Esta función recibe como entrada una lista y un valor objetivo, esta encuentra 2 números que suemen el target y luego devuvleve su multiplicación. Si no encuentra ningún par esta devuvlve none

### parentesis
Esta función recibe como entrada un string con paréntesis y esta devuvlve true si estos están balanceados y false en otro caso.

## Parte 2 MVP Notificación cambio de tas

### Framework:

Para resolver esta pregunta se utilizó Django. Además se utilizó un template llamado Hyper para darle estilo a la página.

### Deploy:

Para el deploy se utilizó Heroku el link es: http://xepelin-mvp.herokuapp.com/

### Solución:

Esta página posee un log in (pedir las credenciales) simple para poder acceder a ella, para el log in se utilizó el flow de auth que viene por default en Django. Una vez adentro, esta despliega un Google sheet embedded dentro de esta el cuál se pueden modificar las tasas. Utilizando apps script dentro del Google Sheet, se crea una función que detecta cuando se realizó un cambio en la tasa y esta hace un POST request con toda la información a zapier que de forma automática envía un email al correo que está definido en la celda Email.

### Problemas y Mejoras
- El google sheet que está embedded en la página es modificable por todos (dado que se tiene acceso a la página), en un futuro sería mejor que solo las perosnas con acceso a editar este sheet puedan editarlo, se tendría que hacer un flujo de autentificación con Google para esto.
- No estoy seguro si utilizar apps scrit dentro del Google sheet era efectivamente la mejor opción ya que si se tienen muchos Sheets habría que incluir ese código en todos lo que claramente no es ideal. Una posible mejor opción sería utilizar posiblemente la API de Google Sheet.
- Para poder hacer un POST request desde apps script debí hacer un pequeño workaround la función de on edit que venía por default (más info en: https://stackoverflow.com/questions/58359417/you-do-not-have-permission-to-call-urlfetchapp-fetch). Creo que hacer este workaround no es lo ideal, nuevaente utilizando la API de Google Sheets podría ser mejor.