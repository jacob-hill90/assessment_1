def optimal_change(item_cost: float, amount_paid: float):
    if(item_cost == amount_paid):
        return "Wow, you've payed with exact change and made this assessment way easier for me!"
    
    if(item_cost > amount_paid):
        return "Uh oh, looks like you haven't paid enough!"
    
    answer_string = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is '

    counts = {}
    
    amount_paid_in_pennies = amount_paid * 100
    item_cost_in_pennies = item_cost * 100
    change_in_pennies = amount_paid_in_pennies - item_cost_in_pennies

    money_dict = {
        100: 10000,
        50: 5000,
        20: 2000,
        10: 1000,
        5: 500,
        1: 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }
    
    #Use dictionary to subtract from total change, once largest denomination left is found
    for key in money_dict:
        while change_in_pennies >= money_dict[key]:
            if key in counts.keys():
                counts[key] += 1
            else:
                counts[key] = 1
            change_in_pennies -= money_dict[key]
    #Create another dictionary with denominations and occurences 
    items = list(counts.keys())

    if len(items) == 1:
        end_str = ' dollar bill' if type(items[0]) is int else ''
        end_str += 's.' if counts[items[0]] > 1 else '.'
        if type(items[0]) is int:
            answer_string += f'{counts[items[0]]} ${items[0]}{end_str}'
        else:
           answer_string += f'{counts[items[0]]} {items[0]}{end_str}' 

    else:
        last_item = items[-1]

        for key in counts:
            if key is last_item:
                answer_string += 'and '
            
            if counts[key] > 1:
                if type(key) is int:
                    answer_string += f'{counts[key]} ${key} bills'
                elif key == 'penny':
                    answer_string += f'{counts[key]} pennies'
                else:
                    answer_string += f'{counts[key]} {key}s'
            else:
                if type(key) is int:
                    answer_string += f'{counts[key]} ${key} bill'
                else:
                    answer_string += f'{counts[key]} {key}'

            if not last_item is key:
                answer_string += ', '
            else:
                answer_string += '.'
    return answer_string

print(optimal_change(42.22, 100))