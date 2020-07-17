############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        #Activate the 'variables'/traits ^parameters^ related to each object by telling the function to create a template. 
        #Follow parameter order.

        self.code = code 
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedles = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        #Adds pairing information (pairing "method") 

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        #Overriding the previous code used to describe melon traits/. 

        self.code = new_code 


def make_melon_types():
    """Returns a list of current melon types."""
    #Specifying the traits/information about the melons. 
    #Using the call/order 'MelonType' to specify information about the Melon.

    all_melon_types = []

    # code = MelonType(code, name, first_harvest, color, is_seedless, is_bestseller)

    #Muskmelon:
    musk = MelonType('musk', 'Muskmelon', 1998, 'green',True, True)
    musk.add_pairing('mint') #This specifies the pairing 
    all_melon_types.append(musk) #This gives us the name of the melon
    print(musk)

    #Casaba:
    cas = MelonType("cas", "Casaba", 2003, 'orange', True, False)
    cas.add_pairing('strawberries, mint')
    all_melon_types.append(cas)
    
    #Crenshaw:
    cren = MelonType('cren', 'Crenshaw', 1996, 'green', True, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    #Yellow Watermelon:
    yw = MelonType('yw', "Yellow Watermelon", 2013, 'yellow', True, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)
    


    return all_melon_types

    
def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types: 
        print(f' {melon.name} pairs with:') 

        for pairing in melon.pairings: 
            print(f' - {pairing}') 


    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon_obj in melon_types:
        melon_dict[melon_obj.code] = melon_obj

    
    
    return melon_dict



all_melon_types = make_melon_types()
print(print_pairing_info(all_melon_types))
# print(make_melon_type_lookup(all_melon_types))
# (print(all_melon_types))





# print(make_melon_types())

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, harvested_by): #is_bestseller)
        self.code = code 
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Determine whether this melon can be sold."""
        for melon in melons:
            if melon.shape_rating > 5 and melon.color_rating >5:
        #field !=3:
                print('can be sold')
        else:
            print('unsafe')

    def melon_type(melon_types):

        # (self, code, shape_rating, color_rating, harvested_by

        melons_by_id = make_melon_type_lookup(melon_types)
        melons = []

        #Melon 1
        melon1 = Melon(melons_by_id["musk"], 8, 7, 'Sheila')

        #Melon 2
        melon2 = Melon(melons_by_id['yw'], 3, 4, 'Sheila')

        #Melon 3
        melon3 = Melon(melons_by_id['yw'], 9, 8, 'Sheila')
        
        #Melon 4
        melon4 = Melon(melons_by_id['cas'], 10, 6, "Sheila ")

        #Melon 5
        melon5 = Melon(melons_by_id['cren'], 8, 9, "Michael")

        #Melon 6 
        melon6 = Melon(melons_by_id['cren'], 8, 2, "Michael")

        #Melon 7 
        melon7 = Melon(melons_by_id['cren'], 2, 3, "Michael")

        #Melon 8
        melon8 = Melon(melons_by_id["musk"], 6, 7, "Michael")

        #Melon 9 
        melon9 = Melon(melons_by_id['yw'], 7, 10, 'Sheila')

        melons.extend(melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9)


        return melons



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
 

melons = melon_type(melon_types)
print(get_sellability_report(melons))
# print(make_melon_type_lookup(all_melon_types))
# (print(all_melon_types))







