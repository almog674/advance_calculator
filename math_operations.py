"""
Name: math_operations.py
Author: Almog Maimon
Purpose:
Date: 01/10/2022
"""


def get_min(first_number: int, second_number: int):
    if first_number < second_number:
        return first_number
    else:
        return second_number


def get_mean(first_number: int, second_number: int):
    return (first_number + second_number) / 2


def get_max(first_number: int, second_number: int):
    if first_number > second_number:
        return first_number
    else:
        return second_number


def modulu(first_number: int, second_number: int):
    return first_number % second_number


def power(first_number: int, second_number: int):
    return first_number ** second_number


def multiply(first_number: int, second_number: int):
    return first_number * second_number


def divide(first_number: int, second_number: int):
    return first_number / second_number


def addition(first_number: int, second_number: int):
    return first_number + second_number


def subtraction(first_number: int, second_number: int):
    return first_number - second_number


def factorial(first_number: int):
    total = 1

    for i in range(first_number):
        total *= (first_number - i)

    return total


def negative(first_number: int):
    return -int(first_number)
