
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADDSUBleftMULDIVADD BEC DIV DO ELSE END EQ GEQ GRTR ID IF LEQ LESS LPAR MUL NEQ NUM READ RPAR SEM SUB THEN WHILE WRITEProgram : StatementsStatements : StatementStatements : Statements SEM StatementStatement : If\n                 | While\n                 | AssignmentIf : IF Comparison THEN Statements ENDWhile : WHILE Comparison DO Statements ENDAssignment : Id BEC ExpressionComparison : Expression Relation ExpressionRelation : EQ\n                | NEQ\n                | LESS\n                | LEQ\n                | GRTR\n                | GEQExpression : Expression ADD Expression\n                  | Expression SUB Expression\n                  | Expression MUL Expression\n                  | Expression DIV ExpressionExpression : LPAR Expression RPARExpression : NUMExpression : IdId : IDIf : IF Comparison THEN Statements ELSE Statements ENDRead : READ IdWrite : WRITE Expression'
    
_lr_action_items = {'IF':([0,11,20,33,44,],[7,7,7,7,7,]),'WHILE':([0,11,20,33,44,],[8,8,8,8,8,]),'ID':([0,7,8,11,14,18,20,21,22,23,24,25,26,27,28,29,30,31,33,44,],[10,10,10,10,10,10,10,10,10,10,10,10,-11,-12,-13,-14,-15,-16,10,10,]),'$end':([1,2,3,4,5,6,10,15,16,19,34,37,38,39,40,41,43,45,47,],[0,-1,-2,-4,-5,-6,-24,-22,-23,-3,-9,-17,-18,-19,-20,-21,-7,-8,-25,]),'SEM':([2,3,4,5,6,10,15,16,19,34,35,37,38,39,40,41,42,43,45,46,47,],[11,-2,-4,-5,-6,-24,-22,-23,-3,-9,11,-17,-18,-19,-20,-21,11,-7,-8,11,-25,]),'END':([3,4,5,6,10,15,16,19,34,35,37,38,39,40,41,42,43,45,46,47,],[-2,-4,-5,-6,-24,-22,-23,-3,-9,43,-17,-18,-19,-20,-21,45,-7,-8,47,-25,]),'ELSE':([3,4,5,6,10,15,16,19,34,35,37,38,39,40,41,43,45,47,],[-2,-4,-5,-6,-24,-22,-23,-3,-9,44,-17,-18,-19,-20,-21,-7,-8,-25,]),'LPAR':([7,8,14,18,21,22,23,24,25,26,27,28,29,30,31,],[14,14,14,14,14,14,14,14,14,-11,-12,-13,-14,-15,-16,]),'NUM':([7,8,14,18,21,22,23,24,25,26,27,28,29,30,31,],[15,15,15,15,15,15,15,15,15,-11,-12,-13,-14,-15,-16,]),'BEC':([9,10,],[18,-24,]),'ADD':([10,13,15,16,32,34,36,37,38,39,40,41,],[-24,22,-22,-23,22,22,22,-17,-18,-19,-20,-21,]),'SUB':([10,13,15,16,32,34,36,37,38,39,40,41,],[-24,23,-22,-23,23,23,23,-17,-18,-19,-20,-21,]),'MUL':([10,13,15,16,32,34,36,37,38,39,40,41,],[-24,24,-22,-23,24,24,24,24,24,-19,-20,-21,]),'DIV':([10,13,15,16,32,34,36,37,38,39,40,41,],[-24,25,-22,-23,25,25,25,25,25,-19,-20,-21,]),'EQ':([10,13,15,16,37,38,39,40,41,],[-24,26,-22,-23,-17,-18,-19,-20,-21,]),'NEQ':([10,13,15,16,37,38,39,40,41,],[-24,27,-22,-23,-17,-18,-19,-20,-21,]),'LESS':([10,13,15,16,37,38,39,40,41,],[-24,28,-22,-23,-17,-18,-19,-20,-21,]),'LEQ':([10,13,15,16,37,38,39,40,41,],[-24,29,-22,-23,-17,-18,-19,-20,-21,]),'GRTR':([10,13,15,16,37,38,39,40,41,],[-24,30,-22,-23,-17,-18,-19,-20,-21,]),'GEQ':([10,13,15,16,37,38,39,40,41,],[-24,31,-22,-23,-17,-18,-19,-20,-21,]),'RPAR':([10,15,16,32,37,38,39,40,41,],[-24,-22,-23,41,-17,-18,-19,-20,-21,]),'THEN':([10,12,15,16,36,37,38,39,40,41,],[-24,20,-22,-23,-10,-17,-18,-19,-20,-21,]),'DO':([10,15,16,17,36,37,38,39,40,41,],[-24,-22,-23,33,-10,-17,-18,-19,-20,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Statements':([0,20,33,44,],[2,35,42,46,]),'Statement':([0,11,20,33,44,],[3,19,3,3,3,]),'If':([0,11,20,33,44,],[4,4,4,4,4,]),'While':([0,11,20,33,44,],[5,5,5,5,5,]),'Assignment':([0,11,20,33,44,],[6,6,6,6,6,]),'Id':([0,7,8,11,14,18,20,21,22,23,24,25,33,44,],[9,16,16,9,16,16,9,16,16,16,16,16,9,9,]),'Comparison':([7,8,],[12,17,]),'Expression':([7,8,14,18,21,22,23,24,25,],[13,13,32,34,36,37,38,39,40,]),'Relation':([13,],[21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Statements','Program',1,'p_program','ply-parser.py',291),
  ('Statements -> Statement','Statements',1,'p_statements_statement','ply-parser.py',295),
  ('Statements -> Statements SEM Statement','Statements',3,'p_statements_statements','ply-parser.py',299),
  ('Statement -> If','Statement',1,'p_statement','ply-parser.py',305),
  ('Statement -> While','Statement',1,'p_statement','ply-parser.py',306),
  ('Statement -> Assignment','Statement',1,'p_statement','ply-parser.py',307),
  ('If -> IF Comparison THEN Statements END','If',5,'p_if','ply-parser.py',311),
  ('While -> WHILE Comparison DO Statements END','While',5,'p_while','ply-parser.py',315),
  ('Assignment -> Id BEC Expression','Assignment',3,'p_assignment','ply-parser.py',319),
  ('Comparison -> Expression Relation Expression','Comparison',3,'p_comparison','ply-parser.py',323),
  ('Relation -> EQ','Relation',1,'p_relation','ply-parser.py',327),
  ('Relation -> NEQ','Relation',1,'p_relation','ply-parser.py',328),
  ('Relation -> LESS','Relation',1,'p_relation','ply-parser.py',329),
  ('Relation -> LEQ','Relation',1,'p_relation','ply-parser.py',330),
  ('Relation -> GRTR','Relation',1,'p_relation','ply-parser.py',331),
  ('Relation -> GEQ','Relation',1,'p_relation','ply-parser.py',332),
  ('Expression -> Expression ADD Expression','Expression',3,'p_expression_binary','ply-parser.py',336),
  ('Expression -> Expression SUB Expression','Expression',3,'p_expression_binary','ply-parser.py',337),
  ('Expression -> Expression MUL Expression','Expression',3,'p_expression_binary','ply-parser.py',338),
  ('Expression -> Expression DIV Expression','Expression',3,'p_expression_binary','ply-parser.py',339),
  ('Expression -> LPAR Expression RPAR','Expression',3,'p_expression_parenthesis','ply-parser.py',343),
  ('Expression -> NUM','Expression',1,'p_expression_num','ply-parser.py',347),
  ('Expression -> Id','Expression',1,'p_expression_id','ply-parser.py',351),
  ('Id -> ID','Id',1,'p_id','ply-parser.py',355),
  ('If -> IF Comparison THEN Statements ELSE Statements END','If',7,'p_if_else','ply-parser.py',363),
  ('Read -> READ Id','Read',2,'p_read','ply-parser.py',367),
  ('Write -> WRITE Expression','Write',2,'p_write','ply-parser.py',371),
]
