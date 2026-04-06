def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    if kilometers==0:
        return 0
    
    if 0<kilometers<1:
        return miles
        
        
    
    
    if kilometers>=1:
        return miles
    
    
    
    else:
        return "Distance cannot be negative"