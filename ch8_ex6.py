numList = []
while True:
    n = input('Enter a number: ')
    if n == 'done': break
    #异常处理在float转换时进行，确认是否为数字
    try:
        n = float(n)
    except:
        print('Invalid input.')
        continue
    numList.append(float(n))

print('Maximum: ', max(numList))
print('Minimum: ', min(numList))
