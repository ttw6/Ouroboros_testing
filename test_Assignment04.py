# this is our unit testing for assignment 04






# Second function
def test_return_min_max():
   from Assignment04 import return_min_max
   test_input_list = ([-1,5,8,100],[5,-8,9,45,88,34,65],[-5,8.234,-99023,342,9.452])
   test_output_values = ((100,-1),(88,-8),(342,-99023))

   for count, elem in enumerate(test_input_list):   #enuerate itirate and gives the index
      min_max_output = return_min_max(elem)
      assert min_max_output == test_output_values[count]
      assert isinstance(min_max_output, tuple) == True 

