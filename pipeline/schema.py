class TransactionRecord:
    """A single, Valid retail transaction"""
    def __init__(self, branch_id, transaction_date,Customer_tier, item_count, revenue):
        self.branch_id = branch_id
        self.transaction_date = transaction_date
        self.customer_tier = Customer_tier
        self.item_count = item_count
        self.revenue = revenue


class Branch:
    """Holds all the transactions that belongs to one branch """
    def __init__(self, branch_id):
        self.branch_id = branch_id
        self.transactions = [] 

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    @property
    def total_revenue(self):
        return sum(t.revenue for t in self.transactions)
    