# 0x01 Caching Project
`#Back-end`

## Overview

This project explores different caching algorithms and how they affect data retrieval and storage efficiency. Caching helps to improve the performance of applications by temporarily storing data, allowing for faster access. The project includes the implementation of various caching strategies such as FIFO, LIFO, LRU, and MRU.

## Learning Objectives

Upon completing this project, you should be able to:
- Understand what a caching system is and its purpose.
- Explain various cache replacement policies:
  - **FIFO** (First In, First Out)
  - **LIFO** (Last In, First Out)
  - **LRU** (Least Recently Used)
  - **MRU** (Most Recently Used)
  - **LFU** (Least Frequently Used)
- Identify the limitations and considerations when using a caching system.

## Project Structure

- **BaseCaching**: Parent class that defines a caching system structure, providing:
  - `cache_data`: Dictionary for storing cached data.
  - `MAX_ITEMS`: Maximum number of items allowed in the cache (default 4).
  - `put` and `get` methods, which must be implemented in child classes.

- **Caching Algorithms**:
  1. **BasicCache**: No limit on cache size; a basic dictionary cache.
  2. **FIFOCache**: Implements a First-In-First-Out (FIFO) policy, removing the oldest item when capacity is exceeded.
  3. **LIFOCache**: Implements a Last-In-First-Out (LIFO) policy, removing the most recent item when capacity is exceeded.
  4. **LRUCache**: Implements a Least Recently Used (LRU) policy, removing the least recently accessed item when capacity is exceeded.
  5. **MRUCache**: Implements a Most Recently Used (MRU) policy, removing the most recently accessed item when capacity is exceeded.
  
## Files

Each caching strategy is implemented as a separate Python file, inheriting from the `BaseCaching` class.

- **base_caching.py**: Defines the `BaseCaching` class, which child classes will extend.
- **0-basic_cache.py**: Implements a cache without any limit.
- **1-fifo_cache.py**: Implements a FIFO caching strategy.
- **2-lifo_cache.py**: Implements a LIFO caching strategy.
- **3-lru_cache.py**: Implements an LRU caching strategy.
- **4-mru_cache.py**: Implements an MRU caching strategy.

## Usage

Each cache class follows a similar structure and can be tested individually. Here is an example usage of `FIFOCache`:

```python
#!/usr/bin/env python3
from 1_fifo_cache import FIFOCache

cache = FIFOCache()
cache.put("A", "Hello")
cache.put("B", "World")
cache.put("C", "Holberton")
cache.put("D", "School")
cache.print_cache()  # Expected: A, B, C, D
cache.put("E", "Battery")  # Discards A
cache.print_cache()  # Expected: B, C, D, E
```

Each caching class includes:
- `put(key, item)`: Adds an item to the cache.
- `get(key)`: Retrieves an item from the cache, or `None` if the item is not present.

## Testing

To test each cache class, use the provided test files (e.g., `0-main.py`, `1-main.py`). These files demonstrate basic operations, including adding items to the cache and checking eviction behavior when the cache reaches its limit.

## Tasks

### Task 0: Basic Dictionary

**File:** `0-basic_cache.py`

Implement a `BasicCache` class inheriting from `BaseCaching`. This caching system has no limit on cache size.

- **put(key, item):** Adds an item to the cache dictionary.
- **get(key):** Retrieves an item from the cache dictionary by key.

### Task 1: FIFO Caching

**File:** `1-fifo_cache.py`

Implement a `FIFOCache` class using the First-In-First-Out caching algorithm.
- If the number of items in the cache exceeds `MAX_ITEMS`, discard the first added item and print `DISCARD: <key>`.

### Task 2: LIFO Caching

**File:** `2-lifo_cache.py`

Implement a `LIFOCache` class using the Last-In-First-Out caching algorithm.
- Discard the most recent item added when the cache exceeds `MAX_ITEMS` and print `DISCARD: <key>`.

### Task 3: LRU Caching

**File:** `3-lru_cache.py`

Implement an `LRUCache` class using the Least Recently Used caching algorithm.
- Discard the least recently accessed item when the cache exceeds `MAX_ITEMS` and print `DISCARD: <key>`.

### Task 4: MRU Caching

**File:** `4-mru_cache.py`

Implement an `MRUCache` class using the Most Recently Used caching algorithm.
- Discard the most recently accessed item when the cache exceeds `MAX_ITEMS` and print `DISCARD: <key>`.

### Task 5: LFU Caching `#Advanced`

**File:** `100-lfu_cache.py`

Implement an `LFUCache` class using the Least Frequently Used caching algorithm.
- Discard the least frequently used item when the cache exceeds `MAX_ITEMS` and print `DISCARD: <key>`.
