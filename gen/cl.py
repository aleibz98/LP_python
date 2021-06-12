import sys
from antlr4 import *
from Logo3dLexer import Logo3dLexer
from Logo3dParser import Logo3dParser
from Logo3dVisitor import Logo3dVisitor
from antlr4.InputStream import InputStream


if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
    print(len(sys.argv))
    if len(sys.argv) > 2:
        start_func = sys.argv[2]
    else:
        start_func = "main"

else:
    input_stream = InputStream(input('? '))
    start_func = "main"

lexer = Logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = Logo3dParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
visitor = Logo3dVisitor(start_func)
visitor.visit(tree)
