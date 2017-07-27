def closest_power(base, num):
  '''
  base: base of the exponential, integer > 1
  num: number you want to be closest to, integer > 0
  Find the integer exponent such that base**exponent is closest to num.
  Note that the base**exponent may be either greater or smaller than num.
  In case of a tie, return the smaller value.
  Returns the exponent.
  '''

  # Ensure type
  num = int(num)
  base = int(base)

  print("Base: {}, Num: {}".format(base,num))
  # Create a method that populates an initial guess for comparison to number
  power_min = 0
  power_max = num // 2

  best_dist = base**power_max
  best_guess = 0
  pow_track = 0

  while True:
    #generate a new power guess by bisection
    pow_guess = (power_min + power_max) // 2
    print ("Pow guess: {}".format(pow_guess))

    #calculate the value and distance from num
    val = base**pow_guess
    dist = abs(val - num)
    print ("Current pow_min: {}, pow_max: {}".format(power_min, power_max))
    print ("current val: {}, num: {}".format(val, num))
    print ("Current guess_dist: {}, best dist: {}".format(dist,best_dist))
    if dist < best_dist:
        best_dist = dist
        best_guess = pow_guess
    elif dist == best_dist:
        best_guess = min(pow_guess, best_guess)
        print (best_guess)
        break
    else:
        if pow_track == pow_guess:
            print ("pow_track == pow_guess")
            break
        else:
            pow_track = pow_guess

    #check whether guess is above, below, or equal to number
    if val > num:
        power_max = pow_guess
        print ("guess > num, new power_max: {}".format(power_max))
    elif val < num:
        power_min = pow_guess
        print ("guess < num, new power_min: {}".format(power_min))
    else:
        #if value equals num, found it
        break

  # return guess
  print (best_guess)

closest_power(2, 192)
#closest_power(7, 196)
#closest_power(4, 1)
