from tkinter import *

d = {'Alewife': ['Davis'],\
     'Davis': ['Alewife', 'Porter'],\
    'Porter': ['Harvard', 'Davis'],\
    'Harvard':['Central', 'Porter'],\
    'Central': ['Harvard', 'Kendall'],\
    'Kendall': ['Central', 'Charles/MGH'],\
    'Charles/MGH': ['Kendall', 'Park Street'],\
    'Park Street': ['Charles/MGH', 'Government Center', 'Downtown Crossing', 'Boylston'],\
    'Boylston': ['Park Street', 'Arlington'],\
    'Government Center': ['Haymarket', 'State', 'Park Street', 'Bowdoin'],\
    'Arlington': ['Boylston', 'Copley'],\
    'Copley': ['Arlington', 'Hynes ICA', 'Prudential'],\
    'Hynes ICA': ['Copley', 'Kenmore'],\
    'Kenmore': ['Hynes ICA'],\

    'Prudential': ['Copley', 'Symphony'],\
    'Symphony': ['Prudential'],\

    'Bowdoin': ['Government Center'],\
    'State': ['Haymarket', 'Downtown Crossing', 'Aquarium'],\
    'Aquarium': ['State', 'Maverick'],\
    'Maverick': ['Aquarium', 'Airport'],\
    'Airport': ['Maverick', 'Wood Island'],\
    'Wood Island': ['Airport', 'Orient Heights'],\
    'Orient Heights': ['Wood Island', 'Suffolk Downs'],\
    'Suffolk Downs':['Orient Heights', 'Beachmont'],\
    'Beachmont': ['Suffolk Downs', 'Revere Beach'],\
    'Revere Beach': ['Beachmont', 'Wonderland'],\
    'Wonderland': ['Revere Beach'],\
     
    'Haymarket': ['North Station', 'State', 'Government Center'],\
    'North Station': ['Haymarket', 'Science Park', 'Community College'],\
    'Science Park': ['North Station', 'Lechmere'],\
    'Lechmere': ['Science Park', 'Union Sq'],\
    'Union Sq': ['Lechmere'],\

    'Community College': ['North Station', 'Sullivan Square'],\
    'Sullivan Square': ['Community College', 'Wellington'],\
    'Wellington': ['Sullivan Square', 'Malden'],\
    'Malden': ['Wellington', 'Oak Grove'],\
    'Oak Grove': ['Malden',],\
     
    'Downtown Crossing': ['State','South Station', 'Chinatown', 'Park Street'],\
    'South Station': ['Downtown Crossing', 'Broadway'],\
    'Broadway': ['South Station', 'Andrews'],\
    'Andrews': ['Broadway', 'JFK/UMass'],\
    'JFK/UMass': ['Andrews', 'Savin Hill', 'North Quincy'],\
    'Savin Hill': ['JFK/UMass', 'Fields Corner'],\
    'Fields Corner': ['Savin Hill', 'Shawmut'],\
    'Shawmut': ['Fields Corner', 'Ashmount'],\
    'Ashmount': ['Shawmut'],\
     
    'North Quincy': ['JFK/UMass', 'Wollaston'],\
    'Wollaston': ['North Quincy', 'Quincy Center'],\
    'Quincy Center': ['Wollaston', 'Quincy Adams'],\
    'Quincy Adams': ['Quincy Center', 'Braintree'],\
    'Braintree': ['Quincy Adams'],\
     
    'Chinatown': ['Downtown Crossing', 'NE Medical Center'],\
    'NE Medical Center': ['Chinatown', 'Back Bay'],\
    'Back Bay': ['NE Medical Center', 'Mass Ave'],\
    'Mass Ave': ['Back Bay', 'Ruggles'],\
    'Ruggles': ['Mass Ave', 'Roxbury Crossing'],\
    'Roxbury Crossing': ['Ruggles', 'Jackson'],\
    'Jackson': ['Roxbury Crossing', 'Stony Brook'],\
    'Stony Brook': ['Jackson', 'Green Street'],\
    'Green Street': ['Stony Brook', 'Forest Hills'],\
    'Forest Hills': ['Green Street']}


def nextStop(location_in):
    for i in range(len(d[location_in])):

        if d[location_in][i] not in visited:

            next_stop = d[location_in][i]

            return next_stop
        
    else:
        return None

    
def nextStopReversed(location_in):

    location_range = []
    for i in range(len(d[location_in])):
        location_range += [i]

    location_range.reverse()
    
    for number in location_range:

        if d[location_in][number] not in reverse_visited:

            next_stop = d[location_in][number]

            return next_stop
    else:  
        return None
   

window = Tk()

window.geometry('390x500+300+150')

window.title('Subway Solver')


listChoices = list(d.keys())
listChoices.sort()

varChoice = StringVar(window)

labelStart = Label(window, text='Start Location:  ')
labelStart.grid(row=0, column=0, padx=10, pady=5)

optionmenuStart = OptionMenu(window, varChoice, *listChoices)
optionmenuStart.configure(width=20)
optionmenuStart.grid(row=0, column=1)


##listChoices = list(d.keys())
##listChoices.sort()

varChoice2 = StringVar(window)

labelDestination = Label(window, text='Destination:      ')
labelDestination.grid(row=1, column=0, padx=10, pady=5)

optionmenuDestination = OptionMenu(window, varChoice2, *listChoices)
optionmenuDestination.configure(width=20)
optionmenuDestination.grid(row=1, column=1)


def onFindRouteClick():

    start_location = varChoice.get()

    destination = varChoice2.get()

    current_location = start_location

    path = [start_location]

    global visited

    visited = [start_location]
    
    
    while current_location != destination:

        next_location = nextStop(current_location)

        if next_location == None:
        
            path.remove(current_location)

            current_location = path[-1]

        else:
            current_location = next_location
            
            path += [current_location]

            visited += [current_location]



    current_location = start_location

    reverse_path = [start_location]

    global reverse_visited

    reverse_visited = [start_location]

    while current_location != destination:

        next_location = nextStopReversed(current_location)

        if next_location == None:

            reverse_path.remove(current_location)

            current_location = reverse_path[-1]
         

        else:
            current_location = next_location
            
            reverse_path += [current_location]

            reverse_visited += [current_location]

        
    if len(path) > len(reverse_path):
        path = reverse_path


    s = 'To get from {} to {}, \n you can take the following route:\n\n'.format(start_location, destination)

    n = 1
    for location in path:
        s += '  {}. '.format(n) + location + '\n'
        n += 1
        

    routeLabel = Label(window, text=s)
    routeLabel.grid(row=3, column= 0, columnspan=2, padx=10, pady=5)
    
buttonFindRoute = Button(window, text='Find Route', command=onFindRouteClick)
buttonFindRoute.grid(row=2, column= 0, columnspan=2, padx=10, pady=5)
buttonFindRoute.configure(width=37)

varChoice.set('Alewife')
varChoice2.set('Harvard')

mainloop()
