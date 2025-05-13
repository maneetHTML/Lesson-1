print("Welcome to AI chat bot what is your name?")
name=input(":")
print(f"Nice to meet you {name}.")
print("How are you feeling today? (good/bad)")
feel=input(':').lower()
if feel=='good':
    print("I'm glad to hear that!")
elif feel=='bad':
    print("I'm sorry to hear that! Hope thing get better soon.")
else:
    print("I know feeling can be hard to explain.")
# Second question
print("What is your favourite color?")
color=input(':').lower()
print(f"Yo I like that {color} as well!")
print(f"Why is {color} your favourite color?")
whycolor=input(':')
print(f'Yes I see why that is your favourite color.')
print(f"Nice chating with you {name}.Goodbye!")