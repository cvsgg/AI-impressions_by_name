import functions
import parameters

url = parameters.url
api_key = parameters.api_key

text_ex = functions.get_info_website(url, 200)
list_names = functions.extract_names(text_ex)
print(list_names)
comments_per_name = functions.get_comments(text_ex, list_names, api_key)

get_dict = {
    f"{name}":f"{comments}"
    for name, comments in comments_per_name.items()
}
print(get_dict)
