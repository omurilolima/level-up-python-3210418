def is_palindrome(s):

    forwards = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    backwards = forwards[::-1]
    return forwards == backwards

    # s = s.lower().replace(" ", "").replace(",", "")
    # index = -1
    # for char in s:
    #     if char != s[index]:
    #         return False
    #     index -= 1

    # return True

print(is_palindrome("race CARRO"))
print(is_palindrome("race CAR"))
print(is_palindrome("Sir, I demand, I am a maid named Iris."))
