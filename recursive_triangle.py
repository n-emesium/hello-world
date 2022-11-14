def recursive_triangle(num,char):
    if num > 0:
        print(num * char)
        recursive_triangle(num-1,char)
        
recursive_triangle(5,"x")

"""
def draw_recursive(num,char):
    if num > 0:
        draw_recursive(num-1,char)
        print(num*char)

        
draw_recursive(5,"x")
"""
#This is the reversed version