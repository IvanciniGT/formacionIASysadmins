Contenedores/Contenedorización/Docker/Podman        ESTA SI !!!!

Kubernetes/Openshift/Tamzu                          ESTA NO !!! 

# Contenedores

Los contenedores hoy en día son la forma estandar de distribuir / instalar software.
Todas las empresas SIN EXCEPCION distribuyen su software mediante imágenes de contenedor.

Los contenedores son una alternativa a las Máquinas virtuales.
La realidad es que se han impuesto ya a las VM en la mayor parte de escenarios.
    VMWare (apuesta por los contenedores ENORME)
    
    
# Instalar software

## Instalación más tradicional: A HIERRO
    
        App1  +  App2  +  App3          Problemas:
    ------------------------------          - Configuraciones / Dependencias incompatibles entre apps
           Sistema Operativo                - Seguridad
    ------------------------------          - Si App1 tiene un bug (CPU 100%) -> App1 OFFLINE
                HIERRO                              App2 y App 3 van detrás

## Instalación basada en VM
    
      App1    |    App2  +  App3        Venía con sus propios problemas GORDOS:
    ------------------------------          - Una configuración MUCHO más compleja
      SO1     |         SO2                 - Merma de recursos
    ------------------------------          - Menor rendimiento en las apps
      VM1     |         VM2
    ------------------------------     
    Hipervisor: VMWare, VirtualBox
    HyperV, KVM, Citrix
    ------------------------------     
           Sistema Operativo           
    ------------------------------     
                HIERRO                 

## Instalación basada en Contenedores
   
      App1    |    App2  +  App3  
    ------------------------------
      C1      |         C2
    ------------------------------     
    Gestor de Contenedores:
    Docker, Podman, CRIO, CONTAINERD    (Aquí no entraban: Kubernetes, Openshift)
    ------------------------------     
       Sistema Operativo LINUX           
    ------------------------------     
                HIERRO      
                
    Un contenedor es un ENTORNO AISLADO dentro de un KERNEL LINUX, donde ejecuto procesos.
    AISLADO:
        - Propia configuración de red... y su propia IP
        - Su propio FS (Sistema de archivos)
        - Sus propias VARIABLES DE ENTORNO
        - Puede tener limitaciones de acceso al HIERRO (CPU, RAM...)
                
    Me ofrecen las mismas (casi) ventajas que las VM... pero sin sus inconvenientes.
    Los contenedores los creamos desde IMAGENES DE CONTENEDOR.
    Pero el formato de las imágenes de contenedor está ESTANDARIZADO (HAY UN ESTANDAR)
    Open Container Initiative: Estos son los que han generado un estandar acerca del formato de las 
    IMAGENES de contenedor
        Una imagen es un triste fichero comprimido: TAR
        
    Imaginad que quiero instalar MongoDB en mi computadora Windows:
    1. Requerimientos HW / SF 
    2. Me hago con el INSTALADOR
    3. Ejecuto el instalador (Puede ser complejo)
        ---> C:\Archivos de Programa\Mongo -> zip -> email = NO FUNCIONARIA
    
    Pues en el mundo de los contenedores SI FUNCIONARIA
    Cuando trabajo con contenedores NO INSTALO SOFTWARE... LO DESPLIEGO, ya que dentro de una imagend e contenedor 
    me viene un programa YA INSTALADO de antemano por alguien. HABITUALMENTE el fabricante...
    que sabe instalar su producto 100 veces mejor que yo.
    
    Las imagenes de contenedor las encuentro en registros de repositorios de imagenes de contenedor:
    - Docker hub
    - Quay.io:  Redhat
    - Microsoft container registry: El de microsoft
                
LINUX? Linux es un Kernel de SO...
    De hecho el Kernel de SO más usado del mundo con diferencia sobre cualquier otro!
    Android, 
    GNU/Linux es un SO, que se distribuye en compendios: DISTROS:
        - Redhat: Fedora, Centos, RHEL, Amazon Linux, Oracle Linux
        - Debian: Ubuntu (xUbuntu)...
        - Suse
        - ...

Desde Windows 10... y antes en los servers, Windows puede levantar un kernel LINUX en paralelo con el Kernel NT.
De hecho es una característica del propio Windows.
    CARACTERISTICAS DE WINDOWS > SUBSISTEMA LINUX PARA WINDOWS - WLS

Windows 10 o windows server 2019 son SO... y tienen kernel? SI, claro.. TODO SO, tiene un Kernel
Microsoft a lko largo de su historia ha usado 2 KERNELS para montar todos sus so:
- DOS
    MSDOS
    Windows 2
    Windows 3
    Windows 95, 98, Millenium
