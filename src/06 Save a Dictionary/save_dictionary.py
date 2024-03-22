def save_dict(dict, path):
    with open(path, "w") as file:
        file.write(str(dict))

def load_dict(path):
    with open(path, "r") as file:
        print(file.read())

dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

print(load_dict("dict.txt"))
