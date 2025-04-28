class Account:
    def __init__(self, account_id):
        self.account_id = account_id

    def __str__(self):
        return self.account_id
    
account = Account("f7jvh27")
print(account)