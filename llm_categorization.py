import google.generativeai as genai

#reading key from local file
with open(r'/Users/mebin/Downloads/Work/Coding Projects/SECRETS/gemini-1.5Flash-APIKEY.txt') as f:
    api_key = f.read().strip()
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
category_string = "Healthcare,Finance,Shopping,Electronics,Food,Transport,Online Games, Sports, Lifestyle"
company_name = input("Enter company name:")
response = model.generate_content(f"{company_name}, the company, can be best categorised into which of the following categories: {category_string}. NOTE ONLY SINGLE ANSWER IS ACCEPTED, if it really does not fall into any reply with NONE")
print(response.text)