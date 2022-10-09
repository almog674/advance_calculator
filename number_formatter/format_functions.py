from utils.constants import Operators, ROUND_DIGITS, Notations


def preprocess_number(number):
    number = format_negative_number(number)
    number = round_number(number)

    return number


def postprocess_result(result):
    result = str(result)
    result = handle_scientific_notation(result)
    result = replace_special_minus_notation(result)

    return result


def round_number(number: str) -> str:
    return str(round(float(number), ROUND_DIGITS))


def format_negative_number(number: str) -> str:
    return number.replace(Operators.NEGATIVE_NUMBER, Operators.SUBTRATION)


def replace_special_minus_notation(number: str) -> str:
    """
    The calculator may use special notation for negative number instead of minus
    for not be confused with the subtraction operator.
    """
    return number.replace(Operators.SUBTRATION, Operators.NEGATIVE_NUMBER)


def handle_scientific_notation(number: str) -> str:
    if Notations.SCIENTIFIC in number:
        result = float(number)
        result = "{:.1f}".format(result)

        return str(result)

    return number

