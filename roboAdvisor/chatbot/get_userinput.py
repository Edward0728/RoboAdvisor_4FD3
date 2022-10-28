#from apps import dt
import re

dt='10282022160847'
# conversation = open(f'roboAdvisor/chatbot/{dt}.txt', 'r')
conversation = open(f'roboAdvisor/chatbot/{dt}.txt', 'r')
lines = conversation.readlines() 
for line in lines:
    #print(line)
    if line.find(', please?') == -1:
        if re.findall(".*My name is.*",line):
            cx_name = line[line.index('name')+8:-2]
            print(cx_name)

        if re.findall(".*years old.*",line):
            age = line[line.index('years')-3:line.index('years')]
            print(age)

        if re.findall(".*invest.*",line,re.MULTILINE):
            amount = re.findall("\d+.*",line,re.MULTILINE)
            print(amount[0])
            
        if re.findall(".*risk.*",line,re.MULTILINE):
            risk = line[line.index('take')+5:line.index('risk')]
            print(risk)

        if re.findall(".*size.*",line,re.MULTILINE): 
            if line.find("small"):
                size = 'small'
            if  line.find("medium"):
                size = 'medium'
            if  line.find("large"):
                size = 'large'
            print(size)

        if re.findall(".*top.*",line,re.MULTILINE):  
            percentile = line[line.index('top')+4:line.index('top')+7]
            print(percentile)

        if re.findall(".*volatility.*",line,re.MULTILINE):  
            volatility = line[line.index('volatility')-4:line.index('volatility')-1]
            print(volatility)
