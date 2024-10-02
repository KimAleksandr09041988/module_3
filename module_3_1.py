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
    bool_ = False
    for item in list_to_search:
        if string_.lower() == item.lower():
            bool_ = True
    return  bool_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)