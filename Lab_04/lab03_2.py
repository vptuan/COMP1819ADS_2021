#Creating list of brackets that can be entered
openBrackets = ["(", "[", "{"] 
closeBrackets = [")", "]", "}"] 

#Here is the function that can be called and passed a string of brackets to be checked
def Balanced(enteredString): 
    stackList = []

    #This will loop the string that is entered by the user
    for i in enteredString:
        
        #If the first character of the enteredString is in open brackets list then it will add it to the stack
        if i in openBrackets: 
            stackList.append(i)
            
        #If the character is in the closed bracket list then it will check if the stack is greater than 0 and pop() the stack
        elif i in closeBrackets: 
            indexPosition = closeBrackets.index(i) 
            if ((len(stackList) > 0) and (openBrackets[indexPosition] == stackList[len(stackList)-1])): 
                stackList.pop()
                
            #If the stack is len(0) then it will tell the user that it is not balanced
            else: 
                return "Unbalanced"

    #Once out of the loop it will then check the length, if it is 0 the entry is balanced - If not then it is unbalanced
    if len(stackList) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
#This is where the user will enter the combination of brackets and will be validated
entry = input("Please enter input: ")
print(Balanced(entry)) 
