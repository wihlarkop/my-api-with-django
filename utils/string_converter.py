from datetime import datetime


def convert_string_data_to_datetime(data):
    convert_data = datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f')
    data = convert_data.strftime('%Y-%m-%d')
    return data
