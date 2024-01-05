import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, # A appear 2 times
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def wish_player_luck():
    print("Welcome to the Slot Machine Game!")
    print("Best of luck! May the symbols align in your favor!\n")

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] # Add however many symbols we have above in this list
    for symbol, symbol_count in symbols.items(): # loop thru dictionary. Symbol -> "a", symbol_count -> 2
        for _ in range(symbol_count): # For "A", 2 times
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # make a copy of all_symbols using Slice operator[:] 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
    
        columns.append(column)
    return columns

def print_slot_machine(columns): # Transpose the Matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Amount must be 1-3")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("How much you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(F"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount   


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(F"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(F"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(F"You won ${winnings}.")
    print(F"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    wish_player_luck()  # Add a wish for good luck at the beginning
    balance = deposit()
    while True:
        print(F"Current balance is: ${balance}")
        answer = input("Press enter to play (Q to quit).")
        if answer == "Q":
            break
        balance += spin(balance)

    print(F"You left with ${balance}")

main()
