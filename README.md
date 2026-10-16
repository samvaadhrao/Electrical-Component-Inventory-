# Electrical Component Inventory System

**IE-Mechatronics Club — AI & Development Taskphase**

## Overview
A beginner-friendly, menu-driven Python application for keeping track of electrical and electronic components. It can be used for a small lab, electronics workbench, or student project.

## Features
- Add components with a unique ID, name, category, quantity, storage location, and optional notes.
- View the complete inventory and total units in stock.
- Search by component ID, name, or category.
- Add to or remove from stock, with checks against negative stock.
- Remove a component record with confirmation.
- Find components at or below a chosen stock threshold.
- Save records in a CSV file that persists between runs.
- Handle invalid numeric input and common file errors.

## Requirements
- Python 3.9 or newer recommended.
- No third-party packages are required.

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

4. Choose an option from the menu.
5. The program creates `inventory.csv` when a record is first saved.

## Example component records
| Component ID | Name | Category | Quantity | Location | Notes |
|---|---|---|---:|---|---|
| RES-001 | 220 Ohm Resistor | Resistor | 100 | Box A1 | 1/4 W |
| CAP-001 | 100 uF Capacitor | Capacitor | 25 | Box A2 | 25 V |
| LED-001 | Red LED | LED | 40 | Box B1 | 5 mm |
| DIO-001 | 1N4007 Diode | Diode | 20 | Box B2 | Rectifier |

These are sample records only; enter real quantities and locations for your own inventory.

## Python concepts demonstrated
- Variables, strings, integers, lists, and dictionaries
- `if` / `elif` / `else` conditionals
- `while` and `for` loops
- Functions and return values
- List comprehensions and searching
- File handling with `with open(...)`
- CSV reading and writing with Python's standard library
- Exception handling with `try` / `except`
- Input validation and simple program decomposition

## Suggested manual tests
1. Add a component with a new ID and verify that it appears in the inventory.
2. Try to add another component using the same ID; it should be rejected.
3. Search by a name fragment and by category.
4. Add stock and confirm that the quantity increases.
5. Remove fewer units than are available and confirm that the quantity decreases.
6. Attempt to remove more units than are available; the program should reject it.
7. Enter letters when asked for a quantity; the program should ask again.
8. Exit and restart the program; saved records should still be available.
9. Try the low-stock filter with a chosen threshold.

## Limitations and possible future improvements
This is a local, single-user, command-line application. Future improvements could include editing component details, exporting reports, a graphical interface, user accounts, and database support.

## Author
Samvaadh Rao
