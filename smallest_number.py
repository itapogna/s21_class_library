def smallest_number(*, the_list, the_item):
  new_list = [item for item in the_list if item < the_item] 
  return new_list
