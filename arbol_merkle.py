import hashlib

def calculate_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_tree(data_list):
    if len(data_list) == 1:
        return data_list[0]

    new_data_list = []

    for i in range(0, len(data_list) - 1, 2):
        combined_data = data_list[i] + data_list[i + 1]
        hash_combined = calculate_hash(combined_data)
        new_data_list.append(hash_combined)

    if len(data_list) % 2 != 0:
        new_data_list.append(data_list[-1])  # Add the last element if odd number of elements

    return build_merkle_tree(new_data_list)

# List of data items
data_items = [
    "Transaction1",
    "Transaction2",
    "Transaction3",
    "Transaction4",
    "Transaction5"
]

# Build the Merkle tree
root_hash = build_merkle_tree(data_items)
print("Root Hash:", root_hash)
