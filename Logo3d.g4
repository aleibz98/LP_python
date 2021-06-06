grammar Logo3d;

root            : instruccio+ EOF;

instruccio      : assignacio
                | ifcond
                | whileloop
                | forloop
                | lectura
                | escriptura
                | declaraciof
                | invocaciof
                | comentari
                ;

assignacio      : VARIABLE ASSIGNACIO operacio ENDL;
ifcond          : IF CONDICIO THEN instruccio+ END
                | IF CONDICIO THEN instruccio+ ELSE instruccio+ END;
whileloop       : WHILE CONDICIO DO instruccio+ END;
forloop         : FOR VARIABLE FROM VALOR TO VALOR DO instruccio+ END;
lectura         : (LECTURA VARIABLE)+ ENDL;
escriptura      : (ESCRIPTURA VARIABLE)+ ENDL;
declaraciof     : PROC FUNCIO IS instruccio+ END;
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
operacio        :   VALOR OPERADORARITMETIC operacio
                |   VALOR
                ;
OPERADORARITMETIC       :   MULT
                        |   DIV
                        |   SUMA
                        |   RESTA
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

