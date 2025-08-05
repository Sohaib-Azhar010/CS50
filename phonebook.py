# phonebook = {
#     "Alice": "123-456-7890",
#     "Bob": "987-654-3210",
#     "Charlie": "555-123-4567"
# }

# name = input("Enter a name to search: ")

# if name in phonebook:
#     print(f"{name}'s number is {phonebook[name]}")
# else:
#     print(f"{name} is not in the phonebook.")

import re

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

# Normalize the phonebook: create lower-case keys and digits-only values
normalized_phonebook = {
    name.lower(): re.sub(r'\D', '', number)
    for name, number in phonebook.items()
}

# Reverse phonebook: numbers as keys, names as values
reverse_phonebook = {
    re.sub(r'\D', '', number): name
    for name, number in phonebook.items()
}

query = input("Enter a name or number to search: ").strip()

# Try to interpret input
if query.replace(" ", "").isalpha():  # likely a name
    key = query.lower()
    if key in normalized_phonebook:
        print(f"{query.title()}'s number is {phonebook[query.title()]}")
    else:
        print(f"{query} is not in the phonebook.")
else:  # likely a number
    digits_only = re.sub(r'\D', '', query)
    if digits_only in reverse_phonebook:
        found_name = reverse_phonebook[digits_only]
        print(f"The number belongs to {found_name}: {phonebook[found_name]}")
    else:
        print(f"No match found for number {query}.")
