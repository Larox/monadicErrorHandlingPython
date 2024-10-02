# 🚀 Beyond Try-Except: Python's Frontier of Error Handling with Monads and Railway Magic

This repository includes the example used in PyCon ES 2024 talk and summarizes the two approaches to error handling in Python:

1. **Traditional Error Handling**: Using the LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission) paradigms.
2. **Monadic Error Handling**: Using the Results Monad to handle errors in a functional, structured, and maintainable way.

The examples showcase how monadic error handling can improve readability, maintainability, and error propagation when dealing with complex workflows.

---

## 🔍 What You'll Learn

1. **Traditional Error Handling**: Understand the pros and cons of **LBYL** and **EAFP** techniques.
2. **Monadic Error Handling**: Learn how to implement error handling using the **Results Monad**, which is a more functional approach to managing success and failure states in Python.
3. **Railway-Oriented Development**: See how **monadic chaining** keeps your success and error flows separate, resulting in cleaner and more maintainable code.
4. **Pattern Matching**: Leverage Python's pattern matching for concise and expressive error handling.

---

## 📂 Examples Structure

The repository contains two key files for comparison:

- **1. `lbyl_eafp_example.py`**:
  - Demonstrates the **LBYL** and **EAFP** error-handling methods.
  - This file uses try/except blocks and manual error checks to manage errors.
- **2. `result_monad_example.py`**:
  - Usage of [Result](https://github.com/rustedpy/result) library.
  - Refactors the same use case using the **Results Monad** to manage errors.
  - This file introduces functional error propagation using monads, along with Python's pattern matching for clean, concise handling of results.

---

## 🚀 Quick Overview

### Traditional Error Handling (`lvyl_eafp_example.py`)

```python
def validate_items(items: List[Item]) -> List[Item] | str:
    try:
        if not items:
            raise ValueError("Invalid items list")
        for item in items:
            if item.quantity <= 0:
                raise ValueError(f"Invalid quantity for item {item.name}")
        return items
    except ValueError as e:
        return f"Error: {str(e)}"
```

This approach uses manual error checks (`if/else`) and `try-except` blocks to manage failures.
While simple, it becomes unwieldy as complexity increases.

### Monadic Error Handling (`result_monad_example.py`)

```python
from result import Ok, Err

def validate_items(items: List[Item]) -> Result[List[Item], str]:
    if not items:
        return Err("Invalid items list")
    for item in items:
        if item.quantity <= 0:
            return Err(f"Invalid quantity for item {item.name}")
    return Ok(items)
```

Using the **Results Monad** allows you to propagate errors seamlessly,
and handle them in one place. This results in cleaner, more maintainable code.

---

## 💻 How to Run

1. Clone the repository

2. Install dependencies:

   You'll need the [`poetry`](https://python-poetry.org/)

   ```bash
   poetry install
   ```

3. Run the traditional error handling example:

   ```bash
   python lbyl_eafp_exampl.py
   ```

4. Run the monadic error handling example:

   ```bash
   python result_monad_example.py
   ```

---

## 🏆 Key Takeaways

### Traditional Error Handling (LBYL/EAFP):

- **Pros**: Simple and familiar for most Python developers.
- **Cons**: Leads to scattered error checks, hard-to-follow control flow, and code duplication in larger codebases.

### Monadic Error Handling with Results Monad:

- **Pros**:
  - Cleaner, more readable, and more maintainable code.
  - Error propagation is automatic and consistent.
  - Separate success and error flows following Railway-Oriented Development principles.
- **Cons**: Requires learning a new functional paradigm, though once adopted, it simplifies complex workflows significantly.

By comparing these two approaches, you'll see how the Results Monad can dramatically simplify error handling, especially as your project scales and grows in complexity.
