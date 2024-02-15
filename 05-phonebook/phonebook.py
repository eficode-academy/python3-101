''' This exercise is meant for testing all that we have learned already.

Let's create a phonebook that is stored in a dict structure and looks like this

book = {
    "Niklas": "+358406661111",
    "Hans": "+491516662222",
    "Madeleine": "+467216663333
}
Before adding numbers to it, a check is run if the number is written in a international format, meaning it has a + sign in front of the number and the leading 0 is disregarded.

Also, the name is checked for validness. Refer to tests to see what is considered invalid.

Our phonebook also has the ability to save and load to file.
'''
import re
book = {}

def add(name, number):
    '''Create a function add() that takes two parameters. Return a boolean that describes if adding that phonenumber succeeded or not. '''
    pass

def _valid_number(number):
    '''Validate the phonenumber using a regular expression \+?[\d ]+$. '''
    pass

def _valid_name(name):
    '''Validate the name using a regular expression [\w ]+$'''
    pass

def get(name):
    '''Create a function get() that takes a name of a entity in phonebook. Return the phone number of that entity in the phonebook. If the entity does not exist, return string "Unknown" instead.'''
    pass

def clear():
    '''Create a function clear() so that the phonebook is completely empty after.'''
    pass
    
def _to_string():
    '''This might be helpful helper'''
    pass

def _read(content):
   '''This might be helpful helper'''
   pass
        
def save(filename):
    '''Create a function save() that takes a filename as a parameter. Write phonebook to a file named with that filename, sorted alphabetically.

    For example, this is a valid file:
    Hans:+491516662222
    Madeleine:+467216663333
    Niklas:+358406661111
    '''
    pass
        
def load(filename):
    '''Create a function load() that loads the saved phonebook back into dictioanry. It takes a filename as a parameter and assumes the same format of the file as save() does.

    Hint: Manipulate the existing phonebook by using other functions you have already created.
    '''
    pass

