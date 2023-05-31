from datetime import datetime, timezone

def convert_to_utc_timestamp(timestamp):
    if isinstance(timestamp, str):
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    elif isinstance(timestamp, datetime):
        return timestamp.replace(tzinfo=timezone.utc)
    else:
        raise TypeError("timestamp must be a str or datetime.datetime object")