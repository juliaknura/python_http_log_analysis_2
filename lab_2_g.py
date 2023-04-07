import lab_2_a as la


def get_entries(log_tuple_list):
    """Prints the list of tuples"""
    for elem in log_tuple_list:
        print(elem)


if __name__ == "__main__":
    get_entries(la.read_log())

