datatype int_option = NONE | SOME of int

(* Gets the last element of a list *)
fun last([] : int list) : int_option = NONE
  | last(x::[] : int list) = SOME x
  | last(x::xs : int list) = last(xs)

(* Gets the last two elements of a list, in order *)
datatype tuple_option = NONE | SOME of int * int

fun last_two([] : int list) : tuple_option = NONE
  | last_two(x::y::[] : int list) = SOME (x, y)
  | last_two(x::xs : int list) = last_two (xs)

datatype int_option = NONE | SOME of int

fun at(n : int, [] : int list) : int_option = NONE
  | at(0 : int, x::xs) = SOME x
  | at(n : int, x::xs) = at (n -1, xs)

fun length([] : int list) = 0
  | length(x::xs : int list) = 1 + length(xs)

fun reverse([] : int list) = []
  | reverse(x::xs : int list) = reverse(xs) @ [x]

fun treverse([] : int list, accum : int list) = accum
  | treverse(x::xs : int list, accum : int list) = treverse(xs, x::accum)

fun rev(L : int list) = treverse(L, [])

fun is_palindrome(L : int list) : bool = (L = rev(L))