- NT (New Technology de Microsoft)
    Windows NT
    Windows XP
    Windows Server
    Windoes 7, 8, 10 y 11

## ElasticSearch 

Es un INDEXADOR... Me permite montar algo asi como mi propio GOOGLE.
Kibana es una interfaz WEB que permite hacer consultas sobre los datos que tengo indexados en un cluster de ES.

Para que se usan realmente en la industria?
En la industria ElasticSearch + Kibana + Logstash se utilizan conjutamente (Stack ELK)
para montar soluciones de observability.


    Servidores WEB
    
        Servidor 1
            Métricas: CPU, RAM, HDD, IO/RED
            Apache
                Métricas: Conexiones abiertas, en proceso, 
                          en cola, tiempo de permamencia de una conexión en cola...
                > access.log
            ElasticAgent    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|
                Es el programa que se encarga de recopilar                      |
                información: METRICAS, logs....                                 |
                                                                                |
        Servidor 2                                                              |
            Métricas: CPU, RAM, HDD, IO/RED                                     |
            Apache                                                              |
                Métricas: Conexiones abiertas, en proceso, en cola,             |
                          tiempo de permamencia de una conexión en cola...      |
                > access.log                                                    |    KAFKA 1
            ElasticAgent    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|>>> KAFKA 2 >>>> Logstash1 >>> Logstash2 >>> ES1 Monitoring    <<< KIBANA
                Es el programa que se encarga de recopilar                      |    KAFKA 3                                  ES2
                información: METRICAS, logs....                                 |                                             ES3
                                                                                |                                             ...
        Servidor N                                                              |
            Métricas: CPU, RAM, HDD, IO/RED                                     |
            Apache                                                              |                           >>> Logstash3 >>> ES20 Negocio      <<< KIBANA
                Métricas: Conexiones abiertas, en proceso, en cola, tiempo      |                                             ES21
                          de permamencia de una conexión en cola...             |                                             ES22
                > access.log                                                    |                                             ...
            ElasticAgent    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|
                Es el programa que se encarga de recopilar                      
                información: METRICAS, logs....                                 



KAFKA es un sistema de mensajería (APACHE)
    Sería equivalente aun RabbitMQ

ES NO ES UNA BBDD... es un indexador.

Las BBDD guardan datos...
Los indexadores guardan INDICES DE LOS DATOS... para poder hacer búsquedas más rápido sobre ellos.
ES, igual que google, guardan una copia del documento que se manda indexar... pero...
En el mundo de la monitorización ocurre una cosa muy especial:
LOS DOCUMENTOS DE MONITORIZACION (EVENTOS) no cambian en el futuro... Son datos muertos.
Si el dato no cambia, entonces: LA COPIA que hizo ES del dato cuando lo indexo refleja el VALOR REAL... ya que no puede cambiar a futuro.
Y en ese sentido, esa copia me sirve como dato real..
Y ES Se convierte sin querer no solo en un idenxador.. sino también en una BBDD (un repositorio de eventos)

---

Imaginad que recopilo información de los logs
- Fecha de un evento
  - Dia del mes
  - Dia de la semana
  - Dia del año
  - Si es fin de semana
  - La hora
  - El minuto
  - El segundo
  - Mes
  - Año
- Código de respuesta HTTP: 200, 400, 500 (indisponibilidad de servicio: SOFTWARE/HARDWARE)
- Bytes
- Cliente:
    - SO: Windows y qué windows | MacOS y qué MACOS
    - Navegador: Chrome, Edge, Firefox
- IP Cliente:
    - IP
    - Pais
    - Continente
    - Zona horaria
    - Provincia
    - Comunidad (Estado)
    - Pueblo
- URL

COMO SÉ que un dato que me viene (una combinación de esos valores) es una ANOMALIA! 
Y entonces es cuando dejo a la computadora que aprenda de los datos:
    Programa de DATA MINING (entrenamiento NO SUPERVISADO). Qué busco? NPI Anomalías... qué es una anomalía? NPI
    Le dejo al propio Kibana que analice todo mi historial de datos... para detectar PATRONES DE COMPORTAMIENTO HABITUALES
    en este caso... en mi sitio WEB

Y el propio Kibana, monta un programa para detectar esos PATRONES DE COMPORTAMENTO particulares de mi sitio WEB.

Y una vez detectados esos patrones, le pedimos a ES que monte un segundo programa: MACHINE LEARNING (entrenamiento SUPEVISADO)
que cuando lleguen nuevos datos, me digas si esos datos encajan con alguno de esos patrones o no, es decir: SI SON ANOMALIAS !