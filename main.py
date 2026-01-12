import base as bs
import cambiarFases as cf
from bdCoches import cribado

elec = int(input("---- BIENVENIDO ----" +"\n" + "QUE OPCION QUIERES ELEGIR? 1. crear base de datos, 2. MONTADO, 3. PINTADO, 4.ACABADO "))

while elec != 0:
    match elec:
        case 1: 
          bs.base()
          cribado.insertar_coches()
          elec = int(input("QUE OTRA OPCION?"))
        case 2:
          cf.insertarMontaje()
          elec = int(input("QUE OTRA OPCION?"))
        case 3:
          cf.insertarPintado()
          elec = int(input("QUE OTRA OPCION?"))
        case 4:
          cf.insertarAcabado()
          elec = int(input("QUE OTRA OPCION?"))
            


