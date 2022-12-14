; =========================================
; ## Macropad test script ##
; test keys are mapped correctly to F13-F24
; and knob sends PgUp and PgDn
; ==========================================
#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

; keys
F13::
MsgBox, f13
return 
F14::
MsgBox, f14
return 
F15::
MsgBox, f15
return 
F16::
MsgBox, f16
return 
F17::
MsgBox, f17
return 
F18::
MsgBox, f18
return 
F19::
MsgBox, f19
return 
F20::
MsgBox, f20
return 
F21::
MsgBox, f21
return 
F22::
MsgBox, f22
return 
F23::
MsgBox, f23
return 
F24::
MsgBox, F24
return 

; knob
PgUp::
MsgBox, PgUp
return
PgDn::
MsgBox, PgDn
return
