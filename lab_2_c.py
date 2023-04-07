import lab_2_a as la


def get_entries_by_addr(log_tuple_list, domain_name):
    """Returns a filtered list of tuples with a given domain_name"""
    return list(filter(lambda tup: tup[0] == domain_name, log_tuple_list))


if __name__ == "__main__":
    test_list = get_entries_by_addr(la.read_log(), "lmsmith.tezcat.com")
    for elem in test_list:
        print(elem)
