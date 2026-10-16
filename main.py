"""
Electrical Component Inventory System
IE-Mechatronics AI & Development Taskphase

A menu-driven inventory manager using Python fundamentals and CSV file handling.
Only Python's standard library is required.
"""

import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("inventory.csv")
FIELDS = ["component_id", "name", "category", "quantity", "location", "notes"]


def load_inventory():
    """Load inventory records from the CSV file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except (OSError, csv.Error) as error:
        print(f"Could not read inventory file: {error}")
        return []


def save_inventory(inventory):
    """Save all inventory records to the CSV file."""
    try:
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(inventory)
        return True
    except (OSError, csv.Error) as error:
        print(f"Could not save inventory: {error}")
        return False


def get_non_empty(prompt):
    """Ask until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_non_negative_integer(prompt, allow_zero=True):
    """Read a valid non-negative integer from the user."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0 or (not allow_zero and value == 0):
                print("Enter a valid positive quantity." if not allow_zero
                      else "Enter zero or a positive whole number.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number, such as 10.")


def display_inventory(inventory):
    """Display all inventory records in a readable format."""
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n" + "=" * 100)
    print(f"{'ID':<12} {'Name':<22} {'Category':<18} {'Qty':>6}  {'Location':<16} Notes")
    print("-" * 100)
    for item in inventory:
        print(
            f"{item['component_id']:<12} "
            f"{item['name'][:21]:<22} "
            f"{item['category'][:17]:<18} "
            f"{item['quantity']:>6}  "
            f"{item['location'][:15]:<16} "
            f"{item['notes']}"
        )
    print("=" * 100)
    print(f"Number of different component records: {len(inventory)}")
    print(f"Total units in stock: {sum(int(item['quantity']) for item in inventory)}")


def add_component(inventory):
    """Add a new component, requiring a unique component ID."""
    print("\n--- Add Component ---")
    component_id = get_non_empty("Component ID (e.g. RES-001): ").upper()

    if any(item["component_id"].upper() == component_id for item in inventory):
        print("That component ID already exists. Use Update Stock to change quantity.")
        return

    name = get_non_empty("Component name: ")
    category = get_non_empty("Category (e.g. resistor, capacitor, sensor): ")
    quantity = get_non_negative_integer("Quantity in stock: ")
    location = get_non_empty("Storage location (e.g. Box A2): ")
    notes = input("Notes/value/specification (optional): ").strip()

    inventory.append({
        "component_id": component_id,
        "name": name,
        "category": category,
        "quantity": str(quantity),
        "location": location,
        "notes": notes,
    })

    if save_inventory(inventory):
        print(f"Added {name} ({component_id}) to the inventory.")


def search_components(inventory):
    """Search records by component ID, name, or category."""
    query = input("\nEnter an ID, name, or category to search: ").strip().lower()
    if not query:
        print("Search cannot be empty.")
        return

    matches = [
        item for item in inventory
        if query in item["component_id"].lower()
        or query in item["name"].lower()
        or query in item["category"].lower()
    ]
    display_inventory(matches)


def update_stock(inventory):
    """Increase or decrease a component's stock quantity."""
    print("\n--- Update Stock ---")
    component_id = get_non_empty("Enter component ID: ").upper()
    item = next(
        (entry for entry in inventory if entry["component_id"].upper() == component_id),
        None
    )

    if item is None:
        print("Component ID not found.")
        return

    print(f"{item['name']} currently has {item['quantity']} unit(s).")
    print("1. Add stock")
    print("2. Remove stock")
    choice = input("Choose an option: ").strip()
    amount = get_non_negative_integer("Quantity to change (must be greater than 0): ",
                                      allow_zero=False)
    current = int(item["quantity"])

    if choice == "1":
        item["quantity"] = str(current + amount)
    elif choice == "2":
        if amount > current:
            print("Cannot remove more units than are currently in stock.")
            return
        item["quantity"] = str(current - amount)
    else:
        print("Invalid option. No changes made.")
        return

    if save_inventory(inventory):
        print(f"Updated stock. New quantity: {item['quantity']}")


def remove_component(inventory):
    """Remove a record after asking for confirmation."""
    print("\n--- Remove Component Record ---")
    component_id = get_non_empty("Enter component ID to remove: ").upper()
    item = next(
        (entry for entry in inventory if entry["component_id"].upper() == component_id),
        None
    )

    if item is None:
        print("Component ID not found.")
        return

    confirm = input(
        f"Remove {item['name']} ({component_id}) from the inventory? Type YES to confirm: "
    ).strip()
    if confirm == "YES":
        inventory.remove(item)
        if save_inventory(inventory):
            print("Component record removed.")
    else:
        print("Removal cancelled.")


def show_low_stock(inventory):
    """List records at or below a user-selected stock threshold."""
    threshold = get_non_negative_integer("Show components with quantity at or below: ")
    matches = [item for item in inventory if int(item["quantity"]) <= threshold]
    print(f"\nComponents with {threshold} or fewer unit(s):")
    display_inventory(matches)


def show_menu():
    print("\n" + "=" * 42)
    print(" ELECTRICAL COMPONENT INVENTORY SYSTEM")
    print("=" * 42)
    print("1. View all components")
    print("2. Add a component")
    print("3. Search components")
    print("4. Update stock quantity")
    print("5. Remove a component record")
    print("6. Show low-stock components")
    print("7. Exit")


def main():
    inventory = load_inventory()
    print("Welcome to the Electrical Component Inventory System!")
    print(f"Loaded {len(inventory)} component record(s).")

    while True:
        show_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            add_component(inventory)
        elif choice == "3":
            search_components(inventory)
        elif choice == "4":
            update_stock(inventory)
        elif choice == "5":
            remove_component(inventory)
        elif choice == "6":
            show_low_stock(inventory)
        elif choice == "7":
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
