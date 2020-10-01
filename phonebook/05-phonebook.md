# phonebook 

Welcome to final exercise, the phonebook! This exercise is meant for testing all that we have learned already.

## Verifying your work

Run `python3 test_phonebook.py` to confirm that you have succesfully created the required functions.

## Phonebook

Our phonebook is stored in a `dict` structure and looks like this 

```
book = {
    "Niklas": "+358406661111",
    "Hans": "+491516662222",
    "Madeleine": "+467216663333
}
```

Before adding numbers to it, a check is run to check if the number is written in a international format, meaning it has a `+` sign in front of the number and the leading 0 is disregarded.

Also, the name is checked. More on these checks on the next chapter.

Our phonebook also has the ability to save and load to file. Of course, it can also be cleared.

### A quick introduction to regular expressions

Regular expressions are a widely used for search & replace operations. It can also be used to check input validation.

Regular expressions or RegExps are used in Python by importing a `re` library like this

```
import re
```

`re` library has `match` function which can be used to check input. It takes two parameters, regular expression and string that is checked for match against that expression.

```
re.match("\+?[\d ]+$", "+358406661111")
```

Let's break down the `\+?[\d ]+$`. The first part, `\+` tells us that the string has to start with `+`. The second part, `?` tells us that the first match needs to occur between 0 and 1 times. So, `+` is an optional start to our string.

Next, `[\d ]` tells us that we are looking for digit. `+` here tells us that we are looking for digit between 1 and unlimited times. Then finally, `$` says that the line ends here and we dont evaluate beyond this line.

Regular expressions might seem hard at first but like expressions, they follow a logic and are sometimes very powerful and simple way to express how things like emails, phone numbers. 

Now, let's use that expression to validate a bunch of strings

```
>>> import re
>>> numbers = ["+358 40 666 1111", "aaa+358 40 666 1111", "+358406661111", "358 40 666 111", ""]

>>> for number in numbers:
>>>     print(re.match("\+?[\d ]+$", number))

<re.Match object; span=(0, 16), match='+358 40 666 1111'>
<re.Match object; span=(0, 13), match='+358406661111'>
<re.Match object; span=(0, 14), match='358 40 666 111'>
None
```

If `re.match` returns None, there are no matches against the regular expression. We can use this functionality to build a validation into our phonebook.

## Building a Phonebook

Start by importing `re` and defining a global variable. Give that variable a type `dict`. Then, create the following functions

### add 

Create a function `add` that takes two parameters, name and phonenumber. Return a boolean that describes if adding that phonenumber succeeded or not. Validate the phonenumber using a regular expression `\+?[\d ]+$`. Validate the name using a regular expression `[\w ]+$`

### get

Create a function `get` that takes a name of a entity in phonebook. Return the phone number of that entity in the phonebook. If the entity does not exist, return `Unknown` instead.

### clear

Create a function `clear` that clears the phonebook completely. 

### save

Create a function `save` that takes a filename as a parameter. Write phonebook to file, sorted alphabetically. Format should be like this: `name:phonenumber`, separated by newline. For example, this is a valid file:

```
Hans:+491516662222
Madeleine:+467216663333
Niklas:+358406661111
```

### load

Create a function `load` that loads the saved phonebook back into memory. It takes a filename as a parameter and uses the same syntax as `save` does. 

*Hint* Mutate the existing phonebook by using existing functions you created before
*Hint* You can easily split string into list by using inbuilt function `.split`



