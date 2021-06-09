# Generated from C:/Users/aleib/Desktop/practica_python_LP/LP_python\Logo3d.g4 by ANTLR 4.9.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .Logo3dParser import Logo3dParser
else:
    from Logo3dParser import Logo3dParser


# This class defines a complete generic visitor for a parse tree produced by Logo3dParser.

class Logo3dVisitor(ParseTreeVisitor):

    def __init__(self):
        self.variables = {}         # como prueba haremos key = varName, value = varValue
        self.sentencies = {}        # key = funcName, value = lista sentencias
        self.parametres = {}        # key = funcName, value = llista parametres
    # Visit a parse tree produced by Logo3dParser#root.
    def visitRoot(self, ctx: Logo3dParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#sentencia.
    def visitSentencia(self, ctx: Logo3dParser.SentenciaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#bloque.
    def visitBloque(self, ctx: Logo3dParser.BloqueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#bucle.
    def visitBucle(self, ctx: Logo3dParser.BucleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#sentencia_simple.
    def visitSentencia_simple(self, ctx: Logo3dParser.Sentencia_simpleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#assignacio.
    def visitAssignacio(self, ctx: Logo3dParser.AssignacioContext):
        value = self.visit(ctx.expresio())
        self.vars[ctx.VARIABLE().getText()] = value

    # Visit a parse tree produced by Logo3dParser#ifcond.
    def visitIfcond(self, ctx: Logo3dParser.IfcondContext):
        condicio = self.visit(ctx.condicio)
        if condicio:
            self.visit(ctx.sentencia)  # pot haver-hi varies sentencies
        else:
            if ctx.getChild(4).getText() == 'ELSE': #TODO esto esta mal, no tiene porque ser el hijo 4
                self.visit(ctx.sentencia)  # visitar les sentencies de despres del ELSE

    # Visit a parse tree produced by Logo3dParser#whileloop.
    def visitWhileloop(self, ctx: Logo3dParser.WhileloopContext):
        condicio = self.visit(ctx.condicio)
        while (condicio):
            self.visit(ctx.sentencia) #TODO puede haber más de una sentencia

    # Visit a parse tree produced by Logo3dParser#forloop.
    def visitForloop(self, ctx: Logo3dParser.ForloopContext):
        iterador = self.visit(ctx.VARIABLE().getText())
        val_entrada = self.visit(ctx.expresio(0))
        val_salida = self.visit(ctx.expresio(1))
        sentencias = [sent for sent in self.visit(ctx.sentencia)]

        for i in range(val_entrada, val_salida):
            self.vars[iterador] = val_entrada
            # Ejecutar sentencias

        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#lectura.
    def visitLectura(self, ctx: Logo3dParser.LecturaContext):
        ids = [id.getText() for id in ctx.VARIABLE()]
        for id in ids:
            self.variables[id] = input()
            print("Lectura realitzada: " + id + " toma el valor " + self.variables[id])

    # Visit a parse tree produced by Logo3dParser#escriptura.
    def visitEscriptura(self, ctx: Logo3dParser.EscripturaContext):
        valors = [self.variables[expresio] for expresio in self.visit(ctx.expresio())]
        print(valors)
        #TODO això es podria millorar

    # Visit a parse tree produced by Logo3dParser#declaraciof.
    def visitDeclaraciof(self, ctx: Logo3dParser.DeclaraciofContext):
        funcio, parametresf = self.visit(ctx.funcio())
        self.parametres[funcio] = parametresf
        temp = list(ctx.getChildren())
        temp2 = []
        for sentencia in temp:
            if sentencia.getText():
                temp2.append(sentencia)
        self.sentencies[funcio] = temp2
        print("Funció declarada")

        if funcio == "main":
            print("Executem funció main")
            for sentencia in self.sentencies[funcio]: # Si la declaració es del main, hi ha que executar la funcio
                self.visit(sentencia)
            print("Funció main executada")

    # Visit a parse tree produced by Logo3dParser#invocaciof.
    def visitInvocaciof(self, ctx: Logo3dParser.InvocaciofContext):
        funcio, parametresf = self.visit(ctx.funcio)
        for arg, val in zip(self.parametres[funcio],parametresf):
            self.vars[arg] = val

        for sentencia in self.sentencies[funcio]:
            self.visit(sentencia)

        if funcio in ["forward", "left", "right", "backward", "up", "down", "color"]:
            # TODO executar les funcions
            pass

    # Visit a parse tree produced by Logo3dParser#funcio.
    def visitFuncio(self, ctx: Logo3dParser.FuncioContext):
        funcName = ctx.getChild(0).getText()
        children = [child for child in ctx.getChildren()]
        parametres = []
        for child in children:
            if child.getText() == "expresio":
                parametres.append(self.visit(child))
        return funcName, parametres

    # Visit a parse tree produced by Logo3dParser#expresio.
    def visitExpresio(self, ctx: Logo3dParser.ExpresioContext):
        children = list(ctx.getChildren())
        result = None

        if children[1].getText() == "+":
            result =  self.visit(ctx.expresio(0)) + self.visit(ctx.expresio(1))
        elif children[1].getText() == "-":
            result = self.visit(ctx.expresio(0)) - self.visit(ctx.expresio(1))
        elif children[1].getText() == "*":
            result = self.visit(ctx.expresio(0)) * self.visit(ctx.expresio(1))
        elif children[1].getText() == "/":
            second = self.visit(ctx.expresio(1))
            if second != 0:
                result = self.visit(ctx.expresio(0)) / self.visit(ctx.expresio(1))
            else:
                print("Divisió entre 0")
        elif children[0].getText() == "-":
            result = - self.visit(ctx.expresio(0))
        elif len(children) == 1:
            result = self.visit(children(0))
        elif children[0].getText() == '(' and children[2].getText() == ')':
            result = self.visit(ctx.expresio())
        else:
            print("Expresió no definida")

        return result

    # Visit a parse tree produced by Logo3dParser#condicio.
    def visitCondicio(self, ctx: Logo3dParser.CondicioContext):
        exp1 = self.visit(ctx.expresio(0))
        exp2 = self.visit(ctx.expresio(1))
        comparador = ctx.OPERADORLOGIC().getText()
        result = None

        if comparador == '>':
            result = exp1 > exp2
        elif comparador == '<':
            result = exp1 < exp2
        elif comparador == '==':
            result = exp1 == exp2
        elif comparador == '!=':
            result = exp1 != exp2
        elif comparador == '>=':
            result = exp1 >= exp2
        elif comparador == '<=':
            result = exp1 <= exp2
        else:
            print("Operador inesperat")
            pass
        return result


del Logo3dParser
