GAN
Generative Adversarial Networks

Redes de generación ENEMIGAS

Una cosa es dar fotos y averiguar el dígito
Y otra es generar fotos nuevas
Quien dice fotos.. dices sonidos, textos, videos...

Vamos a montar 2 redes neuronales que compitan entre si.
Una red, se va a inventar fotos.
Otra red, va a intentar adivinar si la foto es inventada o real

--- 
Vamos a plantear la arquitectura de la red que intenta adivinar si una foto es real o false

Cuántos datos va a recibir esa red? 784... pixels de la foto
Cuántos datos va a producir? 1... si es real o no

RED DISCRIMINADORA
784 entradas -> 1024 -> 512 -> 256 -> 1 salida
                RELU    RELU   RELU   SIGMOID             (SI o NO)

--- 
red que inventa fotos
100 números aleatorios --> entradas ----> 784 salidas
100 entradas -> 256  -> 512 -> 1024 -> 784 salidas
                RELU    RELU   RELU   TANH                -1 a 1 (progresivos) -> 0 - 255