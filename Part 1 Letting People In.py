def palindrome(word):
    if word[::1]== word[::-1]:
        ispalindrome = word + " is a palindrome."
    else:
         ispalindrome = word + " is not a palindrome."
    return ispalindrome

print("Please enter your number or phrase")
word = input()

print("Checking...")
print(palindrome(word))

#asks the user to enter a number or phrase
#slices through it forwards and backwards
#if the slices are the same returns that the input is a palindrome.