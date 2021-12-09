num = [7, 2, 5, 2, 2]

for x_count in num:
    print(x_count * 'x')


for x in range(len(num)):
    print(num[x] * 'x')

for x_count in num:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output) 

for i in num:
    print(num)  

for j in num:
    print(j)

for k in num:
    print(k * num) 



numbers = [3,8,5,20,9,10]
max  = numbers[0]
for n in numbers:
    if n > max:
        max = n
        # print(max)            #check how these work
    # print(f'max {max}')   
print(f'MAX : {max}' )   