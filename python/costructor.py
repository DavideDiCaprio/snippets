class Game:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

g = Game("Test", "Survival")


'''
__init__ act like a constructor but is not. It's recieve the instance of the object, doesn't create it
it recieve ti instance already created and imposta the attributes

__new__ create the object

__init__ depends on __new__ and inizialize it

__new__ is implicit, is necessary to use when needed modifying object creation itself,
 Like implementing singleton pattern, custom metaclasses
 Python loc chimaa automaticamente, è un metodo statico 


__init__ reconize a folder as a package
'''