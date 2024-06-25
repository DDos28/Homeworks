calls = 0
def count_calls():
    global calls
    if (count_calls):
        calls += 1
    return calls

def string_info(str):
    print((len(str), str.upper(), str.lower()))
    count_calls()

def is_contains(str, list):
    str = str.lower()
    list = [x.lower() for x in list]
    if str in list:
        print(True)
    else:
        print(False)
    count_calls()

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycle', 'cyclic'])
print(calls)