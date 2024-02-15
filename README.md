# Arithmetic_Formatter
Program to format arithmetic expressions from string format into paper-like solution format. Created for practice

```
Rules for this program:
-> The function takes no more than 5 arguments
-> The function only supports addition ("+") and subtraction ("-")
-> Each operand may only contain digits 
-> Each operand may contain up to four digits 
-> Otherwise, return the respective error

Rules for conversion: 
-> There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom)
-> Numbers should be right-aligned
-> There should be 4 spaces between each problem 
-> There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually


Example usage: 

Function Call:

a_formatter(["32 + 100", "4923 - 7", "11 + 84"])
Output:

   32      4923      11
+ 100    -    7    + 84    
-----    ------    ----    


Function Call:

Second argument indicates whether the answer should be displayed

a_formatter(["32 + 100", "4923 - 7", "11 + 84"], True)

Output:

   32      4923      11
+ 100    -    7    + 84    
-----    ------    ---- 
  132      4916      95

```