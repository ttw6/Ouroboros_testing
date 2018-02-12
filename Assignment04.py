# This is our first assignment as a group

def main():
   return_sum(my_list)
   return_min_max(my_list)
   return_max_difference(my_list)



def return_min_max(my_list):
   
   try:
       max_min = ((max(my_list), min(my_list)))
   except TypeError:
      print("You did not input a list of number")
   except ValueError:
      print("The input type is correct but inappropriate")   
   except ImportError:
      print("Could not import the list")
   
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

