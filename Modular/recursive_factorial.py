
def factorial(limit) :
    u""" returns factorial number
    this implementation uses recursive programming technique
    """
    if limit > 1 :
        return limit * factorial(limit -1)
    return 1
