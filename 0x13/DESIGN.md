
# Menu-Driven Calculator 

## 1. Purpose

The Menu-Driven Calculator is a three-layer program that allows a user to select an arithmetic operation, enter numbers, perform the calculation, and view the result.

The program uses a `main()` function as its entry point and separates responsibilities into three layers.

---
## 2. Three-Layer Architecture

### Layer 1 — Presentation Layer

Responsible for communication with the user.

Functions:
- `show_menu()`
- `get_choice()`
- `get_numbers()`
- `display_result()`

### Layer 2 — Application Layer

Responsible for controlling the program flow.

Functions:
- `main()`
- `process_choice()`

### Layer 3 — Calculation Layer

Responsible for performing mathematical calculations.

Functions:
- `add()`
- `subtract()`
- `multiply()`
- `divide()`

---