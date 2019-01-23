
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/leftPOWERSQRTrightUMINUSABS FLOAT ID INT POWER SQRT\n        main : expression\n        \n        var_assign : ID\n        \n        expression : INT\n                   | FLOAT\n                   | SQRT\n                   | var_assign\n        \n        expression : expression '+' expression\n                   | expression '-' expression\n                   | expression '*' expression\n                   | expression '/' expression\n                   | expression POWER expression\n        \n        expression : SQRT expression\n        \n        expression : '-' expression %prec UMINUS\n        \n        expression : '(' expression ')'\n        \n        expression : ABS expression ABS\n        "
    
_lr_action_items = {'INT':([0,5,7,8,9,11,12,13,14,15,],[3,3,3,3,3,3,3,3,3,3,]),'FLOAT':([0,5,7,8,9,11,12,13,14,15,],[4,4,4,4,4,4,4,4,4,4,]),'SQRT':([0,5,7,8,9,11,12,13,14,15,],[5,5,5,5,5,5,5,5,5,5,]),'-':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[7,12,-3,-4,-5,-6,7,7,7,-2,7,7,7,7,7,-12,-13,12,12,-7,-8,-9,-10,-11,-14,-15,]),'(':([0,5,7,8,9,11,12,13,14,15,],[8,8,8,8,8,8,8,8,8,8,]),'ABS':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,],[9,-3,-4,-5,-6,9,9,9,-2,9,9,9,9,9,-12,-13,26,-7,-8,-9,-10,-11,-14,-15,]),'ID':([0,5,7,8,9,11,12,13,14,15,],[10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,3,4,5,6,10,16,17,20,21,22,23,24,25,26,],[0,-1,-3,-4,-5,-6,-2,-12,-13,-7,-8,-9,-10,-11,-14,-15,]),'+':([2,3,4,5,6,10,16,17,18,19,20,21,22,23,24,25,26,],[11,-3,-4,-5,-6,-2,-12,-13,11,11,-7,-8,-9,-10,-11,-14,-15,]),'*':([2,3,4,5,6,10,16,17,18,19,20,21,22,23,24,25,26,],[13,-3,-4,-5,-6,-2,-12,-13,13,13,13,13,-9,-10,-11,-14,-15,]),'/':([2,3,4,5,6,10,16,17,18,19,20,21,22,23,24,25,26,],[14,-3,-4,-5,-6,-2,-12,-13,14,14,14,14,-9,-10,-11,-14,-15,]),'POWER':([2,3,4,5,6,10,16,17,18,19,20,21,22,23,24,25,26,],[15,-3,-4,-5,-6,-2,-12,-13,15,15,15,15,15,15,-11,-14,-15,]),')':([3,4,5,6,10,16,17,18,20,21,22,23,24,25,26,],[-3,-4,-5,-6,-2,-12,-13,25,-7,-8,-9,-10,-11,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'expression':([0,5,7,8,9,11,12,13,14,15,],[2,16,17,18,19,20,21,22,23,24,]),'var_assign':([0,5,7,8,9,11,12,13,14,15,],[6,6,6,6,6,6,6,6,6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> expression','main',1,'p_main','math_parser.py',66),
  ('var_assign -> ID','var_assign',1,'p_var_assign','math_parser.py',73),
  ('expression -> INT','expression',1,'p_expression','math_parser.py',82),
  ('expression -> FLOAT','expression',1,'p_expression','math_parser.py',83),
  ('expression -> SQRT','expression',1,'p_expression','math_parser.py',84),
  ('expression -> var_assign','expression',1,'p_expression','math_parser.py',85),
  ('expression -> expression + expression','expression',3,'p_expression_binop','math_parser.py',91),
  ('expression -> expression - expression','expression',3,'p_expression_binop','math_parser.py',92),
  ('expression -> expression * expression','expression',3,'p_expression_binop','math_parser.py',93),
  ('expression -> expression / expression','expression',3,'p_expression_binop','math_parser.py',94),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','math_parser.py',95),
  ('expression -> SQRT expression','expression',2,'p_expression_sqrt','math_parser.py',115),
  ('expression -> - expression','expression',2,'p_expression_uminus','math_parser.py',122),
  ('expression -> ( expression )','expression',3,'p_expression_group','math_parser.py',129),
  ('expression -> ABS expression ABS','expression',3,'p_expression_abs','math_parser.py',136),
]