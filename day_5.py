import re 
from copy import deepcopy

def get_input(): 
    with open("input.txt","r") as f: 
        return [item.splitlines() for item in f.read().strip("\n").split("\n\n")]     
        
def find_message():

    def parse_cargo(cargo:list)->dict: 
        cargo_dict={number.strip():[] for number in cargo[-1].split("  ")}   
        possible_indexes=[id for id,letter in enumerate(cargo[-1]) if letter!=" "] #that solved the whole thing lol  
        for line in cargo[:-1]:
            for id,index in enumerate(possible_indexes,start=1): 
                if line[index]!=" ":cargo_dict[str(id)].insert(0,line[index])   
        return cargo_dict        
            
    def parse_command(command:str)->list[str]:return map(str,re.findall("\d+",command)) 
        
    def execute_command(command_items,cargo_dict,mode): 
        amount,start,to=command_items 
        items_list=cargo_dict[start][-int(amount):]    
        del cargo_dict[start][-int(amount):]
        if mode=="9000":
            for item in reversed(items_list):cargo_dict[to].append(item)
        elif mode=="9001":
            for item in items_list:cargo_dict[to].append(item)    
        return cargo_dict
 
    cargo,commands=get_input() 
    cargo_dict=parse_cargo(cargo) 
    cargo_dict_copy=deepcopy(cargo_dict)
    for command in commands:
        cargo_dict=execute_command(parse_command(command),cargo_dict,mode="9000")
        cargo_dict_copy=execute_command(parse_command(command),cargo_dict_copy,mode="9001")
    ''' 
    for command in commands:cargo_dict=execute_command(parse_command(command),cargo_dict,mode="9000") 
    for command in commands:cargo_dict_copy=execute_command(parse_command(command),cargo_dict_copy,mode="9001")
    '''  
    msg_9000=f"{''.join([value[-1] for value in cargo_dict.values()])}"
    msg_9001=f"{''.join([value[-1] for value in cargo_dict_copy.values()])}"
    return (msg_9000,msg_9001)
           
print(find_message())   