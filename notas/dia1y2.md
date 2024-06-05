
# Inteligencias artificiales: IA

Bajo el nombre IA entran muchas cosas.
Cualquier programa/máquina que simula un comportamiento inteligente(humano) entra dentro de la IA.
Máquina que va cogiendo piezas de una cinta y las va colocando en una caja, máquina que juega al ajedrez, coche autónomo, etc.
Y es capaz de discriminar entre cosas que le interesan y cosas que no le interesan (piezas defectuosas, piezas que no son de su color, etc.)
Eso es IA.

Lo que ocurre es que habitualmente, sobre todo hoy en día, cuando hablamos de IA nos referimos a algo más concreto.
En concreto nos referimos a la IA que se basa en el aprendizaje automático (machine learning).

## Aprendizaje automático / machine learning

En ocasiones queremos montar/diseñar programas que son tan complejo, que los seres humanos no sabríamos crearlos.
No podemos analíticamente especificar el comportamiento que queremos simular:
- Reconocer un dígito en una fotografía: un puñado de pixels... Como sea, he de escribir un programa que sea capaz de reconocer un dígito en una fotografía.
- Hacer una traducción de un texto del inglés al español. No sabemos ni por donde comenzar.

En estos escenarios, es cuando aplicamos técnicas de aprendizaje automático / machine learning.

Entra por la puerta una persona (solo sé que tiene entre 5 y 20 años)... y mide 170. Me podéis dar una estimación de su edad?
- Entre 15-20 años.
Mide 110cm. 
- Entre 7-10 años.

OJO: Es una estimación... y como tal, sujeta a error.
Pregunta... ¿cómo has llegado a esa estimación? Habéis usado un procedimiento analítico? No.
La experiencia... LOS DATOS QUE HABEIS IDO ACUMULANDO A LO LARGO DE VUESTRA VIDA.
Habéis visto muchas personas en ese tramo de edad.. y habéis visto la altura que tenían.
En base a esos datos.. hago una estimación.

ESTO ES APRENDIZAJE AUTOMÁTICO.

En ocasiones, cuando tengo un problema que no se resolver analíticamente, lo que hago es recopilar datos (CUANTOS MÁS MEJOR) y en base a esos datos, hago una estimación.

El machine learning consiste en dejar a la computadora que sea ella la que escriba un programa que sea capaz de hacer esa estimación.
La máquina lo que hace es analizar una cantidad ingente de datos y en base a esos datos, escribe un programa que es capaz de hacer esa estimación.

Cuántas lineas de código pensáis que tiene el programa que reconoce un dígito en una fotografía?
Por parte de un desarrollador... sería una locura... no sabemos ni cómo hacer el programa.

En cambio, un desarrollador puede escribir un programa que le pida a la computadora que escriba ese programa en menos de 10 lineas de código.... eso si.. además le tiene que pasar miles de fotografías... etiquetadas con el dígito que aparece en la fotografía.

La computadora buscará los patrones que haya en las fotografías. Identificará lo que tienen en común las fotografías que tienen un 1, un 2, un 3, etc... de forma que cuando le llegue una fotografía nueva, sea capaz de estimar que dígito es.

> Quiero compar un portátil DELL con i7 de 9ª generación, 16GB de RAM, 512GB de disco duro SSD y pantalla de 15 pulgadas ~ 600-1000€

Esa estimación la habéis hecho en base a los datos que habéis ido acumulando a lo largo de vuestra vida.
Si tuvierais en la cabeza los catálogos de precios de todas las tiendas de informática del mundo... podríais hacer una estimación más precisa... para todos los portátiles del mundo. Seguramente sería una estimación más precisa que la que habéis hecho.

A más datos... mejor estimación.

La computadora va a montar ese programa... Y el programa más o menos funcionará bien.. Cuantos más datos le demos, mejor funcionará.
Pero... yo humano... no sé cómo ha hecho la computadora para llegar a esa estimación.
No soy capaz de entender el programa que ha escrito la computadora.
No es que no sea capaz de escribirlo... es que no soy capaz de entenderlo.

