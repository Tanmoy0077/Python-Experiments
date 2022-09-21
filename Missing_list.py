def missing(li):
    """ Leet Code Problem """
    m = max(li)
    l2 = list(range(m+1))
    s1 = list(set(l2) - set(li))
    if not(s1):
        return m+1
    else:
        return s1[0]

print(missing(list(range(12))))
