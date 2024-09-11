# division

# try except block - try catch block
# try except else finally

class NegativeError(Exception):
    pass

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    if n < 0 or d < 0:
        raise NegativeError("No negative numbers please!!")

    q = n / d

    print(q)
except ZeroDivisionError:
    print("The denominator cannot be zero")
except ValueError:
    print("The inputs must be numbers")
except NegativeError as e:
    print(e)
except Exception:
    print("Something went wrong!!")

else:
    # whenever try block is successfully executed without raising any exceptions
    print("This is else block")
finally:
    # this will run at the end whether any exception was raised or not
    print("This is finally block")

print("The end of the program")