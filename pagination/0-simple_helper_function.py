bob@dylan:~$ cat 0-main.py
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

    start_index = (page - 1) * page_size

    end_index = page * page_size

    return (start_index, end_index)
