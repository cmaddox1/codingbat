def squirrel_play(temp, is_summer):
  if temp>=60:
    if is_summer==True:
      if temp <=100:
        return True
      else:
        return False
    if is_summer==False:
      if temp<=90:
        return True
      else:
        return False
  else:
    return False