import lab_2_a as la
import re


def get_failed_entries_by_code(log_tuple_list, join_lists):
    """Takes two parameters: list of log tuples and a logical parameter which determines if two list or one
    joined is returned"""
    client_error_list = list(filter(lambda tup: re.match("4..", str(tup[-2])), log_tuple_list))
    server_error_list = list(filter(lambda tup: re.match("5..", str(tup[-2])), log_tuple_list))
    if join_lists:
        return client_error_list + server_error_list
    else:
        return client_error_list, server_error_list


if __name__ == "__main__":
    logs = la.read_log()
    l1 = get_failed_entries_by_code(logs, True)
    print(len(l1))
    l2, l3 = get_failed_entries_by_code(logs, False)
    print(len(l2))
    print(len(l3))
