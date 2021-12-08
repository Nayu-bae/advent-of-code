f = open('day8/input8', 'r')

outputs = []
inputs = []
for line in f.readlines():
    inputs.append(line.split('|')[0].strip().split(' '))
    outputs.append(line.split('|')[1].strip().split(' '))

def notCommon(arr):
    not_common = []
    for num in arr:
        for letter in num:
            count = 0
            for num2 in arr:
                if letter in num2:
                    count += 1
            if count == 2 and not letter in not_common:
                not_common.append(letter)
    return not_common

def solve(input, output):
    letters = {'a' : '', 'b' : '', 'c' : '', 'd' : '', 'e' : '', 'f' : '', 'g' : ''}
    nums = ['', '', '', '', '', '', '', '', '', '']
    
    for num in input:
        if len(num) == 2:
            nums[1] = num
        elif len(num) == 4:
            nums[4] = num
        elif len(num) == 3:
            nums[7] = num
        elif len(num) == 7:
            nums[8] = num
    #print(nums)


    # find C
    zero_or_nine_or_six = []
    for num in input:
        if len(num) == 6:
            zero_or_nine_or_six.append(num)
    not_common_zero_or_nine_or_six = notCommon(zero_or_nine_or_six)
    #print(not_common_zero_or_nine_or_six)
    for c in nums[1]:
        if c in not_common_zero_or_nine_or_six:
            letters['c'] = c
    #print('Found C: ' + letters['c'])
    
    # find F
    for c in nums[1]:
        if c != letters['c']:
            letters['f'] = c
    #print('Found F: ' + letters['f'])

    # find A
    for c in nums[7]:
        if c != letters['c'] and c != letters['f']:
            letters['a'] = c
    #print('Found A: ' + letters['a'])

    # find E
    five = ''
    two_or_three_or_five = []
    for num in input:
        if len(num) == 5:
            two_or_three_or_five.append(num)
    #print(two_or_three_or_five)
    for num in two_or_three_or_five:
        if letters['c'] not in num:
            five = num
    #print(five)
    for c in nums[8]:
        if (c not in five) and (c != letters['a'] and c != letters['c'] and c != letters['f']):
            letters['e'] = c
    #print('Found E: ' + letters['e'])

    # find G
    for c in five:
        if (c not in nums[4]) and (c != letters['a'] and c != letters['f']):
            letters['g'] = c
    #print('Found G: ' + letters['g'])

    # find D
    for c in notCommon(zero_or_nine_or_six):
        if c != letters['c'] and c != letters['e']:
            letters['d'] = c
    #print('Found G: ' + letters['g'])

    # find b
    for c in five:
        if c not in nums[7] and c != letters['a'] and c != letters['d'] and c != letters['f'] and c != letters['g']:
            letters['b'] = c
    #print('Found B: ' + letters['b'])

    print('Solving line: ' + str(output))    
    print(letters)
    num = ''
    for out in output:
        if letters['a'] in out and  letters['b'] in out and  letters['c'] in out and  letters['e'] in out and  letters['f'] in out and  letters['g'] in out and len(out) == 6:
            num += '0'
        elif letters['c'] in out and letters['f'] in out and len(out) == 2:
            #print('ADDING 1 FROM ' + out)
            num += '1'
        elif letters['a'] in out and letters['c'] in out and letters['d'] in out and letters['e'] in out and letters['g'] in out and len(out) == 5:
            num += '2'
        elif letters['a'] in out and letters['c'] in out and letters['d'] in out and letters['f'] in out and letters['g'] in out and len(out) == 5:
            num += '3'
        elif letters['b'] in out and letters['c'] in out and letters['d'] in out and letters['f'] in out and len(out) == 4:
            num += '4'
        elif letters['a'] in out and letters['b'] in out and letters['d'] in out and letters['f'] in out and letters['g'] in out and len(out) == 5:
            num += '5'
        elif letters['a'] in out and letters['b'] in out and letters['d'] in out and letters['f'] in out and letters['g'] in out and letters['e'] in out and len(out) == 6:
            num += '6'
        elif letters['a'] in out and letters['c'] in out and letters['f'] in out and len(out) == 3:
            num += '7'
        elif letters['a'] in out and letters['b'] in out and letters['c'] in out and letters['d'] in out and letters['e'] in out and letters['f'] in out and letters['g'] in out and len(out) == 7:
            num += '8'
        elif letters['a'] in out and letters['b'] in out and letters['c'] in out and letters['d'] in out and letters['f'] in out and letters['g'] in out and len(out) == 6:
            num += '9'
        #print(num)
    print(num)
    return int(num)



sum = 0
for i in range(len(inputs)):
    sum += solve(inputs[i], outputs[i])

print(sum)