def show_by_gener(a, b):
    c = []
    for key in a:
        if a[key] == b:
            c.append(key)
    return c


def shows_avg_rating(c, d):
    e = []
    for i in range(len(d)):
        for key in c:
            if d[i] == key:
                e.append(c[key])
    return float(sum(e)) / max(len(e), 0)
