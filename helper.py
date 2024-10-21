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
    else:
        print("Card with specified uid not found")
    list_with_constructor_values += list(all_cards[card].values()) 

    #to add card rewards
    all_rewards = json_to_nested_dict("rewards.json")
    for card in all_rewards:
        if all_rewards[card]["uid"] == uid:
            break    
    else:
        print("No rewards found for card with specified uid")
    all_rewards[card].pop("uid")
    for type_of_reward in all_rewards[card]:
        list_with_constructor_values.append(all_rewards[card][type_of_reward])
    
    return list_with_constructor_values

print(card_class_constructor("CITI_A1"))






#create regex func for extracting rewards json
