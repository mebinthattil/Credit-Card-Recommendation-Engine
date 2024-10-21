class Cards():
    def __init__(self, uid, card_name, name_on_card, bank_name, network, type, number, expiry, cvv, NFC, select_retailers,categories,other):
        #card details
        self.uid : str = uid
        self.card_name : str = card_name 
        self.name_on_card : str = name_on_card
        self.bank_name : str = bank_name
        self.network : str = network
        self.type : str = type
        self.number : int = number
        self.expiry : str = expiry
        self.cvv : int = cvv
        self.NFC : bool = NFC

        #rewards
        self.select_retailers : dict  = select_retailers
        self.categories : dict = categories
        self.other : dict = other
    
    def select_retailers_rewards(self, brand_or_category : dict):
        for retailers in self.select_retailers:
            if brand_or_category == retailers:
                return self.select_retailers[retailers]
        return False




        
