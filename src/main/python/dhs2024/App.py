import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha

def main(argv):
    # archivo = "input/entrada.txt"
    # archivo = "input/parentesis.txt"
    # archivo = "input/programa.txt"
    archivo = "input/opal.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa()
    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)