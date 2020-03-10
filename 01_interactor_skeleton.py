import foo
import bar

# Custom errors.
class MyError(RuntimeError): pass 
 
class VerbAdjectiveNoun(): 
    def __init__(self, ...args):
        # Set instance variables.
        # Validate input as much as possible.
        # Raise errors if necessary.
        pass
 
    def run(self): 
        # Validate input as much as possible.
        # Raise errors if necessary.
        # Do business logic.
        return True

    @classmethod
    def _private_method(self, some_data):
        return other_data
