def convert_duration(duration_int):
    duration = int(duration_int)
    min = str(duration // 60).zfill(2)
    seg = str(duration % 60).zfill(2)
    return min + ":" + seg