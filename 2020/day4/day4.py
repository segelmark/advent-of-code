import re
from validationdata import *

def validatePassport(data):
    passport=data.split()
    fields={}
    for entry in passport:
        data=entry.split(":")
        fields[data[0]] = data[1]
    # Check for all fields except cid
    if not 'ecl' in fields or not 'pid' in fields or not 'eyr' in fields or not 'hcl' in fields or not 'byr' in fields or not 'iyr' in fields or not 'hgt' in fields:
        return { 'requiredFields': False, 'valid': False }
    valid=True
    if not int(fields['byr']) >= 1920 or not int(fields['byr']) <= 2002: #byr (Birth Year) - four digits; at least 1920 and at most 2002.
        valid=False
    elif not int(fields['iyr']) >= 2010 or not int(fields['iyr']) <= 2020: #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        valid=False
    elif not int(fields['eyr']) >= 2020 or not int(fields['eyr']) <= 2030: # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        valid=False
    elif not fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        valid=False
    elif not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', fields['hcl']): # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        valid=False 
    elif not re.search(r'^[0-9]{9}$', fields['pid']): # pid (Passport ID) - a nine-digit number, including leading zeroes.
        valid=False
    if fields['hgt'][-2:]=="cm":  # hgt (Height) - a number followed by either cm or in
        if not int(fields['hgt'][:-2])>=150 or not int(fields['hgt'][:-2])<=193: # If cm, the number must be at least 150 and at most 193.
            valid=False
    elif fields['hgt'][-2:]=="in":
        if not int(fields['hgt'][:-2])>=59 or not int(fields['hgt'][:-2])<=76: # If in, the number must be at least 59 and at most 76.
            valid=False
    else:
        valid=False
    
    return { 'requiredFields': True, 'valid': valid }

assert validatePassport(validation[0])["requiredFields"]==True #The first passport has all eight fields present.
assert validatePassport(validation[1])["requiredFields"]==False #The second passport is missing required hgt (the Height field).
assert validatePassport(validation[2])["requiredFields"]==True #The third passport is only missing field is cid, temporarily to be treated as having all fields.
assert validatePassport(validation[3])["requiredFields"]==False #The fourth passport is missing two fields, cid and required byr.

def day4(data):
    countRequired=0
    countValid=0
    for passport in data:
        if(validatePassport(passport)["requiredFields"]):
            countRequired+=1
        if(validatePassport(passport)["valid"]):
            countValid+=1
    return [countRequired, countValid]

assert day4(validation)[0] == 2
assert day4(validationGood)[1] == 4
assert day4(validationBad)[1] == 0

f = open("input.txt", "r")
data = f.read().split("\n\n")

print(day4(data))
