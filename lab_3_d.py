import lab_2_a as l2a
import entry_dict_functions as edf
import lab_3_b as l3b


def print_dict_entry_dates(entry_dictionary):

    for key in entry_dictionary:

        print("IP address/domain name: " + key)
        print("Number of entries: ", end="")
        print(len(entry_dictionary[key]))

        min_entry = min(entry_dictionary[key], key=lambda cur_dict: cur_dict["datetime"])
        max_entry = max(entry_dictionary[key], key=lambda cur_dict: cur_dict["datetime"])

        print("Earliest entry: ")
        edf.print_dict(min_entry)
        print("Latest entry: ")
        edf.print_dict(max_entry)

        print("Ratio of successfull requests (code 200) to all requests: " +
              str(len(edf.get_entries_by_code(entry_dictionary[key], 200))/len(entry_dictionary[key])))
        print("---------------------------------------------------")


if __name__ == "__main__":
    print_dict_entry_dates(l3b.log_to_dict(l2a.read_log()))
