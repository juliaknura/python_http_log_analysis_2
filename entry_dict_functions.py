import log_functions as lf


def get_entries_by_code(log_dict_list, code):
    """Returns a list of dictionaries with a given HTTP response code"""
    if lf.validate_code(code):
        return list(filter(lambda cur_dict: cur_dict["HTTP response code"] == code, log_dict_list))
    else:
        return []


def sort_dict(log_dict_list, parameter):
    """Sorts a list of logs in dictionary format. Parameter is the key to access the element in the dictionary
    which will be the sorting key: \n
    ip - domain name/IP address \n
    datetime - datetime \n
    HTTP request method - HTTP request method \n
    path - path \n
    HTTP response code - HTTP response code \n
    size - size
    """
    return sorted(log_dict_list, key=lambda cur_dict: cur_dict[parameter])


def print_dict(my_dict):
    print("{")
    for key in my_dict:
        print(key, end=": ")
        print(my_dict[key])
    print("}")


