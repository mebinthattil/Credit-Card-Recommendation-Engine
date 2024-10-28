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

    print("\n\n\n\nOne 97 Communications --> paytm\n\n") #fuzzy does horrible on this one, need to benchmark this with llama
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
#fuzzy_search_test()

def custom_test_case_fuzzy(abbriviated_name,actual_name):
    abbriviated_name,actual_name = abbriviated_name.lower(),actual_name.lower()
    print(f"Simple ratio similarity score: {fuzz.ratio(abbriviated_name, actual_name)}")
    print(f"Simple partial ratio similarity score: {fuzz.partial_ratio(abbriviated_name, actual_name)}")
    print(f"Simple token sort ratio similarity score: {fuzz.token_sort_ratio(abbriviated_name, actual_name)}")
    print(f"Simple token set ratio similarity score: {fuzz.token_set_ratio(abbriviated_name, actual_name)}")
    print(f"Simple partial token sort ratio similarity score: {fuzz.partial_token_sort_ratio(abbriviated_name, actual_name)}")
    print(f"Simple partial token set ratio similarity score: {fuzz.partial_token_set_ratio(abbriviated_name, actual_name)}")

def custom_avg_fuzzy(abbriviated_name,actual_name):
    collection = helper.read_from_retailers_list_txt()

    abbriviated_name,actual_name = abbriviated_name.lower(),actual_name.lower()
    print(f"\n{abbriviated_name} --> {actual_name}\n\n")
    l_partial_ratio = dict(process.extract(abbriviated_name, collection, scorer=fuzz.partial_ratio, limit= 200))
    l_ratio = dict(process.extract(abbriviated_name, collection, scorer=fuzz.ratio, limit= 200)) 
    l_averaged = []
    for i in collection:
        l_averaged.append(( ((l_partial_ratio[i]+l_ratio[i])/2)  ,i ))
    l_averaged = sorted(l_averaged, reverse=True)
    l_return = [(j,i) for i,j in l_averaged]
    return l_return

print(custom_avg_fuzzy('HPE','Hewlett-Packard Enterprise'))

def benchmarking_custom_avg_fuzzy():
    print(custom_avg_fuzzy('amzn','amazon'))
    print(custom_avg_fuzzy('zeptonow.inc','zepto'))
    print(custom_avg_fuzzy('amazonaws','amazon web services'))
    print(custom_avg_fuzzy('one 97 communications','paytm'))
    print(custom_avg_fuzzy('apple ME','apple'))
    print(custom_avg_fuzzy('next billion tech','groww'))

