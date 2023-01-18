def get_input():
    with open ("input.txt","r") as f: return f.read().splitlines()  

def false_assumption_score(): 
    
    def symbol_score(pair:list[str])->int:  
        symbol_scores={"X":1,"Y":2,"Z":3}     
        return symbol_scores[pair[1]] 

    def round_outcome_score(pair:list[str])->int: 
        win_conditions={"A":"C","B":"A","C":"B"}  
        equivalent_symbols={"X":"A","Y":"B","Z":"C"} 
        if equivalent_symbols[pair[1]]==pair[0]:return 3 
        elif win_conditions[ equivalent_symbols[pair[1]] ] == pair[0]: return 6     
        else:return 0     
     
    total=0  
    rounds=[pair.split(" ") for pair in get_input()]   
    for round in rounds:total+=(symbol_score(round)+round_outcome_score(round))   
    return total 

def true_assumption_score():

    def round_outcome_score(pair:list[str])->int:
        symbols_to_points_table={"X":0,"Y":3,"Z":6} 
        return symbols_to_points_table[pair[1]] 
    
    def symbol_to_play(pair:list[str])->str:
        win_conditions={"A":"C","B":"A","C":"B"} 
        outcome=pair[1] 
        if outcome=="Y":return pair[0] 
        elif outcome=="X": return win_conditions[pair[0]]  
        else: return  [key for key,value in win_conditions.items() if value==pair[0]] [0]   

    def symbol_score(pair:list[str])->int:    
        symbol_scores={"A":1,"B":2,"C":3}
        symbol=symbol_to_play(pair)      
        return symbol_scores[symbol] 

    total=0 
    rounds=[pair.split(" ") for pair in get_input()] 
    for round in rounds: total+=(round_outcome_score(round)+symbol_score(round)) 
    return total 

print( (false_assumption_score(),true_assumption_score()) )
      











  





















''' 
def get_score():
    convertion_symbols={"X":"A","Y":"B","Z":"C"} 
    win_conditions={"A":"C","B":"A","C":"B"}    
    symbol_scores={"A":1,"B":2,"C":3}  
    data=get_input() 
    data=[pair.split(" ") for pair in data] 
    data=[[pair[0], convertion_symbols[pair[1]]] for pair in data]  
    total=0 
    for pair in data:
        total+=(symbol_scores[pair[1]]) 
        if pair[0]==pair[1]:total+=3 
        elif pair[0]==win_conditions[pair[1]]:total+=6
    return total 
'''






      

        

false_assumption_score()