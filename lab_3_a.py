import lab_2_a as la
import entry_dict_functions as edf


def entry_to_dict(entry):
    """Transforms a given entry to a dictionary form"""
    entry_dict = {
        "ip": entry[0],
        "datetime": entry[1],
        "HTTP request method": entry[2],
        "path": entry[3],
        "HTTP response code": entry[4],
        "size": entry[5]
    }
    return entry_dict


if __name__ == "__main__":
    edf.print_dict(entry_to_dict(la.read_log()[50]))
