def weight_on_planets():

    #Boolean to indicate whether the user input is valid
    clear = False
    
    #First prompt for user input
    weight = input('What do you weigh on earth? ')
       
    while (clear == False):
        
        #Loop to disallow program from continuing if user input is a non-numerical answer
        while True:
            try:
                test = int(weight)
                break
            except ValueError:
               weight = input('What do you weigh on earth? ')
            
        #If statement to disallow program from continuing if user input is not at least 1
        if ('-' in weight or weight == '0'):
            weight = input('What do you weigh on earth? ')
        else:
            clear = True
    
    #Casting new variable as float value of user input
    space_weight = float(weight)
    
    #Printing Mars and Jupiter weights based on user input
    print('\nOn Mars you would weigh %s pounds.\nOn Jupiter you would weigh %s pounds.' \
        % (space_weight*0.38, space_weight*2.34))

if __name__ == '__main__':
    weight_on_planets()