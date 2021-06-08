# Generated from C:/Users/aleib/Desktop/practica_python_LP/LP_python\Logo3d.g4 by ANTLR 4.9.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .Logo3dParser import Logo3dParser
else:
    from Logo3dParser import Logo3dParser


# This class defines a complete generic visitor for a parse tree produced by Logo3dParser.

class Logo3dVisitor(ParseTreeVisitor):

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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#ifcond.
    def visitIfcond(self, ctx: Logo3dParser.IfcondContext):
        condicio = self.visit(ctx.condicio())
        if condicio:
            self.visit(ctx.sentencia())  # pot haver-hi varies sentencies
        else:
            if ctx.getChild(4).getText() == 'ELSE':
                self.visit(ctx.sentencia())  # visitar les sentencies de despres del ELSE
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#whileloop.
    def visitWhileloop(self, ctx: Logo3dParser.WhileloopContext):
        condicio = self.visit(ctx.condicio())
        while (condicio):
            self.visit(ctx.sentencia())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#forloop.
    def visitForloop(self, ctx: Logo3dParser.ForloopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#lectura.
    def visitLectura(self, ctx: Logo3dParser.LecturaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#escriptura.
    def visitEscriptura(self, ctx: Logo3dParser.EscripturaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#declaraciof.
    def visitDeclaraciof(self, ctx: Logo3dParser.DeclaraciofContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#invocaciof.
    def visitInvocaciof(self, ctx: Logo3dParser.InvocaciofContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#comentari.
    def visitComentari(self, ctx: Logo3dParser.ComentariContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#funcio.
    def visitFuncio(self, ctx: Logo3dParser.FuncioContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Logo3dParser#expresio.
    def visitExpresio(self, ctx: Logo3dParser.ExpresioContext):
        return self.visitChildren(ctx)

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
            pass  # operador inesperado
        return self.visitChildren(ctx)


del Logo3dParser
