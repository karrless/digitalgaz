"""
Этот модуль предназначен для компьютерного зрения
"""
from .dimension import get_dimension
from .number import get_number
from .process import process_image

__all__ = [
    'process_image',
    'get_dimension',
    'get_number'
]