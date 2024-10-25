# 0x00. Pagination Project
`#Back-end`

This project is focused on implementing pagination techniques in a backend application using Python. The project covers simple pagination, hypermedia pagination, and deletion-resilient pagination, using a dataset of popular baby names to demonstrate the various methods.

## Project Overview

The goal of this project is to learn and implement several pagination techniques, including:

1. Simple pagination with page and page size parameters.
2. Hypermedia pagination with metadata.
3. Deletion-resilient pagination to handle data changes between requests.

Each part of this project builds upon the last, moving from basic to more advanced pagination techniques to ensure a comprehensive understanding of REST API pagination.

## Project Requirements

- **Environment:** Ubuntu 18.04 LTS, Python 3.7
- **Style:** Code must follow the `pycodestyle` (version 2.5.) style guide.
- **Documentation:** All modules, functions, and classes require comprehensive docstrings.
- **Type Annotations:** All functions and coroutines must be type-annotated.

## Files in This Project

- **0-simple_helper_function.py:** Contains a helper function `index_range` that calculates the start and end indexes for paginating a dataset.
- **1-simple_pagination.py:** Contains the `Server` class and a `get_page` method to return a paginated dataset based on page and page size.
- **2-hypermedia_pagination.py:** Adds the `get_hyper` method to the `Server` class for hypermedia pagination with metadata.
- **3-hypermedia_del_pagination.py:** Implements a `get_hyper_index` method to provide deletion-resilient pagination.

## Project Tasks

### Task 0: Simple Helper Function

Defines the `index_range` function that calculates and returns a tuple representing the start and end index for pagination based on a given page and page size.

### Task 1: Simple Pagination

Implements a basic pagination method in the `Server` class that:

- Reads data from `Popular_Baby_Names.csv`.
- Returns a specified page of data based on `page` and `page_size` parameters.

### Task 2: Hypermedia Pagination

Extends pagination to include hypermedia metadata by adding the `get_hyper` method:

- Provides additional details, such as `page_size`, `page`, `next_page`, `prev_page`, and `total_pages`.
- Ensures response is in dictionary format, allowing clients to understand the pagination context.

### Task 3: Deletion-Resilient Pagination

Implements the `get_hyper_index` method for a more robust pagination approach:

- Ensures the correct data is displayed even if rows are deleted from the dataset between requests.
- Returns metadata such as `index`, `next_index`, `page_size`, and `data` to prevent missing items in paginated data.

## Usage

The code can be executed in the terminal with the following commands:
```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
```

Each of these main files tests a specific task in the mains directory.
