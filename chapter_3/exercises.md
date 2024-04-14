# 3.2
- When a recursive function is called and each recursive call is added too the 
stack, there is a potential for more memory to be allocated than is availible, 
this is known as a 'stack overflow'.
- Stack overflows can occur when no base case is included in a recursive 
funciton, causing maximum recursive depth to be reached and for the call stack
to overflow as no limit to recursive calls was set with a condition.