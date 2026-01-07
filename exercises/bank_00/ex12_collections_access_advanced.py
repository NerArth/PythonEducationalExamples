# 12. Exercise. Collections Access Advanced
# Write code demonstrating understanding of given nested collections (lists and dictionaries) and
# showing how to access different levels of nested data.
# You do not have to use loops in this exercise.

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

# Write code here.
# - You MUST print the value of a deeply nested collection (at least 2 levels deep).
# - The printed value must NOT be an entire list or dictionary.