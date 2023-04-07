import lab_2_a as la


def get_entries_by_extension(log_tuple_list, extension):
    """Returns a list of tuples with a given file extension"""
    return list(filter(lambda tup: tup[-3][-len(extension):] == extension, log_tuple_list))


if __name__ == "__main__":
    l = get_entries_by_extension(la.read_log(), "jpg")
    for elem in l:
        print(elem)
