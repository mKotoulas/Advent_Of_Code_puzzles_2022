def get_input():
    with open("input.txt","r") as f:
        return [[int(food) for food in foods.split("\n")] for foods in f.read().split("\n\n")]

def top_elf(foods:list[list[int]]):
    return sorted([sum(calories) for calories in foods],reverse=True)[0]

def top_three_elves(foods:list[list[int]]): 
    return sum(sorted([sum(calories) for calories in foods],reverse=True)[:3])
    
print(f"Top elf is carrying in total:{top_elf(get_input())} calories")
print(f"Top three elves are carrying in total:{top_three_elves(get_input())} calories")