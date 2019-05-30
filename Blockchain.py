blockchain = []

# Read previous list value
def get_last_blockchain_value(name):
    if not name:
        return [0]
    else:
        return name[-1]


# Add a value to a list
def add_value(name, value):
    name.append([get_last_blockchain_value(name), value])

# Input value and loop until 0 is entered
amount = 1
while amount:
    amount = float(input("Enter the next transaction amount: "))
    if amount:
        add_value(blockchain, amount)

# Print Blockchain
print(blockchain)
