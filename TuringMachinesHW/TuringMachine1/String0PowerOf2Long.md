input: '00000000000000000'
blank: ' '
start state: q1

table:
  q1:
    0: {write: ' ', R: q2}      
    x: {R: qreject} 
    ' ': {R: qreject}
  q2:
    0: {write: x, R: q3} 
    x: {R: q2} 
    ' ': {write: ' ', R: qaccept}
  q3:
    0: {R: q4} 
    x: {R: q3} 
    ' ': {L: q5}
  q4:
    0: {write: x, R: q3}
    x: {R: q4}
    ' ': {R: qreject}
  q5:
    0: {L: q5}
    x: {L: q5}
    ' ': {R: q2}
  qaccept:
  qreject: