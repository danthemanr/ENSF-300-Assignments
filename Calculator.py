#Calculator.py
#Daniel Rey, ENSF 300, F24
#A simple calculator program

prompt = "Enter a mathematical expression with three integers and two operators. Brackets are not allowed. Type q to quit.\n"
operators = ['+', '-', '*', '/'] #I might want to add some more

def myAdd(x,y):
    return x+y
def mySub(x,y):
    return x-y
def myMul(x,y):
    return x*y
def myDiv(x,y):
    return x//y

def readnum(string):
    numstr_list = ["", "", ""]
    current = 0
    er_char = '' #for error message
    er_pos = 0
    for x in string:
        #print(x)
        if x == ' ':
            continue
        elif '0' <= x and x <= '9':
            numstr_list[current] += x
            #print("a number in string format: ", numstr_list[current])
        elif x in operators:
            if x == '-' and (numstr_list[current] == "" or numstr_list[current][-1] == '-'): #If a number is negative
                numstr_list[current] += x
                #print("should be a dash: ", numstr_list[current])
            elif numstr_list[current] == "": #if the first charcter is an operator or the previos character was one
                string = "e"
                er_char = x
                break
            else:
                current += 1
        else:
            string = "e"
            er_char = x
            break
        er_pos += 1

    num_list = [0, 0, 0, 0]
    if string == "e": #will this properly send an error message?
        print(f'invalid format detected at character \'{er_char}\' in position {er_pos}. Try again.')
        num_list = [0, 0, 0, 1]
    
    count = 0
    #the loop that make the integers into integers
    for s in numstr_list:
        #print("findnum: ", s)
        dec = 1
        length = 0
        for ch in s:
            length += 1
        for i in range(length): #FIXME am I allowed to use len or range or int? The TAs say I am... probably not allowed to use len
            if s[-1-i] == '-':
                num_list[count] *= -1
            else:
                num_list[count] += int(s[-1-i]) * dec
                dec *= 10
        #print("a number from num_list: ", num_list[count])
        count += 1
    return num_list

def readop(string):
    op_list = [-1, -1, -1]
    current = 0
    er_char = '' #for error message
    er_pos = 0
    y = False
    for x in string:
        #print(x)
        if x == ' ' or '0' <= x and x <= '9':
            y = True #this was part of an integer
            continue
        elif x in operators:
            if x == '-' and not y: #If the dash is not imediately after an integer
                continue #then it can't be an operator
            else:
                op_list[current] = x
                #print(op_list[current])
                current += 1
                y = False
        elif op_list[2] != -1: #if there are too many operators
            string = "e"
            er_char = x
            break
        er_pos += 1
    if string == "e":
        print(f'invalid format detected at character \'{er_char}\' in position {er_pos}. Try again.')
        op_list = [-1, -1, -1]
    return op_list

def evaluate(num_list, op_list):
    if (op_list[1] == '*' or op_list[1] == '/') and (op_list[0] == '+' or op_list[0] == '-'):
        if op_list[1] == '*':
            if op_list[0] == '+':
                answer = myAdd(num_list[0], myMul(num_list[1], num_list[2]))
            else:
                answer = mySub(num_list[0], myMul(num_list[1], num_list[2]))
        else:
            if op_list[0] == '+':
                answer = myAdd(num_list[0], myDiv(num_list[1], num_list[2]))
            else:
                answer = mySub(num_list[0], myDiv(num_list[1], num_list[2]))
    else:
        if op_list[0] == '+':
            if op_list[1] == '+':
                answer = myAdd(myAdd(num_list[0], num_list[1]), num_list[2])
            else:
                answer = mySub(myAdd(num_list[0], num_list[1]), num_list[2])
        elif op_list[0] == '-':
            if op_list[1] == '+':
                answer = myAdd(mySub(num_list[0], num_list[1]), num_list[2])
            else:
                answer = mySub(mySub(num_list[0], num_list[1]), num_list[2])
        elif (op_list[0] == '*' or op_list[0] == '/') and (op_list[1] == '+' or op_list[1] == '-'):
            if op_list[0] == '*':
                if op_list[1] == '+':
                    answer = myAdd(myMul(num_list[0], num_list[1]), num_list[2])
                else:
                    answer = mySub(myMul(num_list[0], num_list[1]), num_list[2])
            else:
                if op_list[1] == '+':
                    answer = myAdd(myDiv(num_list[0], num_list[1]), num_list[2])
                else:
                    answer = mySub(myDiv(num_list[0], num_list[1]), num_list[2])
        else:
            if op_list[0] == '*':
                if op_list[1] == '*':
                    answer = myMul(myMul(num_list[0], num_list[1]), num_list[2])
                else:
                    answer = myDiv(myMul(num_list[0], num_list[1]), num_list[2])
            elif op_list[0] == '/':
                if op_list[1] == '*':
                    answer = myMul(myDiv(num_list[0], num_list[1]), num_list[2])
                else:
                    answer = myDiv(myDiv(num_list[0], num_list[1]), num_list[2])
    return answer

def display(num_list, op_list, answer):
    print(num_list[0], op_list[0], num_list[1], op_list[1], num_list[2], "=", answer)

def main():
    usr_str = input(prompt)
    while usr_str != "q":
        num_list = readnum(usr_str)
        if num_list[-1] != 0:
            usr_str = input(prompt)
            continue

        op_list = readop(usr_str)
        if op_list[0] == -1:
            usr_str = input(prompt)
            continue
        
        answer = evaluate(num_list, op_list)

        display(num_list, op_list, answer)

        usr_str = input(prompt)
    return 0

if __name__ == '__main__':
    main()