def json_to_nested_dict(json_file: str) -> dict:

    #reading from json
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
    
def regex_extract_reward_value(reward_statement : str, purchase_amount : int) -> int:
    if reward_type(reward_statement) == "percent off":
        return regex_extract_reward_value_PERCENT_OFF(reward_statement, purchase_amount)

    elif reward_type(reward_statement) == "points":
        pass
    elif reward_type(reward_statement) == "cashback":
        pass
    elif reward_type(reward_statement) == "coupons":
        pass
    else:
        return False


def reward_value(reward_statement : str) -> int:
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






#create regex func for extracting rewards json
