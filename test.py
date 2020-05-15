import re

def sign_resolver(operand_list):
    lite_operand_list = list()
    count_minus = 0
    count_plus = 0
    for pos, item in enumerate(operand_list):
        if re.match('[0-9]',item) or re.match('-[0-9]',item):
            lite_operand_list.append(item)
        else:
            for element in operand_list[pos,len(operand_list)]:
                if element == '-':
                  count_minus=count_minus+1
                elif element == '+':
                    count_plus=count_minus+1
            if count_minus % 2 == 0:
                continue
            else:
                operand_list.append('-')
            if count_plus > 0:
                operand_list.append('+')
    print(operand_list)
while True:
    inp = input()
    if inp == "/exit":
        print("Bye!")
        exit()
    elif inp == "/help":
        print("The program calculates the sum of numbers")
    else:
        num = input().split()
        if len(num) == 0:
            continue
        else:
            print(sum(num))