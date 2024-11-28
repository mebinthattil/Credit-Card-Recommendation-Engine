'''
TODO:
1. Vendor can be part of a category as well --> requires fundamental change in thought process
2. REGEX pending for coupoun and cashback
3. Code cleanup for better readability and maintainability


'''




import helper

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
    
    def select_retailers_rewards(self, brand_or_category : str) -> str : 
        for retailer in self.select_retailers:
            if brand_or_category == retailer:
                return self.select_retailers[retailer]
        return False
    
    def categories_rewards(self, brand_or_category : str) -> str : 
        for category in self.categories:
            if brand_or_category == category:
                return self.categories[category]
        return False
    
    def other_rewards(self, brand_or_category : str) -> str : 
        for other in self.other:
            if brand_or_category == other:
                return self.other[other]   
        return False
    
    
list_of_cards = []
def construct_cards() -> None:
    for card in helper.json_to_nested_dict("cards.json"):
        #TODO: below line too complex, write cleaner code
        helper_list = helper.card_class_constructor(helper.json_to_nested_dict("cards.json")[card]["uid"])
        list_of_cards.append(Cards(
            uid=helper_list[0],
            card_name=card,
            name_on_card=helper_list[1],
            bank_name=helper_list[2],
            network=helper_list[3],
            type=helper_list[4],
            number=helper_list[5],
            expiry=helper_list[6],
            cvv=helper_list[7],
            NFC=helper_list[8],
            select_retailers=helper_list[9],
            categories=helper_list[10],
            other=helper_list[11]
            ))

construct_cards()

def best_reward_amount_for_card(list_of_cards : object , brand_or_category : str, purchase_amount : int) -> int :
        highest_reward = 0
        #iterate through all cards in wallet
        for card_object in list_of_cards:
            #iterate through all the individual reward statements, pass into the reward_value function then return the highest
            for vendor,reward_stmt in list(card_object.select_retailers.items()): #cycling through select retailers
                if vendor == brand_or_category:
                    highest_reward = max(highest_reward, helper.reward_value_with_reward_stmt(reward_statement=reward_stmt, purchase_amount=purchase_amount))
            
            for vendor,reward_stmt in list(card_object.categories.items()): #cycling through categories
                if vendor == brand_or_category:
                    highest_reward = max(highest_reward, helper.reward_value_with_reward_stmt(reward_statement=reward_stmt, purchase_amount=purchase_amount))
        return highest_reward

print(best_reward_amount_for_card(list_of_cards, "puma",7000))


        
