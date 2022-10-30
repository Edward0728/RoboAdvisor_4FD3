#from apps import dt
import re
#from  apps import file_index

# symbol = 'TDB3491.CF'
# risk = 'low to medium'
# size = 'medium'
# percentile = '30%'
# volatility = '0.2'
#file_name=open('./conversations/temp.txt', 'r').readline()
# conversation = open(f'roboAdvisor/chatbot/{dt}.txt', 'r')
# with open(f'./conversations/chat.txt', 'w') as output_file:
#     pass

conversation = open('./roboAdvisor/chatbot/conversations/chat.txt', 'r')
lines = conversation.readlines() 
print(lines)

def parse_chat(lines):
    Cx_Name = ''
    Age = ''
    Amount = ''
    Risk = ''
    Size = ''
    Percentile = ''
    Volatility = ''
    for line in lines:
        #print(line)
        if line.find(', please?') == -1:
            if re.findall(".*My name is.*",line):
                name = line[line.index('name')+8:-2]
                Cx_Name = Cx_Name + name
                print(Cx_Name)

            if re.findall(".*years old.*",line):
                age = line[line.index('years')-3:line.index('years')]
                Age = Age + age
                print(Age)

            if re.findall(".*invest.*",line):
                amount = re.findall("\d+.*",line)
                #Amount = Amount + amount
                print(amount)
                
            if re.findall(".*risk.*",line):
                risk = line[line.index('take')+5:line.index('risk')]
                Risk = Risk + risk
                print(Risk)

            if re.findall(".*size.*",line): 
                #if line.find("small"):
                if re.findall(".*small.*",line):
                    size = 'small'
                #if line.find("medium"):
                if re.findall(".*medium.*",line):
                    size = 'medium'
                #if line.find("large"):
                if re.findall(".*large.*",line):
                    size = 'large'
                Size = Size + size
                print(Size)

            if re.findall(".*top.*",line):  
                percentile = line[line.index('top')+4:line.index('top')+7]
                Percentile = Percentile + percentile
                print(percentile)

            if re.findall(".*volatility.*",line):  
                volatility = line[line.index('volatility')-4:line.index('volatility')-1]
                Volatility = float(volatility.strip('%')) / 100.0
                print(type(Volatility))
                print(Volatility)
    #return risk_list[0], size_list[0], percentile_list[0], volatility_list[0]
    return Risk, Size, Percentile, Volatility
    #print(size)
Risk, Size, Percentile, Volatility = parse_chat(lines)
print(Risk, Size, Percentile, Volatility)

