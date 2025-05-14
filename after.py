print("Welcome to AI chat bot what is your name?")
name=input(":")
color_list = {
    "red": "Red represents passion, love, and energy, but it can also signal danger, urgency, or aggression, making it a powerful and emotionally intense color.",
    "blue": "Blue conveys calmness and trust, often associated with stability, professionalism, and intelligence, making it a popular choice in corporate and tech branding.",
    "green": "Green symbolizes nature, health, and growth, and it often evokes feelings of freshness, harmony, and renewal, especially in environmental or wellness contexts.",
    "yellow": "Yellow radiates happiness and optimism, catching attention with its brightness while also symbolizing energy, cheerfulness, and sometimes caution.",
    "orange": "Orange sparks creativity and enthusiasm, combining the energy of red and the cheer of yellow to express warmth, fun, and adventure.",
    "purple": "Purple is linked to royalty, luxury, and spirituality, often conveying ambition, wisdom, and imagination in artistic or premium designs.",
    "black": "Black stands for power and elegance, but it can also evoke mystery, formality, or even mourning, depending on its use and context.",
    "white": "White signifies purity, simplicity, and cleanliness, often used to create a sense of peace, clarity, and minimalism in modern designs.",
    "pink": "Pink conveys love, kindness, and femininity, often used to express nurturing, romance, and gentle playfulness.",
    "gray": "Gray is neutral and balanced, associated with formality, timelessness, and practicality, but it can also suggest detachment or indecision."
}
print(f"Nice to meet you {name}.")
print("What is you favourite color")
feel=input(':').lower()

if feel in color_list:
    print(f"Color: {feel}")
    print("Meaning:")
    print(color_list[feel])  # <- This prints the list for the color
else:
    print("Color not found.")


print(f"Nice chating with you {name}.Goodbye!")