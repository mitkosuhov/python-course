ciname_day = (input('Hor what day do you want a ticket ?'))
if ciname_day in ['Monday','Thuesday','Friday'] :
    print (f'You whant a ticket for {ciname_day} that will be 12$')
elif ciname_day in ['Wednesday','Thursday',] :  
    print (f'You whant a ticket for {ciname_day} that will be 14$')
elif ciname_day in ['Saturday','Sunday'] :  
    print (f'You whant a ticket for {ciname_day} that will be 16$')    
else :
    print('Invalid day ')    
