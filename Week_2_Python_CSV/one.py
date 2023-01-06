def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")


def is_palindrome(str):
    reverse = ''.join(reversed(str))
    if(str == reverse):
        return True
    return False   

str1 = input("Enter the string: ")
palindrome = is_palindrome(str1)
if (palindrome):
    print("True")
else:
    print("False")  
        
if __name__ == "__main__":
    palindrome
else:
    print("one.py is being imported into another module")


