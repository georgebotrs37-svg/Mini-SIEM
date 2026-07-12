seen = set()

def is_new(alert):
    key = alert["raw"]

    if key in seen:
        return False

    seen.add(key)
    return True