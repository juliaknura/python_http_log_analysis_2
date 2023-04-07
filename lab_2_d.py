import sys
import lab_2_a as la
import log_functions as lf


def get_entries_by_code(log_tuple_list, code):
    """Returns a list of tuples with a given HTTP response code"""
    if lf.validate_code(code):
        return list(filter(lambda tup: tup[-2] == code, log_tuple_list))
    else:
        return []


if __name__ == "__main__":
    test_list = get_entries_by_code(la.read_log(), int(sys.argv[1]))
    for elem in test_list:
        print(elem)
