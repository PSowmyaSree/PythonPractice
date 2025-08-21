
password=input("Enter Password \n")
special_characters = "!@#$%^&*()_+=-`~[]{}|;':\",./<>?" + " "
if any(c.isalnum() for c in password) and any(c.islower() for c in password) and any(c.isupper() for c in password) and len(password)>=8 and any(c in special_characters for c in password):
    print("Valid Password")
else:
    print("Invalid Password")