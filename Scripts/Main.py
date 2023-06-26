import functions as f
import time as t

def Ask():
    try:
        val = abs(int(input("A donde desea acceder?\n1-Farmacia\n2-Deportes\n3-Cosmeticos\n")))

        match val:
            case 1:
                f.take_turn('D')
            case 2:
                f.take_turn('S')
            case 3:
                f.take_turn('C')
            case _:
                raise Exception


    except:
        print("Por favor ingrese un numero del 1 al 3")
        Ask()


def start():
    while True:
        Ask()


start()
