#!/usr/bin/env python3
"""
Module qui contient la fonction index_range
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Retourne un tuple (start_index, end_index)
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
