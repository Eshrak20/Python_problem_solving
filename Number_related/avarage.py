Number = int(input('Enter the number of numbers: '))

sum = 0
for i in range(0, Number):
    sum = sum + int(input())
print(sum / Number)
