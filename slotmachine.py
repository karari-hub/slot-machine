#importing packages 
import random


#getting input 
max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_value = {
    "A":2,
    "B":3,
    "C":4,
    "D":6
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines=[]

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line +1)
    
    return winnings, winning_lines
                


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    #transposing
    for row in range (len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) -1:
                print(column[row], end=' | ')
            else:
                print(column[row],end='')

        print()        


def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('please enter a number.')
    
    return amount

def get_number_of_lines():
        while True:
            lines = input('Enter the  number of lines to bet on (1-' + str(max_lines)+')?')
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= max_lines:
                    break
                else:
                    print('Amount must be greater than 0.')
            else:
                print('please enter a number.')
    
        return lines


def get_bet():
    while True:
        amount = input('what would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f'Amount must be between ${min_bet} - ${max_bet}')
        else:
            print('Please enter a number.')
    
    return amount

def spin (balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines 

        if total_bet > balance:
            print(f'You do not have enough to bet that amount. Your current balance is ${balance}')
        else:
            break
    
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ')

    slots = get_slot_machine_spin(rows, cols, symbol_value)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'YOU WON ${winnings}')
    print(f'YOU WON ON LINES:', *winnings_lines)

    return winnings - total_bet


def main():
    balance= deposit()
    while True:
        print(f'current balance is ${balance}')
        answer = input('Press enter to play (q to quit).')
        if answer == "q":
            break
        balance += spin(balance)

    print(f'you left with ${balance}')

main()



    