def swap_case(s):
    a = ""
    for c in s:
        if (c == c.lower()):
            a = a + c.upper()
        else:
            a = a + c.lower()
    return a

