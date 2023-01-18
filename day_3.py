from string import ascii_lowercase,ascii_uppercase 

PRIORITIES_DICTIONARY=dict(zip(ascii_lowercase+ascii_uppercase,range(1,53))) 

def get_input(): 
    with open("input.txt","r") as f: return f.read().splitlines() 

def calculate_priority(letter:str)->int: return PRIORITIES_DICTIONARY[letter]   

def sum_common_priorities():   

    def find_common(rucksack:str)->str:
        middle=int(len(rucksack)/2)  
        first_part=rucksack[:middle]   
        second_part=rucksack[middle:]
        return [letter for letter in rucksack if (letter in first_part and letter in second_part)][0]      

    rucksacks=get_input()  
    total=0 
    for rucksack in rucksacks:total+=(calculate_priority(find_common(rucksack)))   
    return total  

def sum_badges_priorities():
    rucksacks=get_input()
    groups_list=[[rucksacks[i],rucksacks[i+1],rucksacks[i+2]] for i in range(0,len(rucksacks),3)]
    total=0 
    for group in groups_list:
        badge=[item for item in group[0] if (item in group[1] and item in group[2])] [0] 
        total+=(calculate_priority(badge))  
    return total 
 
print((sum_common_priorities(),sum_badges_priorities())) 

