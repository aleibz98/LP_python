grammar Logo3d_v2;

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
                    | comentari
                    ;

assignacio      : VARIABLE ASSIGNACIO expresio;
ifcond          : IF CONDICIO THEN sentencia+ END
                | IF CONDICIO THEN sentencia+ ELSE sentencia+ END;
whileloop       : WHILE CONDICIO DO sentencia+ END;
forloop         : FOR VARIABLE FROM VALOR TO VALOR DO sentencia+ END;
lectura         : (LECTURA VARIABLE)+ ENDL;
escriptura      : (ESCRIPTURA VARIABLE)+ ENDL;
declaraciof     : PROC FUNCIO IS sentencia+ END;
invocaciof      : FUNCIO;
comentari       : COMENTARI TEXT ENDL;

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
FUNCIO          :   [a-zA-Z0-9\u0080-\u00FF]+ PAR1 VARIABLE [COMA VARIABLE]* PAR2;
VARIABLE        :   [a-zA-Z0-9\u0080-\u00FF]+;
TEXT            :   [a-zA-Z0-9\u0080-\u00FF]*;
VALOR           :   [0-9]+;

expresio        :   expresio SUMA expresio
                |   expresio RESTA expresio
                |   expresio MULT expresio
                |   expresio DIV expresio
                |   RESTA expresio
                |   VARIABLE
                |   PAR1 expresio PAR2
                |   VALOR
                ;


CONDICIO                :   VALOR OPERADORLOGIC VALOR
                        |   VALOR OPERADORLOGIC VARIABLE
                        |   VARIABLE OPERADORLOGIC VALOR
                        |   VARIABLE OPERADORLOGIC VARIABLE
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

COMENTARI       : '//';
COMA            : ', ';
ENDL            : '\n' -> skip;
WS              : ' ' -> skip;

