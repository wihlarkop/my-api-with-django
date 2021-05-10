import datetime


def date_convert(data: datetime):
    date_format = '%Y-%m-%d %H:%M:%S'
    if isinstance(data, (datetime.datetime, datetime.date)):
        return data.strftime(date_format)
    elif data == '0000-00-00' or not data:
        data = None
    return data
