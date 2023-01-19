def main():

    def get_input()->str: 
        with open("input.txt","r") as f :return f.read().splitlines()      
    
    def parse_commands(commands:str)->dict:    

        current_path=None  
        path_dictionary={"root":0} 

        for command in commands:
            command_splitted=command.split(" ") 
            if len(command_splitted)==2: 
                first_part,second_part=command_splitted     
                if first_part=="$":continue 
                elif first_part=="dir":
                    revisited=False
                    new_path=current_path+f"/{second_part}" 
                    if new_path not in path_dictionary.keys():path_dictionary[new_path]=0
                    else:revisited=True      
                else:
                    if revisited:continue
                    path=current_path    
                    while path:
                        path_dictionary[path]+=int(first_part) 
                        path="/".join(path.split("/")[:-1])   
            else:
                first_part,second_part,third_part=command_splitted
                if third_part=="/":current_path="root"
                elif third_part=="..":current_path="/".join(current_path.split("/")[:-1]) 
                else:current_path+=f"/{third_part}" 
       
        return path_dictionary       
                   
    commands=get_input()     
    path_dictionary=parse_commands(commands)
    #part one  
    sum_sizes_under_100000=sum([size for size in path_dictionary.values() if size<=100000])
    #part two 
    space_to_free=30000000-(70000000-path_dictionary["root"])   
    size_to_delete=min([size for size in path_dictionary.values() if size>=space_to_free])
    return (sum_sizes_under_100000,size_to_delete) 

print(main())  