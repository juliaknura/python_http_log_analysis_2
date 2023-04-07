import lab_3_b as l3b
import lab_2_a as l2a


def get_addrs(log_dictionary):
    """Returns the list of unique domain names/IP addresses (as keys of a dictionary with all entries)"""
    return list(log_dictionary.keys())


if __name__ == "__main__":
    keys = get_addrs(l3b.log_to_dict(l2a.read_log()))
    for key in keys:
        print(key)
