# 9. Exercise. Collections Advanced
# Write code demonstrating how to create a new list.
# You must demonstrate understanding 

bounty_hunter = ["Samus Aran", "Zer0", "Santa Claws"]
bounty_counter = {bounty_hunter[0]: 832, "Zer0": 216, "Santa Claws": "Countless"}

# Alter the code below.
# - You MUST create a single new `list` variable called `gender`.
# - You MUST create the new list within the for loop.
# - You MUST make sure the list is created only once and not every iteration.
# This exercise benefits from understanding conditional statements.
# You may rename the new list variable to any name you like but remember to alter its name in existing code.
# You may use any values you like within the list, but it MUST contain at least 3 values.

for i in range(len(bounty_hunter)):
    print(bounty_hunter[i])
    print(bounty_counter[bounty_hunter[i]])
    print(gender[i])