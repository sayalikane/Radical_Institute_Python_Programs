import sys;

string="I am a girl"

vowels=[i for i in string if i in 'aAeEiIoOuU']
print(vowels)

string2="olive is enthusiastic"

vowels1=[i for i in string2 if i not in 'aAeEiIoOuU']

print(vowels1)