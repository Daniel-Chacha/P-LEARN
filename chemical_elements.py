import periodictable

def get_element_info(symbol):
    #check if element is valid
    if not periodictable.elements.symbol(symbol):
        print('Invalid Chemical sysmbol')

    element=periodictable.elements.symbol(symbol)

    print('Chemical name' , element.name)
    print('Chemical Atomic Number:' , element.number)
    print('Chemical Isotopes: ',element.isotopes)


symbol=input('Enter a chemical symbol: ')
get_element_info(symbol)