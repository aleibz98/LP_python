# Generated from /Users/alejandro/LP/LP_python/Logo3d.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Logo3dParser import Logo3dParser
else:
    from Logo3dParser import Logo3dParser

# This class defines a complete generic visitor for a parse tree produced by Logo3dParser.

class Logo3dVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Logo3dParser#root.
    def visitRoot(self, ctx:Logo3dParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#instruccio.
    def visitInstruccio(self, ctx:Logo3dParser.InstruccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#assignacio.
    def visitAssignacio(self, ctx:Logo3dParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#ifcond.
    def visitIfcond(self, ctx:Logo3dParser.IfcondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#whileloop.
    def visitWhileloop(self, ctx:Logo3dParser.WhileloopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#forloop.
    def visitForloop(self, ctx:Logo3dParser.ForloopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#lectura.
    def visitLectura(self, ctx:Logo3dParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#escriptura.
    def visitEscriptura(self, ctx:Logo3dParser.EscripturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#declaraciof.
    def visitDeclaraciof(self, ctx:Logo3dParser.DeclaraciofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#invocaciof.
    def visitInvocaciof(self, ctx:Logo3dParser.InvocaciofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Logo3dParser#comentari.
    def visitComentari(self, ctx:Logo3dParser.ComentariContext):
        return self.visitChildren(ctx)



del Logo3dParser