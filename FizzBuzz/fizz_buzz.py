def fizz_buzz(arg):
    """a function that returns FizzBuzz, Fizz or Buzz for multiples of both 5 and 3, 3 or 5 respectively"""
    if isinstance(arg, int):
        if arg % 5 == 0 and arg % 3 == 0:
            return "FizzBuzz"
        elif arg % 3 == 0:
            return "Fizz"
        elif arg % 5 == 0:
            return "Buzz"
        else:
            return arg
    else:
        return arg
