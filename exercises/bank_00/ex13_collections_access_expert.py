# 13. Exercise. Collections Access Expert
# Write code demonstrating understanding of given nested collections.
# You must demonstrate this with the use of loops.

secret_farm_level = {
    "name": "Moo Moo Farm",
    "location": "Secret Cow Level",
    "access": "Secret",
    "completed": False,
    "mobs": [
        {
            "name": "Hell Bovine",
            "type": "Common",
            "drops": [
                "Halberd",
                "Two-handed Axe",
                "Gold"
            ]
        },
        {
            "name": "Cow King",
            "type": "Unique",
            "drops": [
                "Halberd",
                "Two-handed Axe",
                "Unique Ring",
                "Gold"
            ],
            "resistances": [
                ["Lightning", 100],
                ["Cold", 40],
                ["Fire", 25]
            ]
        }
    ]
}

# Alter the code below.
# - You MUST print the VALUE of a very deeply nested collection (at least 3 levels deep).
# - The printed value must NOT be an entire list or dictionary.
# - You must NOT print a key.
# - You MUST use the existing `for` loop to access the value.
# However, you may alter anything at all about it and ONLY need to keep the `for` keyword.
# You may use conditionals if needed.

for x in secret_farm_level:
    print(x)