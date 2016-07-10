# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_tax(state, cost_amount, tax = 0.05):
    """Function takes in three paramters and returns the result. the third parameter
    is set to a default number based on user input

    Function receives a string and binds it to the state variable. It receives
    an int or float and binds it to cost_amount. It receives a float number for
    the tax variable as sets it to a default of 0.05. If state is 'CA' then tax
    is changed to 0.07. The function computes cost_amount plus cost_amount multiplied
    by tax and returns the result
    """

    if state == 'CA':
        tax = 0.07

    return  cost_amount + cost_amount * tax   

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit):
    """Receives string as a parameter and returns a boolen

    Function takes in a string as a paramter and binds it to the fruit variable
    If fruit is equal to 'strawberry', 'cherry' or 'blackberry', then True is
    returned. Otherwise False is returned.
    """

    fruit_list = ['strawberry', 'cherry', 'blackberry']

    if fruit in fruit_list:
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit):
    """Function takes in a string and calls upon is_berry to return a number

    Function takes in a string and binds it to the fruit variable. It calls upon
    is_berry and looks for its result. If is_berry is returning True, then
    shipping_cost returns 0. Otherwise if is_berry is returning False, then
    shipping cost returns 5
    """

    if is_berry(fruit) == True:
        return 0
    else:
        return 5
#
# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
def is_hometown(town):
    """Function takes in a string and returns True or False based on eveluation of string"

    Function takes in a string and binds it to the town variable. my_hometown is a
    variable that is set to equal my home town. If town is equal to my_hometown
    then True is returned. Otherwise if it is not equal then False is returned
    """
    my_hometown = "oklahoma city"

    if my_hometown == town:
        return True
    else:
        return False
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first, last):
    """Function received two string paramters and returns concatenation of both"

    Function receives first string parameter and binds it to first variable. second
    string parameter gets binded to last. First and last and concatenated and
    the result is returned
    """

    return first + " " + last
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town, first, last):
    """ Function receives 3 string parameters and calls upon is_hometown and
    full_name and returns a string

    Function takes in first string parameter and binds it to town. Second string 
    parameter is binded to first and the 3rd parameter is binded to last. Function 
    calls upon is_hometown and it is_hometown returns true, then string is printed
    and calls upon the full_name function and returns a string. If is_hometown
    is false, a differnt string is returned, also calling upon the full_name
    function
    """
    
    if is_hometown(town) == True:
        print "Hi " + full_name(first, last) + ", we're from the same place!"

    else:
        print "Hi " + full_name(first, last) + ", where are you from?"  
#


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x = 1):
    def add(y):
        return x + increment()

    return add()

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

#addfive = increment(5)



# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def list_of_numbers(num, list_of):
    """ Function receives a number and a list and returns number being added to list_of

    Function takes in two parameter. The first paramter is a number and gets binded
    to num. The second parameter is a list and is binded to list_of. num gets appended
    the list_of and is returned
    """
    list_of.append(num)

    return list_of

#####################################################################