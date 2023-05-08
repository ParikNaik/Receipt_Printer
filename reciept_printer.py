import random
import datetime


def main():
    #print the store name 

    print("\nGreetings from Parik's Plate")
    name = input('\nEnter name for Order: ')

    #print out the menu items & price and prompt user for the quantity of each item

    i_pizza = 32 #32 slices of pizza available 
    i_salad = 12 #12 orders of salad available
    i_pasta = 23 #23 orders of pasta available
    i_wings = 70 #70 wings available
    i_nachos = 29 #29 orders of nachos available
    i_fries = 80 #80 orders of fries available
    i_softdrinks = 100 #100 cups available


    print('\nA slice is $1.00, and we have 32 slices available')
    pizza = int(input('How many slices would you like?'))
    while pizza<0 or pizza>i_pizza:
        print("Error: Too many ordered or a negative value has been entered...Please enter a valid amount")
        pizza = int(input('How many slices would you like?'))


    print('\nA salad is $3.50, and we have 12 orders available')
    salads = int(input('How many orders of salad would you like?'))
    while salads<0 or salads>i_salad:
        print("Error: Too many ordered or a negative value has been entered...Please enter a valid amount")
        salads = int(input('How many orders of salad would you like?'))


    print('\nAn order of pasta is $8.50, and we have 23 orders available')
    pasta = int(input('How many orders of pasta would you like?'))
    while pasta<0 or pasta>i_pasta:
        print("Error: Too many ordered or a negative value has been entered...Please enter a valid amount")
        pasta = int(input('How many orders of pasta would you like?'))


    print('\nEach wing is $0.75, and we have 70 available')
    wings = int(input('How many wings would you like?'))
    while wings<0 or wings>i_wings:
         print("Error: Too many ordered or a negative value has been entered...Please enter a valid amount")
         wings = int(input('How many wings would you like?'))


    print('\nAn order of nachos is $6.75, and we have 29 orders available')
    nachos = int(input('How many orders of nachos would you like?'))
    while nachos<0 or nachos>i_nachos:
        print("Error: Too many ordered or a negative value has been entered...Please enter a valid amount")
        nachos = int(input('How many orders of nachos would you like?'))


    print('\nAn order of our fries is $4.25, and we have 80 orders available')
    fries = int(input('How many orders of fries would you like?'))
    while fries<0 or fries>i_fries:
        print("Error: Too many ordered or a negative value has been entered...Please enter a valid amount")
        fries = int(input('How many orders of fries would you like?'))


    print('\nOur soft drinks are $2.00, and we have 100 cups available')
    soft_drink = int(input('How many soft drinks would you like?'))
    while soft_drink<0 or soft_drink>i_softdrinks:
        print("Error: Too many ordered or a negative value has been entered...Please enter a valid amount")
        soft_drink = int(input('How many soft drinks would you like?'))

    print('\n_______________________________________')

    #calculate the amount for each order
    f_pizza = get_pizza(pizza)
    f_salads = get_salad(salads)
    f_pasta = get_pasta(pasta)
    f_wings = get_wings(wings)
    f_nachos = get_nachos(nachos)
    f_fries = get_fries(fries)
    f_soft_drink = get_softdrink(soft_drink)

    total = f_pizza + f_salads + f_pasta + f_wings + f_nachos + f_fries + f_soft_drink
    tax = total*.07
    f_total = total + tax

    pizza_label = "Pizza:"
    salad_label = "Salad:"
    pasta_label = "Pasta:"
    wings_label = "Wings:"
    nachos_label = "Nachos:"
    fries_label = "Fries:"
    soft_drink_label = "Drink:"

    subtotal_label = "Subtotal:"    
    tax_label = "Tax:"
    total_label = "Total:"

    #print receipt

    outfile = open(f'{random.randint(1111111,9999999)}.txt', 'w')

    outfile.write("Parik's Plate")
    outfile.write('\n908-293-3209')
    outfile.write('\n129 Hill Road \nRahway, New Jersey \n')
    outfile.write(name)
    outfile.write("\n\n")
    
    

    outfile.write(f"\n{pizza_label:15} ${f_pizza:.2f}")
    outfile.write(f"\n{salad_label:15} ${f_salads:.2f}")
    outfile.write(f"\n{pasta_label:15} ${f_pasta:.2f}")
    outfile.write(f"\n{wings_label:15} ${f_wings:.2f}")
    outfile.write(f"\n{nachos_label:15} ${f_nachos:.2f}")
    outfile.write(f"\n{fries_label:15} ${f_fries:.2f}")
    outfile.write(f"\n{soft_drink_label:15} ${f_soft_drink:.2f}")

        

    outfile.write('\n----------------------')
    outfile.write(f"\n{subtotal_label:15} ${total:.2f}")
    outfile.write(f"\n{tax_label:15} ${tax:.2f}")
    outfile.write(f"\n{total_label:15} ${f_total:.2f}")

    x = datetime.datetime.now()
    outfile.write(f'\n{x}')

    transaction = random.randint(11111,99999)
    outfile.write(f'\nTransaction ID: {transaction}')

    outfile.write("\nThank you, come again")

    
    outfile.close()


def get_pizza(pizza):
    f_pizza = pizza*1
    return f_pizza

def get_salad(salads):
    f_salads = salads*3.50
    return f_salads

def get_pasta(pasta):
    f_pasta = pasta*8.50
    return f_pasta

def get_wings(wings):
    f_wings = wings*0.75
    return f_wings

def get_nachos(nachos): 
    f_nachos = nachos*6.75
    return f_nachos

def get_fries(fries): 
    f_fries = fries*4.25
    return f_fries

def get_softdrink(soft_drink):
    f_soft_drink = soft_drink*2
    return f_soft_drink


main()

