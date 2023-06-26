def _turn():
    x = 0
    while True:
        x += 1
        yield x

_drugstore = _turn()
_sports = _turn()
_cosmetics = _turn()

def take_turn(type):

    def set_text(turn):
        print("\n" + "*" * 24 + f"\nSu turno es:\n{turn}\nAguarde y sea paciente\n" + "*" * 24 + "\n")

    match type:
        case 'D':
            set_text(f"D-{next(_drugstore)}")
        case 'S':
            set_text(f"S-{next(_sports)}")
        case 'C':
            set_text(f"C-{next(_cosmetics)}")
