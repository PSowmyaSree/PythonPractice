#3-Remove non-alphanumeric characters from a string
input_string = input("Enter a string: ")
clean_string=''
for c in input_string:
    if c.isalnum() or c==' ':
        clean_string= clean_string + c
print("Cleaned string:", clean_string)
