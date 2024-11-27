"""
PEP 8:
 a) lines should be 79 characters in length or less
 b) continuations of long expressions onto 
 additional lines should indented by four 
 extra spaces from normal identation.

 purpose :working with multi line statement python is a 
 interpreter-based language
 -Each line excutes separatly
 - \ ->line continuation operator
 - will join more than one line to a single statement.

Brace
  ()  paranthesis
  []  quare braces
  {}  flower braces

 PEP 8:
   a) Lines should be 79 characters in length or less
   b) Continuations of long expressions onto additional lines should
      indented by four extra spaces from their normal indentation

"""
sum_of_values = 123+23-123*2/12
print(sum_of_values)

sum_of_values1 = 123+23-123*2/12+123+23- \
    123*2/12+123+23-123*2/12+ \
    123+23-123*2/12+123+23-123*2/12 \
    +123+23-123*2/12

print(sum_of_values1)

sum_of_values2 = (123+23-123*2/12+123+23- 
    123*2/12+123+23-123*2/12+ 
    123+23-123*2/12+123+23-123*2/12 
    +123+23-123*2/12)

print(sum_of_values2)
sum_of_values3 = [123+23-123*2/12+123+23- 
    123*2/12+123+23-123*2/12+ 
    123+23-123*2/12+123+23-123*2/12 
    +123+23-123*2/12]

