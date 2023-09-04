import re
from typing import Iterable
from fastapi.datastructures import FormData
from fastapi import UploadFile
from datetime import date

__all__ = ['form_field_as_file',
           'form_field_as_str',
           'is_valid_email',
           'is_valid_password',
           'make_test_regex_fn',
           'MIN_DATE']

MIN_DATE = date.fromisoformat('1800-01-01')

def is_valid_name(name: str):
    return all([len(parte) > 2 for parte in name.split()])

def form_field_as_str(form_data: FormData, field_name: str):
    field_value = form_data[field_name]
    if isinstance(field_value, str):
        return field_value
    raise TypeError(f'Form field {field_name} type is not str')

def form_field_as_file(form_data: FormData, field_name: str):
    field_value = form_data[field_name]
    if isinstance(field_value, UploadFile):
        return field_value
    raise TypeError(f'Form field {field_name} type is not UploadFile')

def is_valid_iso_date(iso_date: str):
    try:
        date.fromisoformat(iso_date)
    except ValueError:
        return False
    else:
        return True

def is_valid_birth_date(birth_date: str):
    return (is_valid_iso_date(birth_date) and 
            date.fromisoformat(birth_date) >= MIN_DATE)

def make_test_regex_fn(regex: str):
    compiled_regex  = re.compile(regex)
    def test_regex_fn(value: str):
        return bool(re.fullmatch(compiled_regex, value))
    return test_regex_fn

is_valid_email = make_test_regex_fn(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")

is_valid_password = make_test_regex_fn(r"[0-9a-zA-Z\$\#\?\.\!]{3,10}") # for testing purposes

def find_in(iterable: Iterable, predicate):
    return next((obj for obj in iterable if predicate(obj)), None)

# def find_in(iterable: Iterable, predicate):
#     for obj in iterable:
#         if predicate(obj):
#             return obj
#     return None