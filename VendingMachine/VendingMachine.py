from collections import Counter

from Items.item import Item
from Money.card import Card
from Money.coin import Coin
from Money.note import Note


class VendingMachine:
    rows = 5
    cols = 5

    initial_balance = {
        Note.twenty_dollars * 100: 10,
        Note.fifty_dollars * 100: 10,
        Coin.ten_cents: 20,
        Coin.one_dollar: 20,
        Coin.fifty_cents: 20,
        Coin.twenty_cents: 20,
    }

    def __init__(self):
        self.amount = 0
        self.items = [[] for _ in range(VendingMachine.rows)]

    def add_item(self, item, r, c):
        self.items[r].append(item)

    def show_items(self):
        print('\nitems available \n***************')
        print('      col0     ||       col1    ||         col2    ||         col3     ||         col4')
        for i in range(len(self.items)):  # for each item in this vending machine
            for j in range(len(self.items[0])):
                if self.items[i][j].item_stock == 0:  # if the stock of this item is 0
                    self.items.remove(self.items[i][j], end=" ")  # remove this item from being displayed

        for i in range(len(self.items)):  # for each item in this vending machine
            print("row", i, end=" : ")
            for j in range(len(self.items[0])):
                print(self.items[i][j].item_name + ": " "$",
                      self.items[i][j].item_price / 100, end=" || ")  # otherwise print this item and show its price
            print()
        print('***************\n')

    def add_cash(self, money):
        self.amount = self.amount + money

    def buy_item(self, item):
        if self.amount < item.item_price:
            print('You can\'t buy this item. Insert more coins.')
        else:
            self.amount -= item.item_price
            item.item_stock -= 1  # Update the stock in the machine for this item
            item.update_stock(item.item_stock)

    def contains_item(self, r, c):
        if self.items[r][c].item_stock > 0:
            return True
        return False

    def get_item(self, r, c):
        if self.items[r][c].item_stock > 0:
            return self.items[r][c]
        return None

    def show_payment_methods():
        payment_method = int(input('Choose your payment: \n 1. Coin Cash \n 2. Note Cash \n 3. Card\n'))
        return payment_method

    def insert_and_check_amount_for_item(self, item, method):
        price = item.item_price
        total_amount = 0
        current_amount = 0

        if method == 1 or method == 2:
            while total_amount < price:
                current_amount = float(input('insert ' + str((price - total_amount) / 100) + ': '))
                if method == 1 and Coin(current_amount).validate_coin():  # Check validity of the coin
                    total_amount += current_amount
                    VendingMachine.initial_balance[current_amount] += 1  # Update the balance in the machine
                elif method == 2 and Note(current_amount).validate_note():  # Check validity of the note
                    total_amount += current_amount * 100
                    VendingMachine.initial_balance[current_amount * 100] += 1 # Update the balance in the machine
                else:
                    print("Invalid Money, Dispense: ", current_amount)
                self.amount = total_amount

        # check validity of the card number
        elif method == 3:
            card_number = input('Please Enter card Number: ')
            if Card(card_number).validate_card():
                self.amount = price
            else:
                print('Invalid Card Number')

    # Check if there's change should be refunded to the user
    def check_refund(self):
        if self.amount > 0:
            self.calculate_change(self.amount)
            self.amount = 0

        print('Thank you, have a nice day!\n')

    # Greedy approach to calculate the change should be dispensed to the user
    def calculate_change(self, value):
        sorted_balance = sorted(VendingMachine.initial_balance)
        n = len(sorted_balance)
        ans = Counter() # Counter dictionary
        for deno in sorted_balance:
            ans[deno] = 0
        i = n - 1
        while i >= 0:
            # Find denominations
            while value >= sorted_balance[i]:
                value -= sorted_balance[i]
                ans[sorted_balance[i]] += 1
                VendingMachine.initial_balance[sorted_balance[i]] -= 1
            i -= 1

        # Print result
        print("Refunded: ")
        for i in ans:
            if ans[i] > 0:
                print(i / 100, "$ : ", ans[i])
