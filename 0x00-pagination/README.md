# 0x00-pagination

This directory contains a series of Python scripts designed to implement pagination for a dataset of popular baby names. The main focus is to handle pagination in a way that is resilient to data deletions and provides hypermedia metadata to clients. The following tasks are included in this directory:

## Tasks

### Task 0: Simple Helper Function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`. The function returns a tuple of size two containing the start index and the end index for those pagination parameters. The page numbers are 1-indexed.

- **File:** `0-simple_helper_function.py`
- **Function:** `index_range`

### Task 1: Simple Pagination

Implement a method named `get_page` in the `Server` class that takes two integer arguments `page` and `page_size` with default values of 1 and 10, respectively. The method returns the appropriate page of the dataset.

- **File:** `1-simple_pagination.py`
- **Class:** `Server`
- **Method:** `get_page`

### Task 2: Hypermedia Pagination

Implement a method named `get_hyper` in the `Server` class that takes the same arguments as `get_page` and returns a dictionary containing the current page, page size, dataset page, and metadata for navigation.

- **File:** `2-hypermedia_pagination.py`
- **Class:** `Server`
- **Method:** `get_hyper`

### Task 3: Deletion-Resilient Pagination

Implement a method named `get_hyper_index` in the `Server` class that provides deletion-resilient pagination. The method should ensure that the user does not miss items when changing pages even if rows are removed between queries.

- **File:** `3-hypermedia_del_pagination.py`
- **Class:** `Server`
- **Method:** `get_hyper_index`

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the folder is mandatory.
- Code should use the `pycodestyle` style (version 2.5.*).
- The length of files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- All functions and coroutines must be type-annotated.

## Usage

### Running the Scripts

To run the scripts, you can use the following commands:

```bash
# Run task 0
python3 0-main.py

# Run task 1
python3 1-main.py

# Run task 2
python3 2-main.py

# Run task 3
python3 3-main.py
```

### Sample Output

The provided main files demonstrate how to use the implemented functions and classes. The output of these scripts should match the expected results shown in the task descriptions.

## Data File

The dataset used in these tasks is stored in the file `Popular_Baby_Names.csv`. It contains the popular baby names data, which will be used for pagination purposes.

## Main Test Files

- [0-main.py](0-main.py)
- [1-main.py](1-main.py)
- [2-main.py](2-main.py)
- [3-main.py](3-main.py)