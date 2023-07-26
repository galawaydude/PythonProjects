import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
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

def check_winnings(columns, lines_bet, bet_amount, symbol_value):
    total_winnings = 0
    winning_lines = []
    for line in range(lines_bet):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            total_winnings += symbol_value[symbol] * bet_amount
            winning_lines.append(line + 1)

    return total_winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = [[], [], []]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit_amount():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines_to_bet():
    while True:
        lines_bet = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines_bet.isdigit():
            lines_bet = int(lines_bet)
            if 1 <= lines_bet <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and", MAX_LINES)
        else:
            print("Please enter a number.")
    return lines_bet


def get_bet_amount():
    while True:
        amount = input(f"What would you like to bet? (${MIN_BET}-${MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def spin(balance):
    lines_bet = get_number_of_lines_to_bet()
    while True:
        bet_amount = get_bet_amount()
        total_bet = bet_amount * lines_bet

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet_amount} on {lines_bet} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines_bet, bet_amount, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit_amount()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play or 'q' to quit: ")
        if answer.lower() == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
