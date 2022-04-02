
def factorial(limit) :
    u""" returns factorial number
    this implementation uses iterative programming technique
    """
    if limit > 1 :
        result = limit
        for number in range(2, limit) :
            result *= number
        return result
    return 1
