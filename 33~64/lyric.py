oct = [111,114,157,166,145,123,145,143,165,162,151,164,171,126,145,162,171,115,165,143,150]#八进制，对应为二进制-三个位，就是猜不出也得一个一个试，反正是有意义的，然后是八进制
res = 'flag{'
for i in oct:
    res += chr(int(str(i),8))#int函数的用法之一：int(str(i),digit)
res +='}'
print(res)