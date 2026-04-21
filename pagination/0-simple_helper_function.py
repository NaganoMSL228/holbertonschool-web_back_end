#!/usr/bin/env python3
"""
Module qui contient la fonction index_range
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Retourne un tuple (start_index, end_index)
    """

    return ((page - 1) * page_size, page * page_size)
