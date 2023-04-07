import lab_2_a as l2a
import lab_3_a as l3a
import entry_dict_functions as edf


def log_to_dict(log_tuple_list):
    """Sorts all entries into a dictionary with domain names/IP addresses as keys"""
    log_dict = {}
    for elem in log_tuple_list:
        if log_dict.get(elem[0], -1) == -1:
            log_dict[elem[0]] = [l3a.entry_to_dict(elem)]
        else:
            log_dict[elem[0]].append(l3a.entry_to_dict(elem))
    return log_dict


if __name__ == "__main__":
    dicti = log_to_dict(l2a.read_log())
    for key in dicti:
        print("--------------", end="")
        print(key, end="")
        print("----------------------------------------")
        for entry_dict in dicti[key]:
            edf.print_dict(entry_dict)
