my_string = list(map(int, input().split(' ')))


mean = sum(my_string)/len(my_string)
greater = sorted((str(num) for num in my_string if num > mean), key=int)
print(' '.join(greater))