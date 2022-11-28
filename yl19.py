import re

def Check_Vow(string, vowels):

    str_list = re.findall(f'[{vowels}]', string, re.I)

    print(len(str_list))

    return str_list
    
vowels = 'aeiouõäöü'
string = "kääbik"
print (Check_Vow(string, vowels))