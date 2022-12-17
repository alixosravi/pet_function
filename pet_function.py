def prob_to_name(p_cat: float, breed: str, owner=None, pet_age=5) -> str:
  ''' 
  predict between cat and dog and print message
  '''
  if  p_cat > 0.5:
    prediction = 'Cat'
  elif p_cat < 0.5:
    prediction = 'Dog'
  else:
    prediction = "Unknown"

  if owner is not None:
    print(f"{owner} has a {breed} {prediction} who's {pet_age} years old!")
  else:
    print(f"This {breed} is {prediction} {pet_age} years old!")
  return prediction

def print_name(name):
  '''
  Simple function to print name
  input: name
  '''
  # Simple function to print name
  print(f"Hello! {name}")
