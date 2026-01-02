# dict_vs_obj.py
# Educational comparison of a dictionary and a class, in a family theme
# as per the W3 schools website for Python classes and dictionaries
# 
# MIT License (c) 2026 NerArth
# may be viewed at https://github.com/NerArth/PythonEducationalExamples

# ORIGINAL DICT
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# CLASSES
class person:
    # This is the class constructor
    # This method is called when you create a new object of this class by doing `person("name", "age", "family")`
    #
    # `self` is a special keyword reference for a specific object that's being/has been created
    def __init__(self,name,age,family):
        self.name = name
        self.age = age
        self.family = family # a direct reference to the family object this person object belongs to, making it easy to access the family object from the person object
        # note that cyclical references like this can cause issues and have to be handled and planned carefully
    
    def givebirth(self,name,year):
        _baby = person(name,year,self.family)
        self.family.addchild(_baby.name,_baby.age)

class family:
    def __init__(self,surname):
        self.children = {}
        self.counter = -1
        self.surname = surname # it's a good idea to have the surname as a property of the family object because it's shared between all children and means less duplicate data
  
    def addchild(self,name,year):
        self.counter += 1
        self.children.update({self.counter:person(name,year,self)})

# generic list of families
families = []
  
# get all children from a family
def getchildren(_family):
    # This try/except block stops the script from crashing if `_family.children` is not valid
    # or if `_family` is not a valid object in the way we expect it to be
    # as in the case of the original dict
    try:
        for child in _family.children:
            print(f"Child: {_family.children[child].name} {_family.surname}")
    except Exception as e:
        print(f"```\nWarn: Could not get `_family.children` from: {type(_family)}.\nError: {e}\n```\n")

    # This checks if `_family` is an instanced object of the `family` class
    # if it isn't, we still want to pass on the variable as it is
    if isinstance(_family, family):
        return _family.children
    else:
        return _family

# Get all `children` from all `families`
def geteveryone():
    print("\nEveryone who exists:")
    # Loop through all `families`
    for _family in families:
        getchildren(_family)

def main():
    # VARS
    fam1 = family("Bond")
    fam2 = family("Smith")

    families.append(fam1)
    families.append(fam2)
    families.append(myfamily)

    fam1.addchild("Tobias",2004)
    fam1.addchild("Janet",1999)
    fam2.addchild("Karen",2002)
    
    # MAIN CODE
    print("\n")

    # Accessing the original dict
    print("\n\nAccessing the original dict:")
    print(myfamily["child2"]["name"])

    # Using the class method (aka function) to access the object properties
    print("\n\nUsing the class method (aka function) to access the object properties:")
    getchildren(fam1)
    getchildren(fam2)

    # Alternatively, we can use the function to get all children from all families
    print("\n\nAlternatively, we can use the function to get all children from all families:")
    geteveryone()

    # Accessing the object properties directly
    print("\n\nAccessing the object properties directly:")
    print(f"{fam1.children[0].name} {fam1.surname}")
    print(f"{fam2.children[0].name} {fam2.surname}")

    # Now let's add some more children via the `person()` `givebirth()` method
    print("\n\nNow let's add some more children via the `person()` `givebirth()` method:")
    families[0].children[1].givebirth("Steven",2026)
    families[1].children[0].givebirth("Lily",2026)

    # Get everyone again
    geteveryone()

# RUN
main()