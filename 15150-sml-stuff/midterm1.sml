datatype vote = A | B
type election = vote list

(* 
REQUIRES: true
ENSURES: result e => s, the sum of votes for A in e - sum of votes for B in e
*)
fun acc_result ([] : election, accum : int) : int = accum
  | acc_result (x::xs : election, accum : int) : int = (
    case x of 
      A => acc_result(xs, accum + 1)
    | B => acc_result(xs, accum - 1)
  )

fun result (L : election) : int = acc_result(L, 0)


fun acc_always_winning ([] : election, accum, res) = res
  | acc_always_winning (L : election, accum : int, false) : bool = false
  | acc_always_winning (x::xs : election, accum : int, res : bool) = (
    let
      val currCount = (
        case x of 
          A => accum + 1
        | B => accum - 1
      )
    in
      acc_always_winning (xs, currCount, currCount > 0 andalso res)
    end
  )

fun always_winning (x::xs : election) = (
    case x of 
      A => acc_always_winning(xs, 1, true)
    | B => false
)

fun election_map ([], v) = []
  | election_map (x::xs, v) = (v::x)::(election_map(xs, v))

fun all_elections (0) = [[]]
  | all_elections (n) = (
    let
      val allelections = all_elections(n-1)
    in
      election_map(allelections, A) @ election_map(allelections, B)
    end
  )

fun filter_elections ([] : election list, res : int, accum : election list) = accum
  | filter_elections (x::xs, res, accum) = (
    case result(x) = res of
      true => filter_elections(xs, res, x::accum)
    | false => filter_elections(xs, res, accum)
  )

fun all_perms (a, b) = filter_elections(all_elections(a+b), a-b, [])


datatype tree = Empty | Node of tree * int * tree

fun nextsmallest (Empty, lo, acc) = acc
  | nextsmallest (Node (l, x, r), lo, acc) = (
    case lo < x of
      true => Int.min(nextsmallest(l, lo, Int.min(x, acc)), nextsmallest(r, lo, Int.min(x, acc)))
    | false => Int.min(nextsmallest(l, lo, acc), nextsmallest(r, lo, acc))
  )

