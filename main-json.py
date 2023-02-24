import translate
import json
import sys

original_file_name = 'auth.json'
if len(sys.argv)>=2:
    original_file_name = sys.argv[1]

with open(original_file_name, 'r') as f:
    json_text = f.read()

# Load the JSON data into a dictionary
json_dict = json.loads(json_text)

# Translate values in the dictionary from English to Romanian
translator = translate.Translator(to_lang='ro')
for key, value in json_dict.items():
    translated_value = translator.translate(value)
    json_dict[key] = translated_value

result_file_name = 'output.json'
if len(sys.argv)>=3:
    result_file_name = sys.argv[2]

with open(result_file_name, 'w', encoding='utf-8') as f:
    json.dump(json_dict, f, ensure_ascii=False, indent=4)