Si el programa lo que hace es estimar el precio de un portátil... me da igual cómo lo haya hecho.
Si el programa lo que hace es estimar la probabilidad de que una persona haya cometido un delito... me interesa mucho cómo lo ha hecho.
Imaginad que el programa es racista!
Ha analizado datos de 10000 personas.. y resulta que 9000 eran de una determina etnia... y ha llegado a la conclusión de que las personas de esa etnia tienen más probabilidad de cometer un delito.

Hace años, microsoft lanzo un asistente virtual (montado con machine learning) que era racista... y empezó a hacer comentarios en RRSS que eran racistas.

La calidad de los datos es fundamental para el aprendizaje automático.

Cuando google me muestra un captcha, para ver si soy humano... dándome a elegir entre las fotos que contienen AUTOBUSES... no es para saber si soy humano o no... eso lo averigua por otros conceptos... por ejemplo, por cómo muevo el ratón, el tiempo que tardo en hacer click, etc.
De paso... lo que estoy engordando de gratis es una BBDD de fotografías ETIQUETADAS de autobuses para google... para que así sus programas puedan aprender a reconocer autobuses.

---

Antes os puse el ejemplo de traducir un texto del inglés al español.
No sabemos como hacer eso... Pero le puedo dar a un programa cientos / miles / millones de libros... escritos tanto en inglés como en español. Y decirle a la computadora que lea esos libros y aprenda a traducir.


Texto a Voz: Cómo hago un programa que lea un texto y genere un archivo .mp3 con la voz de un locutor leyendo el texto?
No sabemos crearlo...
Qué hago... Le doy a una computadora miles / millones de textos, y sus correspondientes archivos .mp3... y le digo que lea esos textos y aprenda a generar archivos .mp3 en base a esos datos. Y APLICA REGLAS ESTADÍSTICAS para generar la voz.

Canciones, películas: YOUTUBE
---

Hay muchos tipos de reglas estadísticas que se pueden aplicar / algoritmos que se pueden aplicar.
- Regresión lineal
- Regresión logística
- Árboles de decisión
- Redes neuronales

Cuando nos enfrentamos a un problema de este tipo, le indicamos a la computadora un algoritmo base... y la computadora lo que hace es ajustar los parámetros de ese algoritmo para que las predicciones que hace se ajusten lo máximo posible a los datos que le hemos dado.


Persona: altura / edad

    altura
    ^
    |
    |                                |          R           F
    |                                |  T           O
    |                               L|          I
    |                           K    |      L
    |                           J    |
    |                   M            |
    |                       F        |
  90|       M                        |
    |                                |
    +--------------------------------^------------------------------> Edad
   /        5
  /
 /
PESO


En este caso, eso lo podemos hacer matematicamente... y podemos hacer una regresión lineal...
Aplicamos un procedimiento llamado mínimos cuadrados... y obtenemos una recta que se ajusta a los datos.

Con cosas como esta... nos apañamos = LAS MEDIO ENTIENDO.
Según voy metiendo variables adicionales... ya me explota la cabeza!
Pues ahora meto el género... su municipio en el que vive... el nivel de renta de su familia... 
No se ni donde representar eso.


De entre todos los algoritmos que hay... hay uno que destaca por encima de todos (el que genera mejores programas)... y es el de las redes neuronales.


- Peso       ----------  [Neurona 1]    \                   0     CHICA
              /  /                       \   [Neurona 3] / 
- Edad       /  /   \                    /               \
               /     -   [Neurona 2]    /                   1     CHICO
- Altura      /     /

768 pixels   * 98 neuronas * 10 nuronas  = 75360 pesos

Neurona1 = f(Argumento1, Argumento2, Argumento3) = w1 * Argumento1 + w2 * Argumento2 + w3 * Argumento3 + b
                                                    w= Weight = Peso
                                                    Si ese resultado es > 0 ... la función devuelve 1

