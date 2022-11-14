from Money.note import Note
from Money.coin import Coin
from Money.card import Card
from Items.item import Item
from VendingMachine.VendingMachine import VendingMachine

# Initial Balance in  the machine in order to dispense change when needed
initial_balance = {
    Note.twenty_dollars * 100: 10,
    Note.fifty_dollars * 100: 10,
    Coin.ten_cents: 20,
    Coin.one_dollar: 20,
    Coin.fifty_cents: 20,
    Coin.twenty_cents: 20,
}


# prices in cents (1 dollar = 100 Cents)
# One dollar is treated as 100 cent, other coins and notes are treated as expected.
initial_items_stock = [
    [Item(0, "Milky Bar", 300, 10),
     Item(1, "Oreo", 350, 10),
     Item(2, "m&ms", 100, 10),
     Item(3, "Twiks", 100, 10),
     Item(4, "KitKat", 100, 10)],
    [Item(5, "Rafaello", 200, 10),
     Item(6, "Snickers", 200, 10),
     Item(7, "Mars", 200, 10),
     Item(8, "Reese's", 400, 10),
     Item(9, "Clif Bar", 555, 10)],
    [Item(10, "Fanta", 100, 10),
     Item(11, "Sprite", 100, 10),
     Item(12, "Pepsi", 100, 10),
     Item(13, "Water", 50, 10),
     Item(14, "Coca Cola", 100, 10)],
    [Item(15, "Bavaria", 150, 10),
     Item(16, "Iced Tea", 150, 10),
     Item(17, "Mountain Dew", 200, 10),
     Item(18, "Lays", 60, 10),
     Item(19, "Doritos", 60, 10)],
    [Item(20, "Popcorn", 60, 10),
     Item(21, "Cheetos", 80, 10),
     Item(22, "Takis", 90, 10),
     Item(23, "Gum", 200, 10),
     Item(24, "Hand Sanitizer", 590, 10)]
]


def vend():
    machine = VendingMachine()
    for i in range(len(initial_items_stock)):
        for j in range(len(initial_items_stock[0])):
            machine.add_item(initial_items_stock[i][j], i, j)
    print('Welcome to the vending machine!\n***************')

    continue_to_buy = True
    while continue_to_buy:
        machine.show_items()
        selected_row = int(input('select item row: '))
        selected_col = int(input('select item column: '))

        if selected_col < VendingMachine.cols and selected_row < VendingMachine.rows:
            if machine.contains_item(selected_row, selected_col):
                item = machine.get_item(selected_row, selected_col)
                method = VendingMachine.show_payment_methods()
                if 3 >= method >= 1:
                    machine.insert_and_check_amount_for_item(item, method)
                    machine.buy_item(item)

                    a = input('buy something else? (y/n): ')
                    if a == 'n':
                        continue_to_buy = False
                        machine.check_refund()
                    else:
                        continue
                else:
                    print('Please Enter a valid choice.')
                    continue

            else:
                print('Item not available. Select another item.')
                continue
        else:
            print('Please enter a valid row and column.')
            continue

vend()

