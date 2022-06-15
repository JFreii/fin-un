#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fact(x):
    if x == 0:
        return 1
    return fact(x-1) * x
    pass

def filter_even(li):
    return list(filter(lambda x: x%2 == 0, li))
    pass

def square(li):
    return list(map(lambda x: x * x, li))
    pass

def bin_search(li, element):
    low = 0
    high = len(li) - 1

    while low <= high:
        middle = (low + high) // 2
        if li[middle] == element:
            return middle
        elif li[middle] > element:
            high = middle - 1
        else:
            low = middle + 1

    return -1
    pass

def is_palindrome(string):
    reversed_string = ""

    string = string.translate({ord(i): None for i in ".',!? "})
    string = string.lower()
    
    for i in range(len(string), 0, -1):
        if (string[i-1] >= 'a' and string[i-1] <= 'z') or (string[i-1] >= 'а' and string[i-1] <= 'я'):
            reversed_string += string[i - 1]
            
    if string == reversed_string:
        print("YES")
    else:
        print("NO")
    pass

def calculate(path2file):
    file=path2file.readlines()
    string = ''
    oper = ''
    numb_1 = ''
    numb_2 = ''
    answer = ''
    result = ''
    for i in file:
        string +=i
    string=string.replace('\n','    ')
    string=string.split('    ')
    i=0
    while i+2 < len(string):
        oper = string[i]
        numb_1 = string[i+1]
        numb_2 = string[i+2]
        i += 3

        if oper == '+':
            answer += str(int(numb_1) + int(numb_2))+','
        elif oper == '-':
            answer += str(int(numb_1) - int(numb_2))+','
        elif oper == '*':
            answer += str(int(numb_1) * int(numb_2))+','
        elif oper == '**':
            answer += str(int(numb_1) ** int(numb_2))+','
        elif oper == '//':
            answer += str(int(numb_1) // int(numb_2))+','
        elif oper == '%':
            answer += str(int(numb_1)%int(numb_2))+','

    answer = answer.split(',')
    answer.pop(-1)
    answer = ','.join(answer)

    return answer
    pass

def substring_slice(path2file_1,path2file_2):
    f_1 = open(path2file_1)
    f_2 = open(path2file_2)
    file_1 = f_1.readlines()
    file_2 = f_2.readlines()
    string = ''
    numbers = ''
    answer = ''
    result = ''
    for i in file_1:
        string +=i
    string=string.replace('\n','    ')
    string=string.split('    ')
    for i in file_2:
        numbers +=i
    numbers=numbers.replace('\n','    ')
    numbers=numbers.split('    ')

    for i in range(len(string)):
        str = string[i]
        ind = numbers[i].split()
        answer = str[int(ind[0]):(int(ind[1])+1)]
        result += answer+' '

    result = result.strip()
    return result
    pass

