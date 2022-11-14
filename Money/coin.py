class Coin:
    ten_cents = 10
    twenty_cents = 20
    fifty_cents = 50
    one_dollar = 100  # One dollar is treated as 100 cents

    def __init__(self, value):
        self.value = value

    # Validate the coin
    def validate_coin(self):
        if self.value == Coin.ten_cents or self.value == Coin.twenty_cents \
                or self.value == Coin.fifty_cents or self.value == Coin.one_dollar:
            return True
        else:
            return False
