import requests

text = requests.get('https://codember.dev/data/files_quarantine.txt').text

files = text.split('\n')
sections = [i.split('-') for i in files]

correct_files = []

for file, checksum in sections:
    
    correct_checksum = ''.join([i for i in file if file.count(i) == 1])
    
    if checksum == correct_checksum:
        correct_files.append(checksum)
        
print(correct_files[32])