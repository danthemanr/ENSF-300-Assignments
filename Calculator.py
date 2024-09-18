#Calculator.py
#Daniel Rey, ENSF 300, F24
#A simple calculator program

prompt = "Enter a mathematical expression with three integers and two operators. Brackets are not allowed. Type q to quit.\n"
operators = ['+', '-', '*', '/'] #I might want to add some more

def mathfunct(n1, n2, op):
    #print("mathfunct: ", n1, op, n2)
    if op == 0:
        return n1 + n2
    if op == 1:
        return n1 - n2
    if op == 2:
        return n1 * n2
    if op == 3:
        return int(n1 / n2)

def main():
    usr_str = input(prompt)#formatting needed?
    character = '-' #for error message
    while usr_str != "q":
        
        
        #print(usr_str)

        numstr_list = ["", "", ""]
        op_list = [4, 4] #may need to be longer for brackets
        current = 0
        for x in usr_str:
            #print(x)
            if x == ' ':
                continue
            elif '0' <= x and x <= '9':
                numstr_list[current] += x
                print("a number in string format: ", numstr_list[current])
            elif usr_str[0] == '-' and usr_str[1] == '-':
                usr_str = "q"
                break
            elif x in operators:
                if x == '-' and (numstr_list[current] == ""): #If a number is negative
                    numstr_list[current] += x
                    print("should be a dash: ", numstr_list[current])
                else:
                    op_list[current] = operators.index(x)
                    #print(op_list[current])
                    current += 1
            else:
                usr_str = "q"
                character = x
        if usr_str == "q":
            print('invalid format detected at character', character, 'program terminated')
            break
        
        num_list = [0, 0, 0]
        count = 0
        for s in numstr_list:
            print("findnum: ", s)
            dec = 1
            for i in range(len(s)): #I could have used the int function
                if s[-1-i] == '-':
                    num_list[count] *= -1
                else:
                    num_list[count] += (ord(s[-1-i]) - 48) * dec
                    dec *= 10
            print("a number from num_list: ", num_list[count])
            count += 1
        
        answer = 42 #default answer for testing
        
        if (op_list[1] == '*' or op_list[1] == '/') and (op_list[0] == '+' or op_list[0] == '-'):
            #complex function
            temp = mathfunct(num_list[1], num_list[2], op_list[1])
            answer = mathfunct(num_list[0], temp, op_list[0])
        else:
            #simple function
            temp = mathfunct(num_list[0], num_list[1], op_list[0])
            answer = mathfunct(temp, num_list[2], op_list[1])
        print("first operation =", temp)

        print(usr_str, '=', answer)
        usr_str = input(prompt)
    return 0

if __name__ == '__main__':
    main()