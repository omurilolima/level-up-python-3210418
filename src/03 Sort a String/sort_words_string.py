def sort_words(s):

    return " ".join(sorted(s.split(), key=str.casefold))

print(sort_words("cana branca abrir"))
print(sort_words("string Zorro words"))
print(sort_words("string Of words"))