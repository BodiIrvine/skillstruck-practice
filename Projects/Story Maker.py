# Define the string variables for the story
part1 = "Once upon a time, in a land far, far away, "
part2 = "there was a small village that was known for its beautiful gardens. "
part3 = "In this village lived a young girl named Lily who loved to explore. "
part4 = "One sunny day, Lily discovered a hidden path in the forest. "
part5 = "She followed the path and found a mysterious old book. "
part6 = "The book was covered in ancient symbols and glittered in the sunlight. "
part7 = "Excited, Lily took the book home and showed it to her grandmother. "
part8 = "Her grandmother recognized the symbols and told her that the book was magical. "
part9 = "With a sense of wonder, Lily began to read the book and uncover its secrets. "
part10 = "And so, Lily's adventure had just begun."

# Concatenate the strings to form the story
story = part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9 + part10

# Print the story
print("Story 1:")
print(story)

# Define a different set of strings for the second story
part1_2 = "In a bustling city filled with skyscrapers, "
part2_2 = "lived a curious cat named Whiskers who dreamed of adventure. "
part3_2 = "One day, Whiskers spotted a balloon floating by his window. "
part4_2 = "He decided to follow it, jumping from rooftop to rooftop. "
part5_2 = "The balloon led him to a rooftop garden he had never seen before. "
part6_2 = "There, Whiskers met a friendly parrot named Polly. "
part7_2 = "Polly invited Whiskers to explore the garden and share some fruit. "
part8_2 = "As they chatted, they discovered that they both loved exploring new places. "
part9_2 = "Together, they planned many more adventures around the city. "
part10_2 = "Whiskers realized that sometimes, the best adventures are the ones you find with friends."

# Concatenate the strings to form the second story
story2 = part1_2 + part2_2 + part3_2 + part4_2 + part5_2 + part6_2 + part7_2 + part8_2 + part9_2 + part10_2

# Print the second story
print("\nStory 2:")
print(story2)

# Convert the first story to uppercase
story_upper = story.upper()

# Convert the second story to lowercase
story2_lower = story2.lower()

# Replace a word in the first story
story_replaced = story.replace("Lily", "Alex")

# Print the modified stories
print("\nStory 1 in Uppercase:")
print(story_upper)

print("\nStory 2 in Lowercase:")
print(story2_lower)

print("\nStory 1 with Replacement:")
print(story_replaced)
