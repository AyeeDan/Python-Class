try:
    num = int(input("Enter a number: "))

except ValueError:
   print("BRUH! Use a number, pls!! D:")

try:
    num2 = int(input("Enter a number, pls! I'm going it divide 10 by it!: "))
    result = 10 / num2

except ZeroDivisionError:
    print ("bro, you literally can't even divide by zero-")

try:
    print ("Searching for example.txt...")
    file = open("example.txt", "r")
    content = file.read()

except(FileNotFoundError, PermissionError):
    print ("hey bro, that file doesn't exist, unlike some of us. Like we exist, but why? And how? What is the meaning of existence even??? Many people have questioned existence before, like wondering how humans were created or something. Scientists have multiple theories for how humans came into existence. ...Anyway, example.txt does not exist!")
    
try:
    print ("Opening an existing file...")
    phile = open("data.json", "r")
    content = phile.read()
    phile.close()
    content = phile.read()
    

except(ValueError):
    print ("I will be watching you at 3 am tonight from under your bed :)")

try:
    hi = int(input("Enter a number(numerator): "))
    hoi = int(input("Enter another number(denominator): "))
    hello = hi/hoi

except (ZeroDivisionError):
    print ("HEY! you can't divide by ZERO DA HERO!! D:")

except (ValueError):
    print ("enter a number pwease... i'm DESPERWATE to get a move on with the code! :,(")

except (PermissionError, FileNotFoundError):
    print ("if this error occurs, then i don't know what you could have done honestly, this has nothing to do with file errors...")



class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = f"Negative value error!! REALLLL YES: {value} SEEMS like tis is not ALLOWEEEED"
        super().__init__(self.message)

def divide(numerator, denominator):
    if numerator < 0:
        raise NegativeValueError(numerator)
    if denominator < 0:
        raise NegativeValueError(denominator)
    return numerator / denominator

try:
    hi = float(input("Enter a number (numerator): "))
    hoi = float(input("Enter another number (denominator): "))
    
    hello = divide(hi, hoi)
    print(f"The result is: {hello}")

except ZeroDivisionError:
    print("HEY! you can't divide by ZERO DA HERO!! D:")
except ValueError:
    print("Enter a number pwease... I'm DESPERWATE to get a move on with the code! :,(")
except NegativeValueError as e:
    print(e)
except Exception as e:
    print(f"an UNEXPECTEEEEEEEED error happened. what did ya do? :O : {e}")






















    
