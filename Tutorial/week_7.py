#part 1: HOFs
def maxpower(n,exp):
 def count(m,cnt):
    if m >= exp:
        return cnt
    return count(m*n, 1+cnt)
 return count(1,0)

#print(maxpower(2,1000)) #10

def partial(op):
    def action(a,b):
        print(op(a,b))
    return action

f1 = partial(lambda x,y : x*2 + y*2)
#print(f1(5,10)) #30

f2 = partial(f1) #function created blabla 
#print(f2(5,10))


#part 2: lambda expressions
#can pass args and don't use, but must give all params

#print((lambda a,b,c : a + b)(1,2,3)) #3
#print((lambda a,b,c : a + b + c)(1,2)) #error, need to provide 3 arguments.
#print((lambda a: lambda b: a + b)(1)) #creates the inner lambda function object lambda b: 1 + b 
#print((lambda a: lambda b: a + b)(1,2)) #error, cause i gave 2 arguments to a
#print((lambda a: lambda b: a + b)(1)(2)) #3, cause i gave a a valuse of 1 and b a value of 2
#print((lambda x: x (lambda y: y))(lambda z : z)(1))
#^ z is passed into x. 1 is passed into y. 1 is passed into z. 1==1