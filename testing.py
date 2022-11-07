import requests

url = 'http://api.duckduckgo.com/?q=presidents of the united states&format=json'


response = requests.get(url)
answer = response.json()

president = answer["RelatedTopics"]


#print(president)

result = president[0]
#print(type(result))

#for i in president:
 #   print(i)
 #   if 'Lincoln' in i['Text']:
 #      print(True)


def test_lincoln():
    answer = False
    for i in president:
        if 'Lincoln' in i['Text']:
            answer = True
    assert answer

def test_jackson():
    answer1 = False
    for i in president:
        if 'Jackson' in i['Text']:
            answer1 = True
    assert answer1

def test_johnson():
    answer1 = False
    for i in president:
        if 'Johnson' in i['Text']:
            answer1 = True
    assert answer1

def test_obama():
    answer1 = False
    for i in president:
        if 'Obama' in i['Text']:
            answer1 = True
    assert answer1

def test_harrison():
    answer1 = False
    for i in president:
        if 'Harrison' in i['Text']:
            answer1 = True
    assert answer1

def test_clinton():
    answer1 = False
    for i in president:
        if 'Clinton' in i['Text']:
            answer1 = True
    assert answer1

def test_coolidge():
    answer1 = False
    for i in president:
        if 'Coolidge' in i['Text']:
            answer1 = True
    assert answer1

def test_arthur():
    answer1 = False
    for i in president:
        if 'Arthur' in i['Text']:
            answer1 = True
    assert answer1

def test_trump():
    answer1 = False
    for i in president:
        if 'Trump' in i['Text']:
            answer1 = True
    assert answer1

def test_eisenhower():
    answer1 = False
    for i in president:
        if 'Eisenhower' in i['Text']:
            answer1 = True
    assert answer1

def test_roosevelt():
    answer1 = False
    for i in president:
        if 'Roosevelt' in i['Text']:
            answer1 = True
    assert answer1

def test_pierce():
    answer1 = False
    for i in president:
        if 'Pierce' in i['Text']:
            answer1 = True
    assert answer1

def test_bush():
    answer1 = False
    for i in president:
        if 'Bush' in i['Text']:
            answer1 = True
    assert answer1

def test_washington():
    answer1 = False
    for i in president:
        if 'Washington' in i['Text']:
            answer1 = True
    assert answer1

def test_ford():
    answer1 = False
    for i in president:
        if 'Ford' in i['Text']:
            answer1 = True
    assert answer1

def test_cleveland():
    answer1 = False
    for i in president:
        if 'Cleveland' in i['Text']:
            answer1 = True
    assert answer1

def test_truman():
    answer1 = False
    for i in president:
        if 'Truman' in i['Text']:
            answer1 = True
    assert answer1

def test_hoover():
    answer1 = False
    for i in president:
        if 'Hoover' in i['Text']:
            answer1 = True
    assert answer1

def test_garfield():
    answer1 = False
    for i in president:
        if 'Garfield' in i['Text']:
            answer1 = True
    assert answer1

def test_buchanan():
    answer1 = False
    for i in president:
        if 'Buchanan' in i['Text']:
            answer1 = True
    assert answer1

def test_polk():
    answer1 = False
    for i in president:
        if 'Polk' in i['Text']:
            answer1 = True
    assert answer1

def test_madison():
    answer1 = False
    for i in president:
        if 'Madison' in i['Text']:
            answer1 = True
    assert answer1

def test_monroe():
    answer1 = False
    for i in president:
        if 'Monroe' in i['Text']:
            answer1 = True
    assert answer1

def test_carter():
    answer1 = False
    for i in president:
        if 'Carter' in i['Text']:
            answer1 = True
    assert answer1

def test_biden():
    answer1 = False
    for i in president:
        if 'Biden' in i['Text']:
            answer1 = True
    assert answer1

def test_adams():
    answer1 = False
    for i in president:
        if 'Adams' in i['Text']:
            answer1 = True
    assert answer1

def test_kennedy():
    answer1 = False
    for i in president:
        if 'Kennedy' in i['Text']:
            answer1 = True
    assert answer1

def test_tyler():
    answer1 = False
    for i in president:
        if 'Tyler' in i['Text']:
            answer1 = True
    assert answer1

def test_buren():
    answer1 = False
    for i in president:
        if 'Buren' in i['Text']:
            answer1 = True
    assert answer1

def test_fillmore():
    answer1 = False
    for i in president:
        if 'Fillmore' in i['Text']:
            answer1 = True
    assert answer1

def test_nixon():
    answer1 = False
    for i in president:
        if 'Nixon' in i['Text']:
            answer1 = True
    assert answer1

def test_reagan():
    answer1 = False
    for i in president:
        if 'Reagan' in i['Text']:
            answer1 = True
    assert answer1

def test_hayes():
    answer1 = False
    for i in president:
        if 'Hayes' in i['Text']:
            answer1 = True
    assert answer1

def test_jefferson():
    answer1 = False
    for i in president:
        if 'Jefferson' in i['Text']:
            answer1 = True
    assert answer1

def test_grant():
    answer1 = False
    for i in president:
        if 'Grant' in i['Text']:
            answer1 = True
    assert answer1

def test_harding():
    answer1 = False
    for i in president:
        if 'Harding' in i['Text']:
            answer1 = True
    assert answer1

def test_taft():
    answer1 = False
    for i in president:
        if 'Taft' in i['Text']:
            answer1 = True
    assert answer1

def test_mckinley():
    answer1 = False
    for i in president:
        if 'McKinley' in i['Text']:
            answer1 = True
    assert answer1

def test_wilson():
    answer1 = False
    for i in president:
        if 'Wilson' in i['Text']:
            answer1 = True
    assert answer1

def test_taylor():
    answer1 = False
    for i in president:
        if 'Taylor' in i['Text']:
            answer1 = True
    assert answer1
