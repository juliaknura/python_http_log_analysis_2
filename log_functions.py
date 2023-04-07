from datetime import datetime


def give(txt, pos, element_type):
    split_line = txt.split(" ")
    if len(split_line) < abs(pos):
        raise RuntimeError(f"Invalid log -- {element_type} cannot be read")
    return split_line[pos]


def give_code(txt):
    """A function that takes a log and returns a status code in Integer format"""
    return int(give(txt, -2, "code"))


def give_size(txt):
    """A function that takes a log and returns a resource size in bytes"""
    return_value = give(txt, -1, "size")
    if return_value == "-":
        return 0
    else:
        return int(return_value)


def give_path(txt):
    """A function that takes a log and returns a resource path"""
    return give(txt, 6, "path")


def give_domain_name(txt):
    """A function that takes a log and returns a resource path"""
    return give(txt, 0, "domain name")


def give_http_request_method(txt):
    """A function that takes a log and returns a HTTP request method"""
    return give(txt, 5, "request_method")[1:]


def give_full_date(txt):
    """A function that takes a log and returns a datetime in string format: DD/MMM/YYYY:HH:MM:SS"""
    returned_val = give(txt, 3, "date")
    return returned_val[1:]


month_dictionary = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}


def month_change_format(month_string):
    return month_dictionary.get(month_string)


def give_datetime_format(txt):
    """A function that takes a log and returns a full date in a datetime format"""
    date_time = give_full_date(txt)
    dt = datetime(int(date_time[7:11]), month_change_format(date_time[3:6]), int(date_time[:2]), int(date_time[12:14]),
                  int(date_time[15:17]), int(date_time[-2:]))
    return dt


"""Complete dictionary of all HTTP response codes"""
code_dictionary = {
    100: "Continue",
    101: "Switching protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found (Previously \"Moved Temporarily\")",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "Switch Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a Teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required",
}


def validate_code(code):
    """Check is given code is a valid HTTP response code"""
    return code_dictionary.get(code, -1) != -1
