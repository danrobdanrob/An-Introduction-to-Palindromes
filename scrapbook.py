
def newpalindrome(word):
    i = 0
    longestsubstring = 0
    while i < len(word):
        candidate = word[0:i]
        if candidate[::1]== candidate[::-1]:
            longestsubstring = candidate
            i += 1
        else:
            return longestsubstring

















# def newpalindrome(word):
#     for i in word:
#         if word[:word.index(i):1]== word[:word.index(i):-1]:
#             longestsubstring = word[:i]
#             return word[0:i]
#         else:
#             return word[:i]


# print(newpalindrome('100'))


def newpalindrome(word):
    i = 0
    longestsubstring = 0
    while i <= len(word):
        candidate = word[0:i]
        if candidate[::1]== candidate[::-1]:
            longestsubstring = candidate
            i += 1
        else:
            return longestsubstring






# def palindrome(word):
#     if word[::1]== word[::-1]:
#         ispalindrome = word + " is a palindrome."
#     else:
#          ispalindrome = word + " is not a palindrome."
#     return ispalindrome

# print("Please enter your number or phrase")
# word = input()

# palindrome(word)
# print(return)




# def newpalindrome(word):
#     lengthforward(word)
#     lengthbackward(word)
#     whichislonger(word)
#     return ispalindrome
    
# def lengthforward(word):
#     while len(word[:i]) < len(word):
#         if word[:i:1]== word[:i:-1]:
#              longestpalindromeforward = longestpalindromeforward + 1
#              return lengthforward(word,(i+1))
#         else:
#             break

# def lengthbackward(word):
#     while len(word[:i]) < len(word):
#         if word[:i:1]== word[:i:-1]:
#             longestpalindromebackward = longestpalindromebackward + 1
#             return lengthbackward(word,(i+1))
#         else:
#             break
                 
# def whichislonger(word):
#     if longestpalindromeforward >= longestpalindromebackward:
#         ispalindrome = word[:i+1:-1] + word
#     else: #longestpalindromeforward < longestpalindromebackward:  #this can just be else if no further if statements are required
#         ispalindrome = word + word[:i-1]

# longestpalindromeforward = 0
# longestpalindromebackward = 0
# i= 0
# ispalindrome = 0


# def newpalindrome(word):
#     for i in word:
#         word[:i:1]== word[:i:-1]:
#             longestpalindromeforward = word[:i]


def newpalindrome(word,i):
    if len(word[:i]) < len(word):
        if word[:i:1]== word[:i:-1]:
             longestpalindromeforward = longestpalindromeforward + 1
             return newpalindrome(word,(i+1))
        else:
             if len(word[:i:-1]) < len(word):
                 if word[:i:1]== word[:i:-1]:
                     longestpalindromebackward = longestpalindromebackward + 1
                     return newpalindrome(word,(i+1))
    if len(longestpalindromeforward) >= len(longestpalindromebackward):
        ispalindrome = word[:i+1:-1] + word
    elif len(longestpalindromeforward) < len(longestpalindromebackward):  #this can just be else if no further if statements are required
        ispalindrome = word + word[:i-1]
    return ispalindrome



#p3. need to find out how to check for palindromes character by character in a string