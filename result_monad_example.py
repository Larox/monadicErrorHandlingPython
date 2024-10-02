from dataclasses import dataclass
from typing import List
from result import Result, Ok, Err


@dataclass
class Item:
    name: str
    price: int
    quantity: int


@dataclass
class User:
    user_id: int
    name: str


def validate_items(items: List[Item]) -> Result[List[Item], str]:
    if not items:
        return Err("Invalid items list")
    for item in items:
        if item.quantity <= 0:
            return Err(f"Invalid quantity for item {item.name}")
    return Ok(items)


def calculate_total(items: List[Item]) -> Result[int, str]:
    total = sum(item.price * item.quantity for item in items)
    if total <= 0:
        return Err("Total amount cannot be zero or negative")
    return Ok(total)


def process_payment(total: int) -> Result[str, str]:
    if total > 1000:
        return Err("Payment exceeds the allowed limit")
    return Ok(f"Payment of ${total} processed")


def process_order(items: List[Item]) -> str:
    result = validate_items(items).and_then(calculate_total).and_then(process_payment)

    # Pattern matching to handle the final Result
    match result:
        case Ok(value):
            return value
        case Err(error):
            return f"Processing error: {error}"


# Successful case - No Errors
print(process_order([Item("PyCon ES Ticket", 50, 2)]))

# Error case total is greater than limit
print(process_order([Item("PyCon ES Ticket", 50, 100)]))

# Error case total is greater than limit
print(process_order([Item("PyCon ES Ticket", 50, 0)]))

# Error case item list is empty
print(process_order([]))
