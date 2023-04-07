import log_functions as lf


def read_log():
    """Transforms input logs into a list of tuples"""
    tuple_list = []
    while True:
        try:
            line = input()
            try:
                current_tuple = (lf.give_domain_name(line), lf.give_datetime_format(line),
                                 lf.give_http_request_method(line), lf.give_path(line), lf.give_code(line),
                                 lf.give_size(line))
                tuple_list.append(current_tuple)
            except RuntimeError:
                continue
            except ValueError:
                continue
        except EOFError:
            break
    return tuple_list




