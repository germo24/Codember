import requests

text = requests.get('https://codember.dev/data/encryption_policies.txt').text

passwords = text.split('\n')
passwords = [i.split(':') for i in passwords]

lines = [( i[0].split(' '), i[1].replace(' ', '') )for i in passwords]

count = 0

for policy, password in lines:
    
    letter = policy[1]
    min, max = [int(i) for i in policy[0].split('-')]
    
    print(count, password, policy)
    if password.count(letter) >= min and password.count(letter) <= max:
        continue
    
    if count == 41:
        print('WE FOUND THE 42ND INVALID PASSWORD SUCCESUFULLY!', password)
        break
    
    else:
        count += 1
