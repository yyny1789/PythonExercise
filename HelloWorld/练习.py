age = 20
name = "lilei"
print("{0} was {1} years old when he wrote this book".format(name, age))

print("{} was {} years old when he wrote this book".format(name, age))

# 对于浮点型 0.333 保留小数点 . 后三位
print('{0:.3f}'.format(1.0/3))

# 使用 (^) 定义 '___hello___'字符串长度为 11 ?? 不懂
print('{0:_^11}'.format('hello'))

# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name = 'lili', book = 'Python'))

print('a', end='')
print('b')

i = 5
print('value is', i)

print(5 > 3)

# number = 23
# guess = int(input('Enter an integer: '))

# if guess == number:
#     print('Congratulations, you guessed it.')
#     print('(but you do not win any prizes!)')
# elif guess < number:
#      print('No, it is a little higher than that')
# else:
#     print('No, it is a little lower than that')

# print('Done')

number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
# 在这里你可以做你想做的任何事
print('Done')
         