Neurona2 = f(Argumento1, Argumento2, Argumento3) = w1' * Argumento1 + w2' * Argumento2 + w3' * Argumento3 + b'
                                                    Si ese resultado es > 0 ... la función devuelve 1

Neurona3 = f(Salida Neurona1, Salida Neurona2)  = w1'' * Salida Neurona1 + w2'' * Salida Neurona2 + b''
                                                    Si ese resultado es > 0 ... la función devuelve 1

Neurona3 = w1'' * (w1 * Argumento1 + w2 * Argumento2 + w3 * Argumento3 + b) + w2'' * (w1' * Argumento1 + w2' * Argumento2 + w3' * Argumento3 + b') + b''

Si ese resultado es > 0 ... la función devuelve 1 = CHICO

Le voy a meter 1000000 de datos... reales... de pesos, edades y alturas... y le voy a decir a la computadora que se invente unos valores de w1, w2, w3, w1', w2', w3', w1'', w2'' y b, b', b'' y que meta los valores de esos pesos en la fórmula de la neurona 3... y que me diga si es chico o chica.

En algunos acertará...por pura chiripa cósmica.. y en otros no acertará.
Calculo el porcentaje de aciertos... y le digo a la computadora que empiece a hacer pequeños cambios en los pesos... para que el porcentaje de aciertos sea mayor.

    w1 = 0.5        w1 = 0.4            w1 = 0.3
    w2 = 0.3                
    w3 = 0.2
    w1' = 0.1
    w2' = 0.2
    w3' = 0.3
    w1'' = 0.4
    w2'' = 0.5
    b = 0.1
    b' = 0.2
    b'' = 0.3

    30% de aciertos 40% de aciertos     20% de aciertos

Y asi miles de millones de veces... hasta que por pura Chiripa cósmica, llegue a una combinación de pesos que me de un 95% de aciertos.

GUAY ! Ese es el programa que ha escrito la computadora:

    Neurona3 = 0.4 * (0.5 * Peso + 0.3 * Altura - 0.2 * Edad + 0.1) + 0.5 * (0.1 * Peso + 0.2 * Altura - 0.3 * Edad + 0.2) - 0.3 > 0 = CHICO
    En caso contrario... CHICA

Al final... hay una ecuación matemática que es capaz de hacer esa estimación.... que más o menos funciona bien.

Pero qué significa esa ecuación? No lo sé... no soy capaz de entenderla.

En un caso como ese... todavía habla de temas que me pueden resonar en la cabeza... edad... peso... altura.

Ahora... si me pasan en lugar de 3 variables: 10000 variables (cada uno de los pixeles de una foto de 100x100).. que tienen un valor de 0-255 si uso escala de grises... si voy con una foto a color... cada pixel tiene a su vez 3 variables: Rojo, Verde, Azul 0-255

Y a lo mejor monto una red neuronal... que en primera capa tiene 20 neuronas... y los resultados los paso a 10 neuronas... y los resultados los paso a 5 neuronas... y los resultados los paso a 1 neurona... que me dice si en la foto hay un gato o no.

Y le pido a la computadora que me invente los valores de los pesos de todas las neuronas... para que me de un 95% de aciertos.

Lo saca... pero npi de cómo lo ha hecho.... ni de lo que significa esa ecuación.

imprimirSaludo(nombre, formal, genero):
    Buenos días Señora Ruiz.


Las Redes sociales usan este tipo de algoritmos para retener a una persona el máximo tiempo posible dentro de la red social.
Le acabo de sacar un video de un gato...
Y sé que es una persona que le gusta cierto tipo de videos... igual que a otras tropecientas personas que ya tenido por aquí.
Y sé que a las personas que siguen unos patrones de videos igual que los que ha visto esta persona... si después del video de gatos, le pongo uno de perros... se va a quedar más tiempo en la red social... en cambio si le pongo uno de política... se va a ir.
Lo tengo claro... le pongo uno de perros.

Y estos programas se vuelven expertos en saber qué es lo que le gusta a una persona... y le van mostrando cosas que le gustan... para que se quede el máximo tiempo posible en la red social.

