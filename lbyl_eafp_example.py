from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    price: int
    quantity: int


@dataclass
class User:
    user_id: int
    name: str


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


def calculate_total(items: List[Item]) -> int | str:
    try:
        total = sum(item.price * item.quantity for item in items)
        if total <= 0:
            raise ValueError("Total amount cannot be zero or negative")
        return total
    except ValueError as e:
        return f"Error: {str(e)}"


def process_payment(total: int) -> str:
    try:
        if total > 1000:
            raise RuntimeError("Payment exceeds the allowed limit")
        return f"Payment of ${total} processed "
    except RuntimeError as e:
        return f"Error: {str(e)}"


def process_order(items: List[Item]) -> int | str:
    validated_items = validate_items(items)
    if isinstance(validated_items, str):  # Error string returned
        return validated_items

    total = calculate_total(validated_items)
    if isinstance(total, str):  # Error string returned
        return total

    payment_result = process_payment(total)
    return payment_result


# Successful case - No Errors
print(process_order([Item("PyCon ES Ticket", 50, 2)]))

# Error case total is greater than limit
print(process_order([Item("PyCon ES Ticket", 50, 100)]))

# Error case quatity is 0 or less
print(process_order([Item("PyCon ES Ticket", 50, 0)]))

# Error case item list is empty
print(process_order([]))
