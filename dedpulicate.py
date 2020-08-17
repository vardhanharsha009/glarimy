def deduplicate(str):
    ret = str.split()
    ret = list(set(ret))
    return ret