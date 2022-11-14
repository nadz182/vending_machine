class Note:
    twenty_dollars = 20
    fifty_dollars = 50

    def __init__(self, value):
        self.value = value

    # Validate the Note
    def validate_note(self):
        if self.value == Note.fifty_dollars or self.value == Note.twenty_dollars:
            return True
        return False
