grammar Logo3d;

root            : declaraciof+ EOF;

sentencia       : sentencia_simple
                | bloque;

bloque          : ifcond
                | bucle;

bucle           : whileloop
                | forloop;

sentencia_simple    : lectura
                    | escriptura
                    | assignacio
                    | invocaciof
                    ;

assignacio      : VARIABLE ASSIGNACIO expresio;
ifcond          : IF condicio THEN sentencia+ END
                | IF condicio THEN sentencia+ ELSE sentencia+ END;
whileloop       : WHILE condicio DO sentencia+ END;
forloop         : FOR VARIABLE FROM expresio TO expresio DO sentencia+ END;
lectura         : LECTURA VARIABLE;
escriptura      : ESCRIPTURA expresio;
declaraciof     : PROC VARIABLE PAR1 parametros PAR2 IS sentencia+ END;
invocaciof      : funcio;
//comentari       : COMENTARI TEXT ENL;

parametros      : VARIABLE (COMA VARIABLE)*
                |
                ;
// PARAULES
IF              : 'IF';
THEN            : 'THEN';
ELSE            : 'ELSE';
END             : 'END';
WHILE           : 'WHILE';
DO              : 'DO';
FROM            : 'FROM';
TO              : 'TO';
PROC            : 'PROC';
IS              : 'IS';
FOR             : 'FOR';

// TOKENS
VALOR           :   ENTER
                |   DECIMAL;
ENTER           :   [0-9]+;
DECIMAL         :   ENTER PUNT ENTER;
funcio          :   VARIABLE PAR1 expresio (COMA expresio)* PAR2
                |   VARIABLE PAR1 PAR2;
BOOL            :   'True'
                |   'False';
VARIABLE        :   [a-zA-Z]+ [0-9]*;
TEXT            :   [a-zA-Z0-9]+;


expresio        :   expresio SUMA expresio
                |   expresio RESTA expresio
                |   expresio MULT expresio
                |   expresio DIV expresio
                |   RESTA expresio
                |   BOOL
                |   VARIABLE
                |   PAR1 expresio PAR2
                |   VALOR
                ;


condicio                :   expresio OPERADORLOGIC expresio
                        |   condicio AND condicio
                        |   condicio OR condicio
                        |   VARIABLE
                        ;


OPERADORLOGIC           :   MESGRAN
                        |   MESPETIT
                        |   IGUAL
                        |   DIF
                        |   MESGRANIGUAL
                        |   MESPETITIGUAL
                        ;



// SINES DE PUNTUACIO o SIMBOLS
ASSIGNACIO      : ':=';
LECTURA         : '>>';
ESCRIPTURA      : '<<';
PAR1            : '(';
PAR2            : ')';

SUMA            : '+';
RESTA           : '-';
MULT            : '*';
DIV             : '/';

MESGRAN         : '>';
MESPETIT        : '<';
IGUAL           : '==';
DIF             : '!=';
MESGRANIGUAL    : '>=';
MESPETITIGUAL   : '<=';
AND             : '&&';
OR              : '||';

COMA            : ',';
PUNT            : '.';
LINE_COMMENT    : '//' ~[\r\n]* -> skip ;
WS              : [ \n\r\t]+ -> skip ;