Esto mismo lo podemos usar para muchos otros fines... algunos muy nobles! Otros no tanto.

Pero nosotros, buena gente, lo vamos a usar para hacer cosas buenas.

---

En el mundo de la IAs hay hoy en día 2 familias de algoritmos que destacan por encima de los demás:
- Predicción / clasificación de datos ---> Para estimas cuándo va a haber un problema con una aplicación/sistema.
  - Observability / Monitoring
- Generación <- CHATGPT, Github Copilot, etc.

---

Machine Learning: Aprendizaje supervisado 
  - Modelos predictivos / clasificatorios
  - Modelo generativo
Data Mining:   Aprendizaje no supervisado


CHAT-GPT = MODELO DE LENGUAJE. Programa que es capaz de generar texto en base a un texto de entrada.

Funciona con una red neuronal... solo que muy grande y con una determinada arquitectura.
En las redes neuronales, al número de capas de neuronas, junto con el número de neuronas en cada capa, se le llama arquitectura de la red. Esta basado en la arquitectura Transformer (todos los algoritmos de traducción de texto de google están basados en esta arquitectura).
En el caso de ChatGPT

---

# Ingeniería del dato

BBDD                        Las tenemos en los entornos de producción... para recoger información y gestionarla 
                            (altas, bajas, modificaciones).
                            No tengo los datos ahí perennes... no tengo los datos históricos.
                            Voy a guardar los datos vivos... los datos que necesito para que la aplicación funcione.
                                    vvvvv
                                     ETL (Extract, Transform, Load)  ... variantes: ETL, TEL, ELT, ETLT
                                    vvvvv
Data lake                   Es otro tipo de BBDD... donde guardo datos en bruto... sin estructura... sin procesar.
                            Los datos que me llegan de las aplicaciones... ficheros... los guardo aquí.
                            No tengo los datos estructurados... no tengo los datos limpios... no tengo los datos procesados

                                Conversación con un cliente... grabo la conversación... AUDIO

                            Los datos, los voy metiendo como en cajones... sin orden... sin estructura... sin limpiar.
                            En ocasiones los guardo por motivos legales... en ocasiones porque me pueden servir en el futuro.
                                A veces quiero empezar a usar esos datos para alguna finalidad... y los preproceso: limpio... les doy estructura... los proceso.
                                      vvvvv
                                       ETL
                                      vvvvvv
Data warehouse              Es otro tipo de BBDD... que tiene datos ordenados y estructurados... y procesados.
                            No es una BBDD de producción... donde voy a hacer operaciones CRUD

                            Aquí los datos están muertos... son datos históricos... Y lo que si hago es ir metiendo más de vez en cuando
Quiero usar los datos:
    Business Intelligence       Cuando hago uso de los datos para fines EVIDENTES... llegar a conclusiones muy directas de los datos.
    Data mining                 Cuando hago uso de los datos para fines NO EVIDENTES... 
                                    llegar a conclusiones que no son tan directas de los datos.
                                    Conclusiones NO DEFINITIVAS... que me pueden llevar a hacer más preguntas... y a hacer más análisis.
    Machine Learning            Se monta un programa con capacidad de predecir si una persona se ha quedado en paro por el cambio
                                    de patrón en el uso de su alarma. Capacidad predictiva del 85%.
        Deep Learning           Cuando esos programas son redes neuronales muy complejas, que requieren de GPUs para su entrenamiento.
Big Data                        Cuando tengo a gestionar (almacenar/transmitir/analizar) un volumen enorme de datos
    Gestión masiva de datos         montamos formas especiales de manejar esos volumenes de datos.
                                    Lo que hacemos es poner a cientos o miles de máquinas de mierda (commotity hardware) a trabajar
                                    juntos... y que se repartan el trabajo.
    Pincho USB 16Gbs vacío... limpito de fabrica... Puedo guardar dentro un fichero que tengo de 5Gbs?
        Depende del sistema de archivos (formato). Formato FAT 16... no entran archivos de más de 2Gbs.
        Y si quiero guardar un archivos de 2 Pb... Lo flipas... no tengo ni sistemas de archivos que soporten eso... ni HDD que soporten eso.

