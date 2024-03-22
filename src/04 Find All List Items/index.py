def index_all(search_list, item):

    index_list = []
    for index, value in enumerate(search_list):

        if value == item:
            index_list.append([index])

        elif isinstance(search_list[index], list):

            for i in index_all(search_list[index], item):

                index_list.append([index] + i)

    return index_list

exemple = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(index_all(exemple, 2))
print(index_all(exemple, [1, 2, 3]))