# invalid character is found in the level 
class InvalidCharacter(Exception):
    def _init_(self, message):
        super()._init_(message)

# extra characters in a line 
class ExtraCharacter(Exception):
    def _init_(self, message):
        super()._init_(message)

# missing characters in a line 
class MissingElement(Exception):
    def _init_(self, message):
        super()._init_(message)

# the number of box slots does not match the number of boxes 
class BoxCount(Exception):
    def _init_(self, message):
        super()._init_(message)