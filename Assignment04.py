# This is our first assignment as a group
try: 
    import numpy as np
except ImportError:
    print("Could not import numpy")

try:
    import logging
except ImportError:
    print("Could not import logging")

import sphinx 


def main():
    logging.basicConfig(filename="OuroborosAssignment04log.txt", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')
    my_list = (['string'])
    return_sum(my_list)
    return_min_max(my_list)
    return_max_difference(my_list)
    logging.info('Finished')



def return_min_max(my_list):

    """ This is the description of the function

    :param my_list: a list of numbers
    :returns max_min: the max and min values in the list of numbers
    :raises TypeError: can only input a list of numbers
    :raises ValueError: can not input an empty list

    """
    if np.iscomplexobj(my_list) is True:
        logging.warning('There are imaginary numbers in your list')
    try:
        np.max(my_list)
    except TypeError:
        logging.debug('my_list is {}'.format(my_list))
        print("You did not input a list of numbers")
    except ValueError:
        print("The input type is correct but inappropriate")  
    

    max_min = ((np.max(my_list), np.min(my_list)))
    return max_min

    
def return_sum(my_list):
    sum = 0
    for elem in my_list:
       sum += elem
    return sum




def return_max_difference(my_list):
   pass


if __name__ == "__main__":
   main()

