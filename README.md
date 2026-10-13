**# PLP Python Week 7 Assignment**



**## Files**



**- `list\_warmup.py`: Demonstrates list indexing, adding and removing items, and counting items.**

**- `shopping\_list.py`: Provides an interactive shopping list manager to add, remove, and show items.**

**- `list\_report.py`: Prints a numbered shopping list, counts item names longer than four characters, and finds the longest name.**



**## Why check `in` before `.remove()`?**



**Checking whether an item is in the list before removing it makes the program safer. If an item is missing, `.remove()` raises a `ValueError`, which can stop the program. Using `in` first allows the program to display a helpful message instead.**

