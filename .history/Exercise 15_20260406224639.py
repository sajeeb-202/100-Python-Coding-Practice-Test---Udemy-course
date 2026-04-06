def check_number(num):
    if num==0:
        return "Zero"
        
    elif num>0:
        return "Positive"
        
    else:
        return "Negative"    
        
#.........test cases..........

checking_number = input()
print(check_number(checking_number))