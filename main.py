import clips

import vocationService as vc
from view import show_menu 


def main():
    sistemaExperto= clips.Environment()
    sistemaExperto.clear()

    vc.define_rules(sistemaExperto)
    show_menu(sistemaExperto)
    
    vc.finish(sistemaExperto)

if __name__ == "__main__":
    main()