grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

PA  : '(' ;
PC  : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;

ASIG  : '=' ;
IGUAL : '==' ;

NUMERO : DIGITO+ ;

INT   : 'int' ;
WHILE : 'while' ;
FOR   : 'for' ;
IF    : 'if' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;


WS : [ \t\n\r] -> skip;
// OTRO : . ;

// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | WHILE  {print("WHILE ->" + $WHILE.text + "<--") }   s
  // | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  // | EOF
  // ;

// si : s EOF ;

// s : PA s PC s
//   |
//   ;




