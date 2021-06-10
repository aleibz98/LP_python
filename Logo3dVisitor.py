# Generated from C:/Users/aleib/Desktop/practica_python_LP/LP_python\Logo3d.g4 by ANTLR 4.9.1
from antlr4 import *
from turtle3d import Turtle3D

if __name__ is not None and "." in __name__:
    from .Logo3dParser import Logo3dParser
else:
    from Logo3dParser import Logo3dParser


# This class defines a complete generic visitor for a parse tree produced by Logo3dParser.

class Logo3dVisitor(ParseTreeVisitor):

    def __init__(self):
        self.variables = {}  # como prueba haremos key = varName, value = varValue
        self.sentencies = {}  # key = funcName, value = lista sentencias
        self.parametres = {"forward": ["distanceF"],
                           "backward": ["distanceB"],
                           "left": ["angleL"],
                           "rigth": ["angleR"],
                           "up": ["angleU"],
                           "down": ["angleD"],
                           "color": ["a", "b", "c"],
                           "hide":  [],
                           "show":  [],
                           "home":  [],
                           "radio": ["r"]}
        self.defaults = ["forward", "backward", "up", "down", "left", "right", "color", "hide", "show", "home", "radio" ]
        self.current_ctx = {}
        self.turtle = Turtle3D()

        # key = funcName, value = llista parametres
        # TODO inicializar parametres[forward], pararametres[left]...

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
        self.current_ctx[ctx.VARIABLE().getText()] = value

    # Visit a parse tree produced by Logo3dParser#ifcond.
    def visitIfcond(self, ctx: Logo3dParser.IfcondContext):
        condicio = self.visit(ctx.condicio())
        children = list(ctx.getChildren())
        i = 3
        sent1 = []
        sent2 = []
        while children[i].getText() != "ELSE" and children[i].getText() != "END":
            sent1.append(children[i])
            i += 1
        if children[i].getText() != "END":
            while children[i].getText() != "END":
                sent2.append(children[i])
                i += 1

        if condicio:
            print("executem if-then")
            for sent in sent1:
                self.visit(sent)
        elif len(sent2) > 0:
            print("executem else")
            for sent in sent2:
                self.visit(sent)
        else:
            print("Liada")
            pass

    # Visit a parse tree produced by Logo3dParser#whileloop.
    def visitWhileloop(self, ctx: Logo3dParser.WhileloopContext):
        condicio = self.visit(ctx.condicio())
        children = list(ctx.getChildren())

        while (condicio):
            i = 3
            while children[i].getText() != "END":
                self.visit(children[i])
                i += 1
            condicio = self.visit(ctx.condicio())

    # Visit a parse tree produced by Logo3dParser#forloop.
    def visitForloop(self, ctx: Logo3dParser.ForloopContext):
        itName = ctx.VARIABLE().getText()
        initVal = self.visit(ctx.expresio(0))
        endVal = self.visit(ctx.expresio(1))

        children = list(ctx.getChildren())

        for var in range(int(initVal), int(endVal)):
            i = 7
            self.current_ctx[itName] = var
            while children[i].getText() != "END":
                self.visit(children[i])
                i += 1


    # Visit a parse tree produced by Logo3dParser#lectura.
    def visitLectura(self, ctx: Logo3dParser.LecturaContext):
        id = ctx.VARIABLE().getText()
        self.current_ctx[id] = input("Introduir valor per " + id + ":")
        print("Lectura realitzada: " + id + " toma el valor " + self.current_ctx[id])

    # Visit a parse tree produced by Logo3dParser#escriptura.
    def visitEscriptura(self, ctx: Logo3dParser.EscripturaContext):
        node = ctx.getChild(1).getText()
        print(node)
        valor = self.visit(ctx.expresio())
        self.current_ctx[node] = valor
        print("print( " + node + " ) = " + str(valor))

    # Visit a parse tree produced by Logo3dParser#declaraciof.
    def visitDeclaraciof(self, ctx: Logo3dParser.DeclaraciofContext):
        funcio = ctx.VARIABLE().getText()
        parametresf = self.visit(ctx.parametros())
        print(parametresf)
        self.parametres[funcio] = parametresf
        children = list(ctx.getChildren())
        print([child.getText() for child in children])
        sentencies_tmp = []
        i = 6
        while children[i].getText() != "END":
            sentencies_tmp.append(children[i])
            i += 1
        self.sentencies[funcio] = sentencies_tmp
        print("Funció declarada :" + funcio)

        if funcio == "main":
            print("Executem funció main")
            self.current_ctx = {}
            for sentencia in self.sentencies[funcio]:  # Si la declaració es del main, hi ha que executar la funcio
                print(sentencia.getText())
                self.visit(sentencia)
            print("Funció main executada")

    # Visit a parse tree produced by Logo3dParser#invocaciof.
    def visitInvocaciof(self, ctx: Logo3dParser.InvocaciofContext):
        funcio, parametresf = self.visit(ctx.funcio())
        print("Executem la funció " + funcio)
        print((self.parametres[funcio]))
        print(parametresf)
        new_context = {}
        for arg, val in zip(self.parametres[funcio], parametresf):
            new_context[arg] = val

        new_context, self.current_ctx = self.current_ctx, new_context

        if funcio in self.defaults:
            if funcio == "forward":
                self.turtle.forward(self.current_ctx["distanceF"])
            elif funcio == "backward":
                self.turtle.forward(self.current_ctx["distanceB"])
            elif funcio == "left":
                self.turtle.left(self.current_ctx["angleL"])
            elif funcio == "right":
                self.turtle.right(self.current_ctx["angleR"])
            elif funcio == "up":
                self.turtle.up(self.current_ctx["angleU"])
            elif funcio == "down":
                self.turtle.down(self.current_ctx["angleD"])
            elif funcio == "home":
                self.turtle.home()
            elif funcio == "show":
                self.turtle.show()
            elif funcio == "hide":
                self.turtle.hide()
            elif funcio == "color":
                self.turtle.color(self.current_ctx["a"], self.current_ctx["b"],self.current_ctx["c"])
            elif funcio == "radio":
                self.turtle.radio(self.current_ctx["r"])
        else:
            #new_context, self.current_ctx = self.current_ctx, new_context
            for sentencia in self.sentencies[funcio]:
                print(sentencia.getText())
                self.visit(sentencia)
            print("funcio " + funcio + " executada")

        new_context, self.current_ctx = self.current_ctx, new_context

    # Visit a parse tree produced by Logo3dParser#funcio.
    def visitFuncio(self, ctx: Logo3dParser.FuncioContext):
        funcName = ctx.VARIABLE().getText()
        children = list(ctx.getChildren())
        parametres_tmp = []
        i = 2
        while children[i].getText() != ')':
            if children[i].getText() != ',':
                parametres_tmp.append(self.visit(children[i]))
            i += 1
        return funcName, parametres_tmp

    # Visit a parse tree produced by Logo3dParser#expresio.
    def visitExpresio(self, ctx: Logo3dParser.ExpresioContext):
        children = list(ctx.getChildren())
        count = ctx.getChildCount()
        result = None

        if count == 1:
            if Logo3dParser.symbolicNames[children[0].getSymbol().type] == "VARIABLE":
                result = float(self.current_ctx[ctx.getText()])
            elif Logo3dParser.symbolicNames[children[0].getSymbol().type] == "VALOR":
                result = float(ctx.getText())
        elif children[1].getText() == "+":
            result = self.visit(ctx.expresio(0)) + self.visit(ctx.expresio(1))
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
        # TODO las comparaciones fallan
        # TODO podria añadir comparacion && || entre condiciones
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

    def visitParametros(self, ctx: Logo3dParser.ParametrosContext):
        children = list(ctx.getChildren())
        result = []
        for child in children:
            if Logo3dParser.symbolicNames[child.getSymbol().type] == "VARIABLE":
                result.append(child.getText())
        return result
