# complete_class_definition.py
# Educational example of class definitions
# using multiple classes with a Diablo II
# secret level enemy as the theme

# An uncommented version is available
# in the same repository folder as this file

# MIT License (c) 2026 NerArth
# may be viewed at https://github.com/NerArth/PythonEducationalExamples



# The first class below contains a triple " quote marks block;
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
    # - This is a class variable, not a property
    # - It is shared by all objects of this class
    valid_elements = ["fire","cold","lightning","poison","physical"]
    
    # This is a class constructor, a special method
    def __init__(self, element, value = 0):
        """
        `__init__` method
        - This method is called when you create a new object of this class by calling `Resistance("element", "value")`
        - `self` is a special keyword reference for a specific object that's being/has been created
        - In methods and other function definitions, `variable = value` sets a default value, in case one isn't passed to the function
        """
        # Default to fire if the element provided in object construction is not valid
        # - This will prevent an error, and for classes, is a different way of setting
        # a default value for an argument a function is expecting.
        if element in Resistance.valid_elements:
            self.element = element
        else:
            self.element = "fire"
        self.value = int(value) if isinstance(value, (int, str)) else 0
        # The above `self.value` definition is equivalent to:
        # - Convert value to `int` if it's a `str`, otherwise default to 0
        # - You will notice that the variable assignment makes use of an "inline if" statement
        # - This is a common pattern in Python, and is used to set a default value
        # Then this is equivalent to:
        #   ```
        #   if isinstance(value, (int, str)):
        #       self.value = int(value)
        #   else:
        #       self.value = 0
        #   ```

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
#### end of Resistance class

class Resistances:
    """
        `Resistances` class
    This class is used to group multiple `Resistance` objects
    and will be used to represent the different resistances
    each enemy has.
    """
    # We shouldn't need to set default values here because the Resistance class already has default values in its constructor
    def __init__(self, **keywordarguments):
        # This helper function decides: do we pass a value, or skip it?
        #   - If we skip it, the Resistance class default (0) is automatically used.
        
        # The `**keywordarguments` is a dictionary of arguments passed to the constructor.
        #   - Python convention usually shortens this to `**kwargs`
        def create(name, key):
            if key in keywordarguments:
                return Resistance(name, keywordarguments[key])
            return Resistance(name) # Only 1 argument = default value triggered!
        
        # By passing 
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
        # Set the object's properties
        # - These will be unique to each new object instance of the class
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

        # Note that this will become a new unique Resistances object for each Hell_Bovine object
        # - If we don't pass a Resistances object, this will use default values from the Resistances constructor
        self.resistances = resistances if resistances is not None else Resistances()
        # In a game, having a unique object for each enemy allows each individual enemy to have its own resistances
        # - e.g. allowing each enemy to be buffed or debuffed independently

    # Notice:
    # - If you are used to dictionaries, you may be used to an update method such as `dictionary_var.update()`
    # - An update method is not necessarily required or useful with an object
    # - An update method is defined below; it deliberately does nothing to demonstrate that we do not need it in this case
    def update(self):
        pass

    def __str__(self):
        return f"{self.name} (Level {self.level})\nHealth: {self.health}\nAttack: {self.attack}\nDefence:\n{self.resistances}"
#### end of Hell_Bovine class


# You may uncomment these to quickly test creating an object of the main class.
# print(Hell_Bovine())
# print(Hell_Bovine("Cow King",55,666,66,Resistances(co=25,li=100,ph=50)))
