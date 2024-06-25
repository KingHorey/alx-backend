#!/usr/bin/env python3

""" import typing annotation assistants """
from typing import Tuple, List


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
