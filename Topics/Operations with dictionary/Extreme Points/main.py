import json
# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
minimum_key = min(test_dict, key=test_dict.get)
maximum_key = max(test_dict, key=test_dict.get)

print(f'''min: {minimum_key}
max: {maximum_key}''')

