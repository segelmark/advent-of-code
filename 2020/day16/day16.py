from validationdata import *

def parseData(data):
    data=data.split("\n\n")
    rules=data[0].splitlines()
    rules = [r.replace("-"," or ").replace(": "," or ").split(" or ") for r in rules]
    rules = [ [r[0], int(r[1]),int(r[2]),int(r[3]),int(r[4])] for r in rules ]
    my_ticket=data[1].splitlines()[1].split(",") 
    my_ticket = [ int(t) for t in my_ticket ]
    nearby_tickets=data[2].splitlines()[1:]
    nearby_tickets=[ticket.split(",") for ticket in nearby_tickets]
    nearby_tickets = [ [int(t) for t in ticket] for ticket in nearby_tickets ]
    return rules, my_ticket, nearby_tickets

def runRules(value,rules):
    valid=False
    for rule in rules:
        if rule[1]<=value<=rule[2] or rule[3]<=value<=rule[4]:
            valid=True
    return valid

def errorsOnTicket(ticket,rules):
    errors=0
    for num in ticket:
        number=int(num)
        if not runRules(number,rules): errors+=number
    return errors

def getScanningErrorRate(data):
    rules, my_ticket, nearby_tickets = parseData(data)
    rateSum=0
    for ticket in nearby_tickets:
        rateSum+=errorsOnTicket(ticket,rules)
    return rateSum

assert getScanningErrorRate(validationdata) == 71


f = open("input.txt", "r")
data = f.read()

rules, my_ticket, nearby_validation = parseData(validationdata)

print(getScanningErrorRate(data))

def validateTicket(ticket,rules):
    valid=True
    for num in ticket:
        number=int(num)
        if not runRules(number,rules): valid=False
    return valid

def getValidTickets(tickets,rules):
    return list(filter(lambda ticket: validateTicket(ticket,rules),tickets))

def validateRule(rule, tickets):
    columns=[]
    column=0
    while(column<len(tickets[1])):
        print(column)
        valid=True
        for t in tickets:
            if(not runRules(t[column],[rule])):
                valid=False
        print(valid)
        if valid: columns.append(column)
        column+=1
    return columns


def part2(data):
    rules, my_ticket, nearby_tickets = parseData(data)
    validTickets=getValidTickets(nearby_tickets,rules)
    columns={}
    for rule in rules:
        print(rule)
        columns[rule[0]] = validateRule(rule, validTickets)
        #while(column<len(rule)):
        # pass
        # validateRule(rule,column,validTickets)
    unique={}
    while len(unique)<len(validTickets[0]):
        for key, value in columns.items():
            if(len(value)==1):
                unique[key]=value[0]
                for key, val in columns.items():
                    if(len(val)>1):
                        try:
                            val.remove(value[0])
                        except:
                            pass
    print(my_ticket)
    print(unique)
    fields=['departure time', 'departure track', 'departure date', 'departure station', 'departure platform', 'departure location']
    product=1
    for f in fields:
        product*=my_ticket[unique[f]]
    return product
        
            
print(part2(data))


# rules, my_ticket, nearby_tickets = parseData(data)
