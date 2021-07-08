i = int(input('''Input an odd number
'''))
y = '*'


if (i % 2) == 0:
    print('bruh i said odd number')

else:
    for x in range(1,i//2+2):
        print((x-1)*' '+'*'+(i-x*2)*' '+y)
        if x == i//2:
                y = ''
        
    for x in range(1,i//2+1):
        print((i//2-x)*' '+'*'+(x*2-1)*' '+'*')