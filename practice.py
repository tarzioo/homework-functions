"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

    >>> nums = [1, 2]
    >>> add_new_number(5, nums)
    >>> nums
    [1, 2, 5]

    
    """
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """function prints 'hello world'

    function does not take any parameters and does not return anything. It only
    prints 'hello world'
    """

    print "Hello World"

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name

def say_hi(name):
    """function prints 'Hi' followed by the name

    function takes in a string parameter and binds it to the name variable.
    the string 'Hi' is printed followed by the name variable
    Nothing is returned
    """

    print "Hi " + name

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result

def print_product(num1, num2):
    """function takes in two integers and multiplies them together

    Two integers are passed into the parameter as num1 and num2. They are multiplied
    together and the result in printed. Nothing is returned
    """

    print num1 * num2



# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(str, num):
    """Function prints string on repeat based on integer 

    Function takes string and binds to str as a paramter. num is a integer parameter
    function prints out str parameter and repeats it based on the num parameter
    nothing is returned
    """

    print str * num


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(num):
    """Receives integer parameter and prints either 'Higher than 0' or
    'lower than 0' or 'zero' based on integer

    Function takes in integer paramter and binds it to num. If num is higher
    than zero then 'Higher than 0' is printed. If num is lower than zero
    then 'Lower than 0' is printed. Otherwise is num is zero then 'Zero' is
    printed. Nothing is returned
    """

    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"


# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(num):
    """Function takes in an integer and returns Boolean based on if it's divisible
    by 3

    Function takes in an integer and binds it to num. Num is tested to see if it
    is divisible by 3. If true, True is returned. Otherwise, False is returned.
    """
    if num % 3 == 0:
        return True
    else:
        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces

def num_spaces(sentence):
    """Function receives string and returns the number of spaces in string

    The function takes in a string for its parameter and binds it to sentence.
    the amount of spaces in sentence are counted and returned
    """

    count = 0
    for char in sentence:
        if char == " ":
            count += 1

    return count


# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(meal_price, tip = 0.15):
    """Function receives two floats and returns a new amount. A default parameter
    is set if second parameter does not get set, it default to 0.15

    Function receives first float parameter and binds it to meal_price. It receives
    in second float parameter and binds it to tip. If second parameter is not
    given, it defaults to 0.15. The total of meal_price and tip are calculated
    and is returned.
    """

    return meal_price + (meal_price * tip)


# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.

def sign_and_parity(num):
    """function takes in an integer and returns a list

    """
    num_properties = []

    if num % 2 == 0:
        num_properties.append("Even")
    else:
        num_properties.append("Odd")


    if num >= 0:
        num_properties.append("Positive")
    else:
        num_properties.append("Negative")


    return num_properties





################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(RECIPIENT_NAME, JOB_TITLE = "Engineer", SENDER_NAME = "from"):
    """

    """
    print "Dear %s %s, I think you are amazing! Sincerely, %s" % (JOB_TITLE,
    RECIPIENT_NAME, SENDER_NAME)

def full_title(RECIPIENT_NAME, JOB_TITLE = "Engineer"):
    return JOB_TITLE + " " + RECIPIENT_NAME

def add_new_number(new_num, list_of_num):
    """function takes in number as a list and adds number to list and returns list
    function has 2 parameters. first parameter is a number and is binded to new_num.
    the second parameter is a list of numbers binded to list_of_num. new_num is
    appended to list_of_num and is returned
    """

    list_of_num.append(new_num)

    return list_of_num  
#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


