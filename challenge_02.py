import requests

text = requests.get('https://codember.dev/data/message_02.txt').text


def MiniCompiler(task):
    
    aux = 0
    answer = ''
    
    for i in task:
        
        if(i == '#'): aux += 1
                
        elif(i == '@'): aux -= 1
                        
        elif(i == '*'): aux *= aux
                        
        elif(i == '&'): answer += str(aux)
        
        else:
            return None
    return answer

print(MiniCompiler(text))