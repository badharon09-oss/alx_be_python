# Mad Libs Story Generator

# Ask user for words
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter a third adjective: ")
adj4 = input("Enter a final adjective: ")

# Conditional twist
if adj1.lower() == "rainy":
    extra_line = "I had to carry an umbrella all day."
else:
    extra_line = "The sunshine made everything brighter."

# Build the story
story = f"""
On a beautiful {adj1} day, I went to the zoo. 
I saw a funny {adj2} monkey swinging from the trees. 
Then, I spotted a majestic {adj3} lion lounging in the sun.  
What a wild and {adj4} experience!  
{extra_line}
"""

# Display the final story
print(story)

