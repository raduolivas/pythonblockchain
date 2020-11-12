blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """Append the new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount: the amount that should be added.
        :last_transaction: the last blockchain trnasaction.
    """
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount)
    as a float. """
    user_input = float(input('Your transaction amount please:'))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    print('-' * 30)
    for block in blockchain:
        print('outputting Block')
        print(block)
    else:
        print('-' * 30)


def verify_chain():
    # block_index = 0;
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add new transaction value')
    print('2: Output the blockchain blocks')
    print('h: manipulate the Chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain')
        break
else:
    print('User left')

print('Done')
