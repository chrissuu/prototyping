val rec fact = 
  (fn 0 => 1
    | x => x * fact(x - 1))
