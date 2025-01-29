(* Non tail recursive fibonacci function, which returns the nth fibonacci number *)
fun fib 0 = 1
  | fib 1 = 1
  | fib n = (fib n-1) + (fib n-2)

(* Tail recursive fibonacci function, returning the nth fibonacci number *)
fun fib'(0, a, b) = a
  | fib'(n, a, b) = fib'(n-1, a+b, a)
