# This is our first assignment as a group
import numpy as np

def main():
    return_sum(my_list)
    return_min_max(my_list)
    return_max_difference(my_list)

    
def return_min_max(my_list):
    max_min = ((max(my_list), min(my_list)))
    return max_min
    
  
def return_sum(my_list):

    """
    :param my_list: list containing real numbers to be summed
    :raises: TypeError if list cannot be summed
    :raises: ValueError if no elements in given list
    :returns: sum of all elements in the list
    """
    import logging
    logging.basicConfig(filename='sumlog.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
    with open('sumlog.txt', 'w'):
        pass
    logging.info('Function starting')

    try:
        np.sum(my_list)
    except TypeError:
        print('Input list should be numbers')        
        logging.debug('Given list does not contain summable elements')
    
    if len(my_list) == 0:
        raise ValueError('No elements in list to be summed')
        logging.warning('No elements present to be summed')


    sum = 0
    for elem in my_list:
        sum += elem
    logging.info('Elements have been summed')
    return sum


def return_max_difference(input_list):
   input_list = np.array(input_list)
   diffs = abs(np.diff(input_list))
   max_val = max(diffs)

   return max_val


if __name__ == "__main__":
   main()
