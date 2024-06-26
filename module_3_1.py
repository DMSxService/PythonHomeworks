calls = 0
def count_calls() :
    global calls
    calls = calls+1
    return calls
def string_info(string) :
    global calls
    calls = count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search) :
    global calls
    calls = count_calls()
    for i in range(len(list_to_search)):
        proof = string.upper() == list_to_search[i].upper()
        if proof:
            break
    return proof
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)