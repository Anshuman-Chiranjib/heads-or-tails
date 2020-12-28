from random import randint
num = input('Number of times to flip coin: ')
num = int(num)
flips = [randint(0,1) for r in range(num)]
results = []
for object in flips:
        if object == 0:
            results.append('Heads')
        elif object == 1:
            results.append('Tails')
print (results)
# IT WILL GIVE THE RESULT ACCORDING TO YOUR NUMBER GIVEN
# SO IF I WRITE 2 AND PRESS ENTER IT WILL FLIP THE COIN TWO TIMES AND IVE TWO RESULTS