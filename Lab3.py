def balanced(s):
    stack = [] #Creation of the stack
    if len(s)<=1: #This is the base size case
        return False
    
    for i in s:
        if (i=="}" or i=="]" or i==")") and len(stack)==0: #There cant be a right bracket with empty stack
            return False
        if i =="[" or i=="{" or i =="(": #Adds left brackets to the stack
            stack.append(i)
        elif i=="]" and stack[-1] =="[": #IF there is a pair encounters stack gets popped
            stack.pop()
        elif i=="}" and stack[-1] =="{":
            stack.pop()
        elif i==")" and stack[-1] =="(":
            stack.pop()            
        else:
            return False
    print(len(stack)==0)#returns of the stack is empty

balanced(str(input("Enter a set of boundaries ")))
