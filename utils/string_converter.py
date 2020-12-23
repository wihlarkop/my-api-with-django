from datetime import datetime


def convert_format_datetime_to_string(data):
    convert_data = datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f%z')
    data = convert_data.strftime('%Y-%m-%d')
    return data
