from thefuzz import process,fuzz
import helper

def fuzzy_search_test():

    collection = helper.read_from_retailers_list_txt()

    print("\nAMZN --> Amazon, few letters missing\n\n")
    print("Partial Ratio:", end = '')
    print(process.extract("amzn", collection, scorer=fuzz.partial_ratio, limit=4))
    print("Ratio:", end = '')
    print(process.extract("amzn", collection, scorer=fuzz.ratio, limit=4)) 
    print("Token Sort Ratio:", end = '')
    print(process.extract("amzn", collection, scorer=fuzz.token_sort_ratio, limit=8)) 
    print("Token Set Ratio:", end = '')
    print(process.extract("amzn", collection, scorer=fuzz.token_set_ratio, limit=8)) 
    print("Partial Token Sort Ratio:", end = '')
    print(process.extract("amzn", collection, scorer=fuzz.partial_token_sort_ratio, limit=8)) 
    print("Partial Token Set Ratio:", end = '')
    print(process.extract("amzn", collection, scorer=fuzz.partial_token_set_ratio, limit=8))



    print("\n\n\n\n\nzeptonow.inc --> zepto --> trailing company abbriviations\n\n")
    print("Partial Ratio:", end = '')
    print(process.extract("zeptonow.inc", collection, scorer=fuzz.partial_ratio, limit=4)) 
    print("Ratio:", end = '')
    print(process.extract("zeptonow.inc", collection, scorer=fuzz.ratio, limit=4)) 
    print("Token Sort Ratio:", end = '')
    print(process.extract("zeptonow.inc", collection, scorer=fuzz.token_sort_ratio, limit=8)) 
    print("Token Set Ratio:", end = '')
    print(process.extract("zeptonow.inc", collection, scorer=fuzz.token_set_ratio, limit=8)) 
    print("Partial Token Sort Ratio:", end = '')
    print(process.extract("zeptonow.inc", collection, scorer=fuzz.partial_token_sort_ratio, limit=8)) 
    print("Partial Token Set Ratio:", end = '')
    print(process.extract("zeptonow.inc", collection, scorer=fuzz.partial_token_set_ratio, limit=8))

    print("\n\n\n\n\nAMAZONAWS --> amazon web services\n\n")
    print("Partial Ratio:", end = '')
    print(process.extract("AMAZONAWS", collection, scorer=fuzz.partial_ratio, limit=4)) 
    print("Ratio:", end = '')
    print(process.extract("AMAZONAWS", collection, scorer=fuzz.ratio, limit=4)) 
    print("Token Sort Ratio:", end = '')
    print(process.extract("AMAZONAWS", collection, scorer=fuzz.token_sort_ratio, limit=8)) 
    print("Token Set Ratio:", end = '')
    print(process.extract("AMAZONAWS", collection, scorer=fuzz.token_set_ratio, limit=8)) 
    print("Partial Token Sort Ratio:", end = '')
    print(process.extract("AMAZONAWS", collection, scorer=fuzz.partial_token_sort_ratio, limit=8)) 
    print("Partial Token Set Ratio:", end = '')
    print(process.extract("AMAZONAWS", collection, scorer=fuzz.partial_token_set_ratio, limit=8))

    print("\n\n\n\n\One 97 Communications --> paytm\n\n") #fuzzy does horrible on this one, need to benchmark this with llama
    print("Partial Ratio:", end = '')
    print(process.extract("One 97 Communications", collection, scorer=fuzz.partial_ratio, limit=4)) 
    print("Ratio:", end = '')
    print(process.extract("One 97 Communications", collection, scorer=fuzz.ratio, limit=4)) 
    print("Token Sort Ratio:", end = '')
    print(process.extract("One 97 Communications", collection, scorer=fuzz.token_sort_ratio, limit=8)) 
    print("Token Set Ratio:", end = '')
    print(process.extract("One 97 Communications", collection, scorer=fuzz.token_set_ratio, limit=8)) 
    print("Partial Token Sort Ratio:", end = '')
    print(process.extract("One 97 Communications", collection, scorer=fuzz.partial_token_sort_ratio, limit=8)) 
    print("Partial Token Set Ratio:", end = '')
    print(process.extract("One 97 Communications", collection, scorer=fuzz.partial_token_set_ratio, limit=8))

