#2-Reverse words in a string
input_string=input("Enter a string: ")
words = input_string.split()
reverse_word=words[-1::-1]
print("Reversed words:", " ".join(reverse_word))
