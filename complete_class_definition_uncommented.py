# complete_class_definition.py
# Educational example of class definitions
# using multiple classes with a Diablo II
# secret level enemy as the theme

# A commented version is available
# in the same repository folder as this file

# MIT License (c) 2026 NerArth
# may be viewed at https://github.com/NerArth/PythonEducationalExamples
# TODO: repository maintenance: make this script not rely on code duplication

class Resistance:
    """
        `Resistance` class
    This class is used to represent a single resistance to an element.

    Constructor `resistance(element, value)`:
    `element` defaults to `fire`
    `value` defaults to `0`
    """

    valid_elements = ["fire","cold","lightning","poison","physical"]
    
    def __init__(self, element, value = 0):
        """
        `__init__` method
        - This method is called when you create a new object of this class by calling `Resistance("element", "value")`
        - `self` is a special keyword reference for a specific object that's being/has been created
        - In methods and other function definitions, `variable = value` sets a default value, in case one isn't passed to the function
        """
        if element in Resistance.valid_elements:
            self.element = element
        else:
            self.element = "fire"
        self.value = int(value) if isinstance(value, (int, str)) else 0

    def __str__(self):
        """
        `__str__` method
        This method returns a string representation of the object.
        e.g. if you call `print(myresistanceobject)`
        """
        return f"{self.element}: {self.value}"

    def make_immune(self):
        """
        `make_immune` method
        This method sets the resistance to 100.
        """
        self.value = 100
        return self.value

class Resistances:
    """
        `Resistances` class
    This class is used to group multiple `Resistance` objects
    and will be used to represent the different resistances
    each enemy has.
    """
    def __init__(self, **keywordarguments):
        def create(name, key):
            """
            `create` helper function
            This function decides: do we pass a value, or skip it?
            - If we skip it, the Resistance class default (0) is automatically used.
            - This function will only exist for the duration of the constructor.
            - We will never need it outside of when we create a new `Resistances()` object,
            so this is a good example of a function that is only needed for a specific purpose.
            """
            if key in keywordarguments:
                return Resistance(name, keywordarguments[key])
            return Resistance(name)
        
        self.resistances = [
            create("fire",      "fi"),
            create("cold",      "co"),
            create("lightning", "li"),
            create("poison",    "po"),
            create("physical",  "ph")
        ]
    def __str__(self):
        return "\n".join(str(res) for res in self.resistances)

class Hell_Bovine:
    """
        `Hell_Bovine` class
    This class is used to represent a single Hell Bovine enemy
    It has default values for all its parameters, so can be created with no parameters:
    `Hell_Bovine()`
    """
    def __init__(self, name="Hell Bovine", level=50, health=500, attack=50, resistances = None):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

        self.resistances = resistances if resistances is not None else Resistances()

    def update(self):
        pass

    def __str__(self):
        return f"{self.name} (Level {self.level})\nHealth: {self.health}\nAttack: {self.attack}\nDefence:\n{self.resistances}"

# You may uncomment these to quickly test creating an object of the main class.
# print(Hell_Bovine())
# print(Hell_Bovine("Cow King",55,666,66,Resistances(co=25,li=100,ph=50)))
