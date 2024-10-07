from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser

class Escucha (compiladoresListener) :
    numTokens = 0
    numNodos  = 0

    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza la compilacion")

    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        print("Se encontraron")
        print("\tNodos:  " + str(self.numNodos)) 
        print("\tTokens: " + str(self.numTokens))

    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Encontre WHILE")
        print("\tCantidad hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText()) 

    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("FIN del WHILE")
        print("\tCantidad hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())

    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print(" ### Declaracion")

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("Nombre variable: " + ctx.getChild(1).getText())

    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
    
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
    