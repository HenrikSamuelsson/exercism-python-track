def is_armstrong_number(number):
    """
    Deduces if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    :param number: Number to be investigated.
    :return: True if the input number is an Armstrong number, False otherwise.
    """
    number_of_digits_in_number = len(str(number))
    number_copy = number
    calculated_number = 0
    while number_copy != 0:
        calculated_number += (number_copy % 10) ** number_of_digits_in_number
        number_copy //= 10
    return number == calculated_number
