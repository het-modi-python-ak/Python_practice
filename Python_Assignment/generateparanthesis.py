# 2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#     Constraints:

#         - 1 <= n <= 8

#     Example 1:

#         - Input: n = 3

#         - Output: ["((()))","(()())","(())()","()(())","()()()"]

#         - Example 2:

#     Example 2:

#         - Input: n = 1

#         - Output: ["()"] 


str=""
tmp=""
res=[]
def genrate(n,op,tmp,res):
    
    if len(tmp) == 2*n:
        print(tmp)
        res.append(tmp)
        tmp=""
        return 

    if op < n:
        tmp+='('
        print(tmp)
        op+=1
        genrate(n,op,tmp,res)
    
    if len(tmp)-op < op:
        tmp+=')'
        print(tmp)
        genrate(n,op,tmp,res)
    

n=3
genrate(n,0,tmp,res)

print(res)

