import helper

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