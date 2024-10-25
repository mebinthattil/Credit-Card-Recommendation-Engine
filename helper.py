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

def PPR_calculator_with_stmt(reward_statement:str) -> int: 
    import re

    pattern = r"(\d+)\s*points\s*(for\s*every|per)\s*Rs\.*\s*(\d+)"

    # Search for a match
    match = re.search(pattern, reward_statement)
    if match:
        points = int(match.group(1))  # Extracts the points value
        amount = int(match.group(3))  # Extracts the Rs amount
        return (points/amount)
    else:
        return 0

    
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

def regex_extract_reward_value_PERCENT_OFF(reward_statement : str, purchase_amount : int) -> int:
    #TODO: currently only condition where value is extractable and logic is understood is 'orders above Rs.X'. Expand to more generic cases like 'first 3 orders'
    import re

    # Any numeric value followed by % or Rs followed by mandatory "off" and optional condition for the discount
    pattern = r"(\d+)\s*(%|Rs)\s*off\s*(on\sorders\sabove\sRs\.\s*(\d+))?"

    match = re.search(pattern, reward_statement)
    if match:
        value = match.group(1)  # Extracts the numeric value
        unit = match.group(2)   # Extracts % or Rs
        condition = match.group(3) if match.group(3) else None  # Extracts the condition or "No condition"
        amount_in_condition = match.group(4) if match.group(4) else None  # Extracts the amount from the condition

        def calc_abs_value(value, unit):
            if unit == "Rs":
                return int(value)
            elif unit == "%": 
                return purchase_amount * (int(value)/100)

        if not condition: #no conditions just return the reward
            return calc_abs_value(value, unit)
        elif condition: #if condition exists check if eligible then return reward
            if purchase_amount > int(amount_in_condition):
                return calc_abs_value(value, unit)
            else:
                return 0
        else:
            print("error with condition valuation ; regex percent off")
            return 0

    else:
        print("percent_off regex failed")
        return 0
    
def regex_extract_reward_value_POINTS(reward_statement : str, purchase_amount : int, points_stmt : str) -> int:
    #example function call: regex_extract_reward_value_POINTS("5 X points on purchases above Rs. 2000",6000, "100 points for every Rs.1000 spent")
    import re
    pattern = r"(\d+)\s*(X)?\s*points\s*(on\s.*Rs\.\s*(\d+))?"

    match = re.search(pattern, reward_statement)
    if match:
        value : int = int(match.group(1))  # Extracts the numeric value
        multiplier : bool = True if match.group(2) else False  # Checks if 'X' (times) is present
        condition : str = match.group(3) if match.group(3) else None  # Extracts the condition or sets "No condition"
        condition_amount :int = int(match.group(4)) if match.group(4) else 0
        # Print the extracted variables
        print(f"Value: {value}")
        print(f"Multiplier: {multiplier}")
        print(f"Condition: {condition_amount}\n")
        if condition:
            if purchase_amount > condition_amount:
                if multiplier:
                    return purchase_amount * PPR_calculator_with_stmt(points_stmt) * value #reward is calculated by amount* PPR * multiplier value, eg 2000 * 0.1 * 2
                else:
                    return value * PPR_calculator_with_stmt(points_stmt) #constant points earned, which is then converted to equivalent Rs.

    else:
        print(f"points regex failed")

def reward_value_with_reward_stmt(reward_statement : str, purchase_amount : int, points_stmt : str = "1 points for every Rs.1 spent") -> int:
    if reward_type(reward_statement) == "percent off":
        return regex_extract_reward_value_PERCENT_OFF(reward_statement, purchase_amount)

    elif reward_type(reward_statement) == "points":
        return regex_extract_reward_value_POINTS(reward_statement, purchase_amount, points_stmt)
    
    elif reward_type(reward_statement) == "cashback":
        pass
        #cashback can have % or abs
    elif reward_type(reward_statement) == "coupons":
        pass
    else:
        return False

print(reward_value_with_reward_stmt("10% off on orders above Rs.5000",20000))

def correct_vendor_txn_name(vendor_txn_name : str) -> str:
    #sometimes vendor txn name can be amzn can be amazon, zeptonow can be zepto, etc
    # we need to bring this to the original brand name in order to compare from data in the json rewards file
    #approach1: ollama
    #approach2: fuzzy search
    pass

def reward_value_with_vendor(reward_statement : str) -> int:
    #here the challenge is that smth like apple can be an individual vendor or a category(electronics)
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