---

Machine Learning: Aprendizaje supervisado 
  - Modelos predictivos / clasificatorios
  - Modelo generativo
Data Mining:   Aprendizaje no supervisado

---
Como administradores de sistemas... no hago carrera en el mundo de la IA... 
Lo que si... que la IA me puede ser una herramienta de gran ayuda en mi trabajo.

Hoy en día... si hay un sitio claro para avanzar en el mundo de la administración de sistemas... pero no son las IAs...
Lo que pasa, es que en ese mundo, las IAs, me vienen de perlas.

El administrador de sistemas, como tal... el de toda la vida... YA NO HACE FALTA EN UNA EMPRESA.

Hace como un año en Linkedin... la gente no hablaba de otra cosa más que de los despidos masivos que había habido en el mundo de las grandes empresas de tecnología: 200.000 personas. Microsoft 7000. Facebook 20000...
Mucha gente en esos momentos le echaba la culpa:
- Final de la pandemia (puede que algo)
- Las IAs... sobre todo porque en esa época apareció una herramienta en el mercado que revolucionó el mundo de las IAs: ChatGPT.

Por qué se despidió a todas esas personas? La mayoría eran administradores de sistemas.
- LAS AUTOMATIZACIONES.
Antes necesitaba a tropetantos sysamins, con un busca metido entre als piernas... a turnos... haciendo guardias... por si un servidor se caía... por si un disco petaba... por si un backup fallaba... reiniciar una app.

Y hoy en día... los entornos de producción los gestiona? KUBERNETES

KUBERNETES es un programa que gestiona el entorno de producción de una empresa. Lo crea GOOGLE... para la gestión de su entorno de producción.

Yo configuro kubernetes. Le digo: Kubernetes quiero de 3 a 7 instancias de esta aplicación... en mi entorno de producción. Con un balanceador de carga (SERVICIO)... con un proxy reverso (INGRESS CONTROLLER)... con reglas de firewall (NETWORKPOLICY)... con auto-escalado (HORIZONTAL POD AUTOSCALER) en base al % de uso de CPU. SNAPSHOTS

También están los clouds... QUE SON AUTO-GESTIONADOS. VENTE aquí que así ya no necesitas un sysadmin.

# DEV--->OPS?

DEVOPS es una cultura, una filosofía... un movimiento... en pro de la automatización.
VAmos a automatizar todo lo que podamos entre el desarrollo y la operación de un sistema.

Devops no es un perfil.. o no lo era.

El primer paso en la adopción de una cultura devops es la INTEGRACION CONTINUA.

Integración continua. Cuando CONTINUAMENTE tengo la ultima versión que han montado los desarrolladores en el entorno de INTEGRACION sometida a pruebas AUTOMATIZADAS.
Entrega Continua: Continuous delivery: Cuando automatizo el siguiente paso DEVOPS.. La distribución de mi producto.. El ponerlo en manos de mis clientes (sean internos o externos)
Despliegue continuo: Continuos deployment: Cuando automatizo el siguiente paso DEVOPS... El despliegue de mi producto en producción.

De forma que quiero que cuando un desarrollador haga click en el botón de enviar su código a un repositorio de un sistema de control de versiones... que una herramienta como JENKINS (AZURE DEVOPS, BAMBOO) se encargue de: 
- Montar un entorno de integración (desde CERO)
- Compilar y empaquetar la app e instalarla en ese entorno
- Ejecutar un montón de pruebas AUTOMATIZADAS sobre la app
- Si va bien, dejar el producto listo para su instalación en un repo de artefactos (WEB, NEXUS, ARTIFACTORY)
- Y preparar un entorno de producción (si es que no lo hay) 
- E instalar en ese entorno de producción la app.
Y en 20 minutos quiero el código nuevo en producción.

Antaño, una app se subía a producción 1 vez al año.

