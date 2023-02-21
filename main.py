import translate
import re
import sys

original_file_name = 'auth.php'
if len(sys.argv)>=2:
    original_file_name = sys.argv[1]

with open(original_file_name, 'r') as f:
    php_text = f.read()

php_dict = {}
for match in re.finditer(r'\'([\w\s]*)\'\s*=>\s*\'([\w\s]*)\'', php_text):
    key = match.group(1)
    value = match.group(2)
    php_dict[key] = value

translator = translate.Translator(to_lang='ro')
for key, value in php_dict.items():
    translated_value = translator.translate(value)
    php_dict[key] = translated_value

result_file_name = 'output.php'
if len(sys.argv)>=3:
    result_file_name = sys.argv[2]

with open(result_file_name, 'w', encoding='utf-8') as f:
    f.write("<?php return [")
    for key, value in php_dict.items():
        f.write("'%s' => '%s', " % (key, value))
    f.write("];")

