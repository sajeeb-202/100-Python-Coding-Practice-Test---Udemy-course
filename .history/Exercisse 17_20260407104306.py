def is_leap_year(year : int):
    if year%4==0 and year%100!=0:
        return True
    
    
    elif year==0:
        return True
        
    if year>=2000 and year%400==0:
        return True
           
            
    else:
        return False
    
#.......test function........

get_year = int(input())
print(is_leap_year(get_year))