Pero hoy en día, las metodologías ágiles.


# En que consiste una metodología ágil?

La clave está en ir entregando el producto de forma incremental al cliente... cada 2/3/4 semanas quiero una versión nueva en prod.
La única forma de poder acometer esto es AUTOMATIZACION

Y claro... si automatizo... los sysadmins... empiezan a pintar poco.

Quiero automatizar el disponer de 4 servidores, conectados por red, con una ip pública enganchada a un proxy reverso.. y un balanceador de carga por detrás... que apunte a 4 instancias de una app que se va a desplegar en el puerto 80 de esos servidores.
Y lo quiero en 3 minutos... Y que se haga en automático... ADQUISICION DEL HARDWARE INCLUIDA.

Quiero 30 servidores en 45 minutos...
Y dentro de 2 horas, te los devuelvo... ya no los quiero.

Web telepizza:
Entorno producción. Cuantos servidores quiero?
- Depende de la hora del día: A las 12 de la noche? UNO... y a las 10 de la mañana? 1
- Y a las 20:00 madrid/barça de por medio... AGARRATE QUE NOS VAMOS !!!!

ESO ES LO QUE ME DAN LOS CLOUDS

Y quién monta esas automatizaciones?

# Qué significa AUTOMATIZAR?

Es crear una máquina o un programa que cambie el comportamiento de una máquina... para que haga lo que antes hacía un ser humano.
En el mundo IT: MAQUINAS = COMPUTADORAS

Lo que tengo son programas que van a pedir a un cloud infraestructura: TERRAFORM
    Quien está capacitado para contratar y configurar INFRA?
        Desarrollador? No
        Tester? No
        Sysadmin? YES !!!!!
Antes, un sysadmin entraba en una máquina / router.. y configuraba cosas...
- Instalar paquetería
- Crear usuario
- Abrir puertos
HOY EN DIA eso esta automatizado... ANSIBLE, PUPPET, CHEF, SALTSTACK...
    Quien está capacitado para crear programas usando esas herramientas? EL SYSADMIN
Y el entorno de producción lo gestiona el kubernetes... pero quien le dice como? el sysadmin. Escribiendo ficheros de manifiesto en YAML.
= ESCRIBIENDO PROGRAMAS !

Lo que pasa es que al sysadmin le he cambiado el contrato sin que se haya dado cuenta!!!!
NOS HAN CONVERTIDO EN PROGRAMADORES ! Y no hay vuelta atrás!

Sistemas de monitorización más complejos: ELASTICSEARCH... KIALI (dentro de kubernetes)

El trabajo del sysadmin hoy en día YA NO ES ADMINISTRAR SISTEMAS... sino MONTAR PROGRAMAS que administren sistemas.

---

Herramientas tipo Weblogic, Websphere (MIDDLEWARE)- Antiguamente MONTABAMOS SISTEMAS MONOLITICOS = MEGAAPLICACIONES
Hoy en día no solo han cambiado las metodologias de desarrollo de software.. también las arquitecturas de desarrollo=
Montamos las apps de otra forma: LOS MICROSERVICIOS.

--- 
# DEVOPS

Que ya hemos hablado que no es un perfil... sino una cultura que se está imponiendo en todas las empresas..
No podemos obviar que hoy en día se usa también como un perfil!
Un problemita con esto. CADA EMPRESA LLAMA DEVOPS A UNA COSA DIFERENTE.

Hoy en día, el empaquetado / compilación de un software (que antes hacía un desarrollador escribiendo comandos por una consola), hoy en día se automatiza (MAVEN, DOTNET...).. quien configura esas herramientas? Lo hace el desarrollador

Hoy en días, las pruebas se ejecutan automáticamente... es decir, creamos programas que hagan pruebas de otros programas... quién crea esos programas? El desarrollador no tiene npi de testing. LOS TESTERS

Hoy en día, la adquisición/configuración / gestión y operación de infra se automatiza... creamos programas que hacen ese trabajo. Quién los configura esos programas? El sysadmin


