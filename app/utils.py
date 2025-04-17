from flask import flash

def validate_item_data(name, quantity, description):
    if not name or len(name) < 3:
        return False, "Item name must be at least 3 characters long."
    if quantity < 0:
        return False, "Quantity cannot be negative."
    if description and len(description) > 255:
        return False, "Description cannot exceed 255 characters."
    return True, ""

def format_item_data(item):
    return {
        "id": item.id,
        "name": item.name,
        "quantity": item.quantity,
        "description": item.description or "No description provided."
    }

def validate_form_data(form_data, required_fields):
    """
    Validate form data to ensure all required fields are present and not empty.
    :param form_data: The form data dictionary (e.g., request.form).
    :param required_fields: A list of required field names.
    :return: True if valid, False otherwise.
    """
    for field in required_fields:
        if not form_data.get(field):
            flash(f"The field '{field}' is required.", "error")
            return False
    return True  # Added this return statement for the valid case.

def format_currency(value):
    """
    Format a numeric value as currency.
    :param value: The numeric value to format.
    :return: A string formatted as currency (e.g., "$1,234.56").
    """
    return f"${value:,.2f}"