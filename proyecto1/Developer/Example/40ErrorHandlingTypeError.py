
def palindrome(string):
    return string == string[::-1]

try:
    print(palindrome("ana"))
except TypeError:
    print("Solo se puede ingresar numero")