PERSIANA!
Y la subo y la bajo con mi cuerdita
Cambio la cuerdita.. y pongo un botón con un motor enganchao!
Acabo de automatizar el proceso de subida y bajada de la persiana. Esto es lo mismo que hacemos con ANSIBLE... PUPPET... MAVEN. TERRAFORM.

Son programas que resuelven una labor que antes se hacía a mano!

Está todo el trabajo de mi persiana automatizado? NO ... necesito a un tío dando al botón...
Pues ahora que tengo ese motor... puedo optar por montar una segunda AUTOMATIZACION...
Quiero montar un programa que a las 9:00 automáticamente dispare el motor de la persiana... y a las 21:00 la baje. SEGUNDA AUTOMATIZACION

En el caso de IT nos pasa igual...
Ahora que tengo todas esas automatizaciones independientes... quiero AUTOMATIZA / ORQUESTAR la llamada a las mismas.

Quiero que:
    - Cuando un desarrollador suba código a git:
    - Crea un contenedor DOCKER
    - Compila en el su software y genera un empaquetado) MAVEN
    - Crea una infra en AWS (terraform)
    - La planchas (paquetería) (ANSIBLE)
    - Le instalas el programa (ANSIBLE)
    - Le ejecutas pruebas (SONARQUBE, JMETER, JUNIT, SELENIUM)
    - Si todo va bien
    - Te creas otra infra en prod.. CON TERRAFORM
    - La planchas (paquetería) (ANSIBLE)
    - Le instalas el programa (ANSIBLE)
    - Le ejecutas pruebas de humo
    - Cambias el balanceador de carga... pa que apunte a lo nuevo
    - Desmantelas la infra vieja (TERRAFORM)

Esto es lo que montamos con unn JENKINS!
Este perfil... el tio que configura un JENKINS que es una herramienta razonablemente nueva... y que tiene que saber de muchas cosas..
es el que no existía antes... y le podemos poner el nombre: DEVOPS

Lo que pasa es que muchas empresas están llamando DEVOPS al administrador de sistemas reconvertido... el que ha aprendido.. de un cloud... de kubernetes... de ansible

---

CLOUD:
- AWS (Amazon Web Services)
- AZURE (Microsoft)
- GoogleCloudPlatform
- IBMCloud (Muy caro.. y se usa menos... pero mucha menos gente sabe del tema)
+ TERRAFORM

HERRAMIENTAS Alternativas a los scripts de la bash o de la powershell de toda la vida:
+ ANSIBLE (Redhat)
- PUPPET
- CHEF

ELK (Elasticsearch, Logstash, Kibana): Observabilidad

CONTENEDORES:
- Kubernetes: Entornos de producción
  - K8S... la distro base de kubernetes
  - OPENSHIFT... la distro de kubernetes de redhat
  - TANZU... la distro de kubernetes de VMWARE
  - KARBON... la distro de kubernetes de NUTANIX
  - RANCHER... la distro de kubernetes de SUSE
- Gestores de contenedores más básicos: Docker, Podman

---

Las IAs son otra forma de AUTOMATIZAR trabajos que antes hacían los humanos.
Tipos de programas que al final montamos a los que llamamos IAs:
- Programas de Data Mining
      PROGRAMAS que ayuda a buscar patrones en datos... NPI de que patrones estoy buscando. 
      Estos se usan algo menos en el mundo de la administración de sistemas.
- Programas de Machine Learning
  - Que ayudan a clasificar     PROGRAMA que asigne tickets de soporte a un departamento u otro
  - Que ayudan a predecir       PROGRAMA que estime cuándo va a haber un problema con una aplicación/sistema
  - Que ayudan a generar        PROGRAMA que genere una respuesta de soporte a un ticket

Como ya os contaba... el desarrollar esos programas (IAS: Modelos(de clasificación, de predicción, generativos)) es un trabajo muy complejo... y que requiere de un perfil muy especializado (Matemático)
Y cuesta mucha pasta (de gasto en electricidad ... si lo queréis asemejar con algo = criptomonedas)

