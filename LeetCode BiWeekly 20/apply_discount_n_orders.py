class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.per = 0
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.product = product
        self.amount = amount
        self.per += 1
        self.cost = 0
        for i in range(len(self.product)):
            j = self.products.index(self.product[i])
            self.cost += self.prices[j]*self.amount[i]
        if(self.per%self.n==0):
            self.cost -= ((self.discount * self.cost) / 100)
            return(self.cost)
        else:
            return(self.cost)
