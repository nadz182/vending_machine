class Item:

    def __int__(self):
        pass

    def __init__(self, item_id=None, item_name=None, item_price=None, item_stock=None):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.item_stock = item_stock

    def update_stock(self, stock):
        self.item_stock = stock

    def buy_from_stock(self):
        if self.item_stock == 0:  # if there is no items available
            print('Item not available')

        self.stock -= 1  # else stock of item decreases by 1
