def get_input():
    with open("input.txt","r") as f: return f.read()

def find_marker_end(mode:int): 
    message = get_input().strip()
    for index,character in enumerate(message):
        potential_marker = message[index:index+mode] 
        unique_characters = set(potential_marker)   
        if len(unique_characters) == mode:            
            return index + mode

print(find_marker_end(4),find_marker_end(14))  