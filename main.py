import functions
import parameters

url = parameters.url
api_key = parameters.api_key

text_ex = functions.get_info_website(url, 200)
list_names = functions.extract_names(parameters.tryout_text) ### If you don't need to extract the text from some url, please skip function get_info_website and put your text directly here
print(list_names)
comments_per_name = functions.get_comments(parameters.tryout_text, list_names, api_key)

print(comments_per_name)
