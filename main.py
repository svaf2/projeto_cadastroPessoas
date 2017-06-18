from controle import Controle
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
    	print("Uso do programa e':\n{} <arquivoDados>".format(sys.argv[0]))
    	sys.exit(0)
    
    controle = Controle(sys.argv[1])
    controle.menu()
