def timestamp_to_utc(timestamp):
    return datetime.fromtimestamp(timestamp) \
                   .strftime('%Y-%m-%d %H:%M:%S')