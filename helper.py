import regex,json,re

def json_to_nested_dict(json_file: str) -> dict:
    import json
    with open(json_file) as f:
        cards = json.load(f)

    cards = dict(cards)
    #converting to nested dictionary
    for i in cards:
        cards[i] = dict(cards[i])
        try: #this is to handle the case of rewards.json which has one more layer of nested dictionary.
            for j in i:
                cards[i][j] = dict(cards[i][j])
        except:
            continue
    
    return cards

def read_from_retailers_list_txt() -> list:
    fr = open("retailers_list.txt", "r")
    lines = fr.read().split(",")[:-1]
    fr.close()
    return lines

def append_to_retailers_list_txt(new_retailer : str = False) -> None:
    import helper
    reward_dict = helper.json_to_nested_dict("rewards.json")
    fw = open("retailers_list.txt", "a")
    for i in reward_dict:
        for j in reward_dict[i]["select_retailers"]:
            if j not in read_from_retailers_list_txt():
                fw.write(j+",")
    if new_retailer and new_retailer not in read_from_retailers_list_txt():
        fw.write(new_retailer+",")
    fw.close()

append_to_retailers_list_txt()
#card class constructor function. Input a card as dictionary, same structure as in json, converts to list with all the values.
def card_class_constructor(uid : int) -> list[str, str, str, str, str, str, int, str, int, bool, dict, dict, dict]:
    list_with_constructor_values = []

    #to add card details
    all_cards = json_to_nested_dict("cards.json")
    for card in all_cards:
        if all_cards[card]["uid"] == uid:
            break
    list_with_constructor_values += list(all_cards[card].values()) 

    #to add card rewards
    all_rewards = json_to_nested_dict("rewards.json")
    for card in all_rewards:
        if all_rewards[card]["uid"] == uid:
            break
    all_rewards[card].pop("uid")
    for type_of_reward in all_rewards[card]:
        list_with_constructor_values.append(all_rewards[card][type_of_reward])
    
    return list_with_constructor_values


    
def reward_type(reward_statement : str) -> str:
    if "off" in reward_statement.lower():
        return "percent off"
    
    elif "points" in reward_statement.lower():
        return "points"

    elif "cashback" in reward_statement.lower():
        return "cashback"

    elif "coupouns" in reward_statement.lower():
        return "coupons"

    else:
        return False


def reward_value_with_reward_stmt(reward_statement : str, purchase_amount : int, points_stmt : str = "1 points for every Rs.1 spent") -> int:
    if reward_type(reward_statement) == "percent off":
        return regex.regex_extract_reward_value_PERCENT_OFF(reward_statement, purchase_amount)

    elif reward_type(reward_statement) == "points":
        return regex.regex_extract_reward_value_POINTS(reward_statement, purchase_amount, points_stmt)
    
    elif reward_type(reward_statement) == "cashback":
        pass
        #cashback can have % or abs
    elif reward_type(reward_statement) == "coupons":
        pass
    else:
        return False


def correct_vendor_txn_name(vendor_txn_name : str) -> str: 
    #sometimes vendor txn name can be amzn can be amazon, zeptonow can be zepto, etc
    # we need to bring this to the original brand name in order to compare from data in the json rewards file
    #approach1: ollama
    #approach2: fuzzy search
    pass

def reward_value_for_vendor(reward_statement : str, purchase_amount : int) -> int:
    #here the challenge is that smth like apple can be an individual vendor or a category(electronics)
    #this is applicable for brands that are eligible under both conditions
    '''
    different types:
    <value> <% or Rs.> *off* [on condition] --> percent off
    <value> X *points* [on condition] --> points
    <value> % *cashback* [on condition] --> cashback
    <value> worth *coupouns* [on condition] --> coupons

    problem 1: regex identification
    '''
    #pass regex pertaining to reward_type
    pass
