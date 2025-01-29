(* Non tail recursive solution *)
fun sum [] = 0
  | sum (x::xs) = x + (sum xs)

(*Tail recursive solution *)
fun tsum ([], acc) = acc
  | tsum (x::xs, acc) = tsum (xs, x + acc)

fun sum_tail_recursive L = tsum (L, 0)
