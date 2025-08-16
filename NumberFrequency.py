input_num = list(map(int, input("Enter a list of integers separated by space: ").split()))
my_dict = {}

for num in input_num:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1
