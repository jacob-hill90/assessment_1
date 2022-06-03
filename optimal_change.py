def optimal_change(item_cost, amount_paid):
    
    #When exact change is given
    if(item_cost == amount_paid):
        return "Wow, You've payed with exact change and made this assessment way easier for me!"
    
    #When item cost isn't met by amount paid
    elif(item_cost > amount_paid):
        return "Uh oh, Looks like you haven't paid enough!"
    
    #When amount paid is greater than item cost and we need to give change
    elif item_cost < amount_paid:
        #Create str which should be added to once we know how much change to give
        answer_string = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is '
        array_of_keys = []
        #Convert arguments to pennies so it's easier to work with
        amount_paid_in_pennies = amount_paid * 100
        item_cost_in_pennies = item_cost * 100
        change_in_pennies = amount_paid_in_pennies - item_cost_in_pennies
        
        dict = {
            "100": 10000,
            "50": 5000,
            "20": 2000,
            "10": 1000,
            "5": 500,
            "1": 100,
            "quarter": 25,
            "dime": 10,
            "nickel": 5,
            "penny": 1
        }
    
        #Use dictionary to subtract from total change, once largest denomination left is found
        for key in dict:
            while change_in_pennies >= dict[key]:
                array_of_keys.append(key)
                change_in_pennies -= dict[key]
        #Create another dictionary with denominations and occurances 
        dict_of_change_values = {x:array_of_keys.count(x) for x in array_of_keys}
         
        print(dict_of_change_values)

optimal_change(100,125)


#Very very frustrating, don't have the tools/knowledge to format this sentence correctly. 

       # if i == '100' or i == '50' or i == '20' or i == '10' or i == '5' or i == '1':
    #     if dict_of_change_values[i] == 1:
    #         added_string += f'{dict_of_change_values[i]} ${i} dollar bill'
    #     elif dict_of_change_values[i] > 1:
    #         added_string += f'{dict_of_change_values[i]} ${i} dollar bills' 
    # elif i == 'quarter' or i == 'dime' or i == 'nickel' or 'penny':
    #     if dict_of_change_values[i] == 1:
    #         added_string += f'{dict_of_change_values[i]} {i}'
    #     elif dict_of_change_values[i] > 1 and (i == 'penny'):
    #         added_string += f'and {dict_of_change_values[i]} pennies'
    #     elif dict_of_change_values[i] > 1 and (i == 'quarter' or i == 'dime' or i == 'nickel'):
    #         added_string += f'{dict_of_change_values[i]} {i}s'
    # return answer_string+added_string+"."  

    # if i == '100' or i == '50' or i == '20' or i == '10' or i == '5' or i == '1':
    #     if dict_of_change_values[i] == 1:
    #         added_string += f'{dict_of_change_values[i]} ${i} dollar bill'
    #     elif dict_of_change_values[i] > 1:
    #         added_string += f'{dict_of_change_values[i]} ${i} dollar bills' 
    # elif i == 'quarter' or i == 'dime' or i == 'nickel' or 'penny':
    #     if dict_of_change_values[i] == 1:
    #         added_string += f'{dict_of_change_values[i]} {i}'
    #     elif dict_of_change_values[i] > 1 and (i == 'penny'):
    #         added_string += f'and {dict_of_change_values[i]} pennies'
    #     elif dict_of_change_values[i] > 1 and (i == 'quarter' or i == 'dime' or i == 'nickel'):
    #         added_string += f'{dict_of_change_values[i]} {i}s'
    # return answer_string+added_string+"."