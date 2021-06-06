import sys
from antlr4 import *
from Logo3dLexer import Logo3dLexer
from Logo3dParser import Logo3dParser
from Logo3dVisitor import Logo3dVisitor
from antlr4.InputStream import InputStream
import networkx as nx
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1], encoding="utf-8")
else:
    input_stream = InputStream(input('? '))

lexer = Logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Logo3dParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
visitor = Logo3dVisitor()
visitor.visit(tree)

#nx.draw(visitor)