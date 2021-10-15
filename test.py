list_value = {}

list_value["1"] = "ankie"

print(list_value["1"])
try:
    print(list_value["2"])
except KeyError as e:
    print('I got a KeyError - reason "%s"' % str(e))