calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string_):
    count_calls()
    a = (len(string_), string_.upper(), string_.lower())
    return a

def is_contains(string_, list_to_search):
    count_calls()
    for item in list_to_search:
        if string_.lower() in item.lower():
            return True
        else:
            return False


string_1 = 'HeLlo'
list_ = ['hello', 'woRld']

print(is_contains(string_1, list_))
print(string_info('Hello'))
print(string_info('Hello'))
print(string_info('Hello'))
print(string_info('Hello'))
print(calls)