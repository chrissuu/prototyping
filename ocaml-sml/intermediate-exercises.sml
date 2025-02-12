datatype superlist = One of int | Many of superlist list

fun flatten([] : superlist list, accum : int list) : int list = accum
  | flatten(x :: xs, accum) = (
    case x of
      One (x) => x::flatten(xs, accum)
    | Many (X) => flatten(X, accum) @ flatten(xs, accum)
  )

val t1 = flatten ([One (1), Many [One (2), Many [One (3), One (4)], One (5)]], [])

fun compress([], prev : int) : int list = []
  | compress(x::xs, prev : int) : int list = (
    case x = prev of
      true => compress(xs, prev)
    | false => x::compress(xs, x)
  )

fun eliminate_duplicates([]) : int list = []
  | eliminate_duplicates(x::[]) : int list = [x]
  | eliminate_duplicates(x::y::L) : int list = (
    case x = y of
      true => x::compress(L, x)
    | false => x::compress(L, y)
  )

val hi = eliminate_duplicates([1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 1, 1])