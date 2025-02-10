def make_initials(fullname):
    # Sarah Connor
    # split the name in 2 by a space
    names = fullname.split(" ")
    # find first letters of both names (first and last)
    first_name = names[0][0]
    last_name = names[1][0]
    # join both letters by a full stop (".")
    initials = first_name + "." + last_name
    # return that string
    # S.C
    return initials
