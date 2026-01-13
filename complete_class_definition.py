# complete_class_definition.py
# Educational example of a more complete class definition
# using multiple classes with a Diablo II secret level enemy as a theme
# 
# MIT License (c) 2026 NerArth
# may be viewed at https://github.com/NerArth/PythonEducationalExamples

# The class below contains a triple " quote marks block;
# That block is a multiline docstring.
# It's not required, but it's a good practice to document your code,
# and when you hover over the object, it will show this docstring in an IDE.
class Resistance:
    """
        `Resistance` class
    This class is used to represent a single resistance to an element.

    Constructor `resistance(element, value)`:
    `element` defaults to `fire`
    `value` defaults to `0`
    """

    # Valid spectra values for resistance
    valid_elements = ["fire","cold","lightning","poison","physical"]
    
    # This is the class constructor
    # This method is called when you create a new object of this class by doing `Resistance("element", "value")`
    # `self` is a special keyword reference for a specific object that's being/has been created
    
    # In methods and other function definitions, `variable = value` sets a default value if one isn't provided
    def __init__(self, element, value = 0):
        # Default to fire if the element provided in object construction is not valid
        if element in Resistance.valid_elements:
            self.element = element
        else:
            self.element = "fire"
        self.value = int(value) if isinstance(value, (int, str)) else 0
        

    # String representation of the object
    # This is used when you print the object
    # e.g. if you have `print(myresistanceobject)`
    def __str__(self):
        return f"{self.element}: {self.value}"

    def make_immune(self):
        self.value = 100
        return self.value
#### end of Resistance class

class Resistances:
    """
        `Resistances` class
    This class is used to group multiple `Resistance` objects
    and will be used to represent the different resistances
    each enemy has
    """
    # We don't need to set default values here because the Resistance class already has default values in its constructor
    def __init__(self, **kwargs):
        # This helper function decides: do we pass a value, or skip it?
        # If we skip it, the Resistance class default (0) is automatically used.
        def create(name, key):
            if key in kwargs:
                return Resistance(name, kwargs[key])
            return Resistance(name) # Only 1 argument = default value triggered!
        
        self.resistances = [
            create("fire",      "fi"),
            create("cold",      "co"),
            create("lightning", "li"),
            create("poison",    "po"),
            create("physical",  "ph")
        ]
    def __str__(self):
        return "\n".join(str(res) for res in self.resistances)
#### end of Resistances class

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

        # Note that this will become a new unique Resistances object for each Hell_Bovine object
        # If we don't pass a Resistances object, this will use default values from the Resistances constructor
        self.resistances = resistances if resistances is not None else Resistances()
        # In a game, having a unique object for each enemy allows each individual enemy to have its own resistances
        # e.g. allowing each enemy to be buffed or debuffed independently

    #     Pay special attention:
    # If you are used to dictionaries, you may be used to an update method such as `dictionary_var.update()`
    # An update method is not necessarily required or useful with an object
    # An update method is defined below; it deliberately does nothing to demonstrate that we do not need it in this case
    def update(self):
        pass

    def __str__(self):
        return f"{self.name} (Level {self.level})\nHealth: {self.health}\nAttack: {self.attack}\nDefence:\n{self.resistances}"
#### end of Hell_Bovine class

print(Hell_Bovine())
print(Hell_Bovine("Cow King",55,666,66,Resistances(co=25,li=100,ph=50)))