Este ha sido el motivo por el que las IAs no han evolucionado antes...
Las técnicas básicas de trabajo con IAs las conocemos desde hace la tira de años... pero no se han podido aplicar hasta ahora:
- Capacidad de procesamiento
- Cantidad de datos

1.000.000 datos de personas de España..  que les hago una encuesta de las elecciones... y les pregunto a quién van a votar.
Hablando de una población 50M de personas... Estamos hablando de 1/50 de la población.
El problema es cuando empiezo a partir la información para sacar conclusiones de más bajo nivel...
Y yo digo.. como va la cosa en este pueblecito? Y de las 1.000.000 de personas... de ese pueblecito hay 4.
De 4 personas puedo hacer una estadística? 2000 personas

HTTP CODIGO: 40 códigos: 200, 201, 202, 204, 206, 301, 302, 303, 304, 307, 308, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 511
Hora del día... 24 horas al día
Día de la semana... 7 días a la semana
Meses del año... 12 meses al año

40 x 24 x 7 x 12 = 40.000... datos, para sacar estadísticas necesito muchos datos!!!!
400M de datos... puedo empezar a sacar conclusiones valiosas.

---

Lo normal es que los desarrolladores opten por tomar modelos pre-entrenados y los adapten a sus necesidades: REDES NEURONALES.

100 datos de partida... cada dato va a las 100 neuronas (perceptrones) en primera capa

    PRIMERA CAPA    SEGUNDA CAPA        TERCERA CAPA   |     CUARTA CAPA
    O                                                  |     O
    O               O                       O          |     O
    O               O                       O          |     O
    O               O                       O          |     O
    O               O                                  |     O
    O                                                  |     O

    La entre completa... pero luego corto la última capa... y la empaqueto y vendo o la ofrezco gratis.
    Y la gente añade una última capa... y la entrena con sus datos.... y esto es mucho más barato que entrenar una red neuronal desde cero.
    La ultima capa es que le da la salida al modelo... la que se configura para un trabajo concreto.
    Las capas anteriores son las que consiguen que un modelo PIENSE... RAZONE... que APRENDA.

---

Los desarrolladores de software:
- ELASTICSEARCH... Él se encarga de entrenar la última capa en base a los datos que va recopilando de mis servidores, logs, apps...
                            Predicción de problemas
- SERVICE NOW..... Él se encarga de ir entrenando la última capa... 
                            Para que según la gente va dando respuestas a tickets... haya respuestas que se puedan dar automáticamente.
                            Clasificación de tickets

                            Y me presenta datos prerellenos en formularios
                            O incluso cuando tiene un volumen de datos sufificiente, para tomar decisiones en automático por mi.
- DYNA TRACE
- GITHUB STUDIO (Virtual BOT)       Me facilita el que yo provea datos de interés para mi... y me ayuda a entrenar la última capa.
                                    Para darme un programa que responda a mis necesidades:
                                    - Clasificación  \
                                    - Predicción     /   Lo hacen muy bien... si tiene muchos datos... Mucho mejor que un humano.
                                    - Generación     Mejorando... pero todavía no!
                                    Es un asistente para el refinamiento de modelos de machine learning.
- CHATGPT Permite personalizar un poquito los modelos... poquito

    Estos programas parten de un modelo preentrenado y me ayudan a entrenar la última capa... para que el modelo se comporte como yo quiera:
    - Clasificar tickets
    - Predecir problemas
    - Generar respuestas

---

Se asocia cada palabra de un idioma a un concepto.... se aprender su significado.

CASA? El significado de CASA... viene por otros conceptos que relaciono con CASA

    CASA : VIVO?
           COMER?
           DESCANSAR?
           DISFUTAR
           FAMILIA
           PERRO
           PLATANO

    ORANGUTAN: SELVA
               PLATANO


---

CHAT-GPT se basa en probabilidades.
GPT lo que hace es estima la palabra siguiente con más probabilidad de aparecer en base a las palabras anteriores.
