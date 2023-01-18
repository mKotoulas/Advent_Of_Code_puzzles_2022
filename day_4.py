def get_input():
    with open("input.txt","r") as f: return f.read().splitlines()  

def overlap_pairs():

    def bounds(pair:str)->tuple[int]:
        first_range,second_range=pair.split(",") 
        first_low,first_high=map(int,first_range.split('-')) 
        second_low,second_high=map(int,second_range.split('-'))  
        return (first_low,first_high,second_low,second_high)  

    def sort_substring(pair:str)->str: 
        first_low,first_high,second_low,second_high=bounds(pair)  
        if second_high>first_high:return pair  
        if second_high<first_high: return f"{second_low}-{second_high},{first_low}-{first_high}"   
        else: 
            if first_low>=second_low:return pair  
            else: return f"{second_low}-{second_high},{first_low}-{first_high}"      
    
    def total_overlap(pair:str):
        first_low,first_high,second_low,second_high=bounds(pair) 
        if first_low>=second_low and first_low<=second_high and first_high<=second_high:return True 
        elif second_high==second_low and second_low==first_high:return True
        else: return False  

    def partial_overlap(pair:str):
        first_low,first_high,second_low,second_high=bounds(pair)  
        if [item for item in range(first_low,first_high+1) if item in range(second_low,second_high+1)]:return True 
        return False 
    
    pairs=[sort_substring(pair) for pair in get_input()]      

    total_overlapping_pairs=sum( [1 if total_overlap(pair) else 0 for pair in pairs] ) 
    partial_overlaping_pairs=sum( [1 if partial_overlap(pair) else 0 for pair in pairs] )
    
    return (total_overlapping_pairs,partial_overlaping_pairs) 

print(overlap_pairs()) 
       