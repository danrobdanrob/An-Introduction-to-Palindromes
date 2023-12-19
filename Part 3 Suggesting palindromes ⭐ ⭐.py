def palindrome(word):
    if word[::1]== word[::-1]:
        ispalindrome = word + " is a palindrome."
    else:
        ispalindrome = word + " is not a palindrome but " + str(newpalindrome(word)) + " is."
    return ispalindrome

def newpalindrome(word):
    ibeginning = 0
    while word[ibeginning:] != word[ibeginning:][::-1]:
        ibeginning += 1
    iend = 0
    while word[:iend] != word[:-iend][::-1]:
        iend += 1
    if ibeginning >= iend:
        extendedpalindrome = word + word[:ibeginning][::-1]
    else:
        extendedpalindrome = word[:-iend][::-1] + word
    return extendedpalindrome

print("Please enter your number or phrase")
word = input()
print(palindrome(word))

#same as part 1 except
#if word is not palindromic call function newpalindrome
#newpalindrome beginning with the last character looks for the longest palindromic substring at the end of the word
#checks left to right and right to left:
#chooses the fewest number of characters to be added in order to make a palindrome or adds them to the end if they're equal
#it then adds characters from the other side of the input in reverse order to make the entire input palindromic