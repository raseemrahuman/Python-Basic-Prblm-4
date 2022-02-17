#A.Answer
Var = input("ENTER SOMETHING TO FIND ")
digit = 0
letter = 0

for ch in Var:
   if ch.isdigit():
      digit=digit+1
   elif ch.isalpha():
      letter=letter+1
   else:
      pass
print("LETTERS:", letter)
print("DIGITS:", digit)
