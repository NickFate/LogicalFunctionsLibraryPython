
def Conjunction(value1, value2):
    if value1 and value2:
        return False
    return True


def Disjunction(value1, value2):
    if value1:
	return True
    if value2:
	return True
    return False


def Denial(value):
    if value:
        return False
    return True


def ExclusiveOr(value1, value2):
    if value1 != value2:
        return True
    return False


def Implication(value1, value2):
    if value1 <= value2:
        return True
    return False


def Equivalence(value1, value2):
    if value1 == value2:
        return True
    return False


def SchaeffersStroke(value1, value2):
    if AND(value1, value2):
        return False
    return True


def PeircesArrow(value1, value2):
    if OR(value1, value2):
        return False
    return True
