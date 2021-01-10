def validation (op1,symb,op2,l1,l2):
  #Validation
  if symb not in ('+','-'): 
    return "Error: Operator must be '+' or '-'."
  if not (op1.isnumeric() and  op2.isnumeric()):
    return "Error: Numbers must only contain digits."
  if (l1 > 4) or (l2 > 4) :
    return "Error: Numbers cannot be more than four digits."

def calculate(op1,symb,op2):
  if symb == '+':
    sol = int(op1) + int(op2)
    return str(sol)
  else :
    sol = int(op1) - int(op2)
    return str(sol)
  




def arithmetic_arranger(problems,operation=False):
    solutions=[]
    if len(problems)>5:
      return "Error: Too many problems."
    #Validations
    for prob in problems:
          op1,symb,op2 = prob.split(" ")
          l1=len(op1)
          l2=len(op2)
          #Call validation
          value = validation(op1,symb,op2,l1,l2)
          #if value returned validaiton is false return error
          if value: return value
          #After validation calcualting solutions
          if operation :
              sol = calculate(op1,symb,op2)
              solutions.append(sol)

    sol_pointer=0
    list_len = len(problems)
    sentence=""
    last = 3
    if operation : last+=1

    for i in range(0,last):
        count =1
        for x in problems:
          prob = x.split(" ")
          l1=len(prob[0])
          l2=len(prob[2])
          diff = abs(l1 - l2)
          if l1 > l2:
            if i == 0:
                sentence+=''.ljust(2)+prob[i]
                if count < list_len:
                    sentence+=''.ljust(4)
                else :sentence+='\n'
            elif i == 1:
                sentence += prob[i]+''.ljust(diff+1)+prob[i+1]
                if count < list_len:
                    sentence+=''.ljust(4)
                else :sentence+='\n'
            elif i== 2:
                sentence += '-'*(l1+2)
                if count < list_len:
                    sentence+=''.ljust(4)
                else :sentence+='\n'
            else:
              diff = l1 - len(solutions[sol_pointer])+2
              sentence += ''.ljust(diff)+solutions[sol_pointer]
              sol_pointer+=1
              if count < list_len:
                  sentence +=''.ljust(4)
              else: sentence+='\n'

          elif l1 < l2:
            if i == 0:
                sentence+=''.ljust(2)+''.ljust(diff)+prob[i]
                if count < list_len:
                    sentence+=''.ljust(4)
                else :sentence+='\n'
            elif i == 1:
                sentence += prob[i]+''.ljust(1)+prob[i+1]
                if count < list_len:
                    sentence+=''.ljust(4)
                else :sentence+='\n'
            elif i == 2:
                sentence += '-'*(l2+2)
                if count < list_len:
                    sentence+=''.ljust(4)
                else :sentence+='\n'
            else:
              diff = l2 - len(solutions[sol_pointer])+2
              sentence += ''.ljust(diff)+solutions[sol_pointer]
              sol_pointer+=1
              if count < list_len:
                  sentence +=''.ljust(4)
              else: sentence+='\n'

          else :
             if i == 0:
                 sentence+=''.ljust(2)+prob[i]
                 if count < list_len:
                     sentence+=''.ljust(4)
                 else :sentence+='\n'
             elif i == 1:
                 sentence += prob[i]+''.ljust(1)+prob[i+1]
                 if count < list_len:
                     sentence+=''.ljust(4)
                 else :sentence+='\n'
             elif i == 2:
                 sentence += '-'*(l1+2)
                 if count < list_len:
                     sentence+=''.ljust(4)
                 else :sentence+='\n'
             else:
              diff = l1 - len(solutions[sol_pointer])+2
              sentence += ''.ljust(diff)+solutions[sol_pointer]
              sol_pointer+=1
              if count < list_len:
                  sentence +=''.ljust(4)
              else: sentence+='\n'
          count+=1
          
      
    return sentence.rstrip()        