class MyList:

    def __init__(self, numbers=[1, 2, 3]):
        self.numbers = numbers
        self.output_sum = None
        self.output_min_max = None
        self.output_max_diff = None
        self.return_sum()
        self.return_min_max()
        self.return_max_diff()

    def return_sum(self):
        """ Function returns sum of list

        :param self: Attribute method to class
        :raises: TypeError if list cannot be summed
        :raises: ValueError if no elements in given list
        :returns: sum of all elements in the list
        """
        import numpy as np
        import logging
        logging.basicConfig(filename='sumlog.txt', level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S')
        with open('sumlog.txt', 'w'):
            pass
        logging.info('Function starting')

        try:
            self.output_sum = np.sum(self.numbers)
        except TypeError:
            print('Input list should be numbers')
            logging.debug('Given list does not contain summable elements')

        if len(self.numbers) == 0:
            raise ValueError('No elements in list to be summed')
            logging.warning('No elements present to be summed')

        # self.output_sum = sum(self.numbers)
        # self.output_sum = 0
        # for elem in self.numbers:
        #    self.output_sum = sum(elem)
        # logging.info('Elements have been summed')

    def return_min_max(self):
        """ Function returns the max and min value of the input list

            :param self: a list of numbers
            :returns max_min: the max and min values in the list of numbers
            :raises TypeError: can only input a list of numbers
            :raises ValueError: can not input an empty list
            """
        import numpy as np
        import logging
        logging.basicConfig(filename="OuroborosAssignment04log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info('Started')

        if np.iscomplexobj(self.numbers) is True:
            logging.warning('There are imaginary numbers in your list')
        try:
            max(self.numbers)
        except TypeError:
            logging.debug('my_list is {}'.format(self.numbers))
            print("You did not input a list of numbers")
        except ValueError:
            print("The input type is correct but inappropriate")

        self.output_min_max = ((np.max(self.numbers)), (np.min(self.numbers)))

    def return_max_diff(self):
        """Function will return maximum difference between adjacent numbers.

        Function takes in the inputted list of values, splits it into two
        arrays to calculate the difference between adjacent values, takes the
        absolute values of the differences to disregard positioning, and then
        outputs the maximum value.

        :param self: List of numbers
        :return: Maximum difference
        :raises ImportError: Check if numpy is installed or
        virtual env is established
        :raises TypeError: Input not given as a list of values
        :raises ValueError: Can occur when only 1 number is given in the list
        """
        # Import pkgs
        import numpy as np
        import logging
        # Setup log
        logging.basicConfig(filename='fn3log.txt', level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        # Function
        try:
            logging.info('Start fn')
            if any(self.numbers) < 0:  # included to use warning
                logging.warning('Negative values in list')
                logging.debug('Values {}'.format(self.numbers))
            input_list = np.array(self.numbers)
            diffs = abs(np.diff(input_list))
            self.output_max_diff = max(diffs)

            logging.info('Max val: {}'.format(self.output_max_diff))
            # return max_val

        except ImportError:  # redundancy
            logging.debug('Values {}'.format(self.numbers))
            logging.error('ImportError: Check if numpy is in virtualenv')
            # print('Check if numpy is in virtualenv')
        except TypeError:
            logging.debug('Values {}'.format(self.numbers))
            logging.debug(self.numbers)
            logging.error('TypeError: Check if input is a list of values')
            # print('Check if input is a list of values')
        except ValueError:
            logging.debug('Values {}'.format(self.numbers))
            logging.error('ValueError: Add more numbers to the list')
            # print('Add more numbers to the list')
