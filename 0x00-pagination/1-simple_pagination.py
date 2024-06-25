#!/usr/bin/env python3

""" import typing annotation assistants
    CSV to read CSV files
    Math for mathematical calculations
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ return a tuple of number of data returned on a page query """
    new_page: int
    queries: int
    result: List = []
    if page == 1:
        new_page = 0
        queries = page_size
    elif page <= 0:
        return tuple(result)
    else:
        new_page = page_size * (page - 1)
        queries = page_size * page

    result.append(new_page)
    result.append(queries)
    return tuple(result)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ function to get the number of queries per page """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        page_index = index_range(page, page_size)
        result = self.dataset()
        (start, end) = page_index

        queries_cap = math.ceil(len(result) / page_size)
        if page >= queries_cap:
            return []
        else:
            return result[start: end]
