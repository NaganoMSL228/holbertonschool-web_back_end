#!/usr/bin/env python3
"""
Module qui contient la fonction index_range
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Retourne un tuple (start_index, end_index) correspondant
    à la plage d'index pour une pagination donnée.

    Args:
        page (int): numéro de la page (commence à 1)
        page_size (int): nombre d'éléments par page

    Returns:
        tuple: (start_index, end_index)
    """

    if page < 1 or page_size < 1:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


if __name__ == "__main__":
    print(index_range(1, 7))     # (0, 7)
    print(index_range(3, 15))    # (30, 45)