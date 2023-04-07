import lab_2_a as la


def sort_log(log_tuple_list, parameter):
    """Sorts a list of logs in tuple format. Parameter indicates a number of the element in the tuple used as key: \n
    0 - domain name/IP address \n
    1 - datetime \n
    2 - HTTP request method \n
    3 - path \n
    4 - HTTP response code \n
    5 - size
    """
    if len(log_tuple_list) <= parameter:
        raise IndexError
    return sorted(log_tuple_list, key=lambda cur_tuple: cur_tuple[parameter])


if __name__ == "__main__":
    test_list = sort_log(la.read_log(), 1)
    for elem in test_list:
        print(elem)



