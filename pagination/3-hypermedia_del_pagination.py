#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position (resilient to deletions)"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a deletion-resilient hypermedia page.
        """

        dataset = self.indexed_dataset()
        dataset_size = len(dataset)

        # default index
        if index is None:
            index = 0

        # validation
        assert isinstance(index, int) and 0 <= index < dataset_size

        data = []
        current = index
        count = 0

        # collect page_size valid elements
        while count < page_size and current < dataset_size:
            if current in dataset:
                data.append(dataset[current])
                count += 1
            current += 1

        next_index = current

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
