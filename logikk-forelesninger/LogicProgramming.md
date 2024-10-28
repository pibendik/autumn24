okt 24.

SLD resolution

Horn Clause (contains one positive literal) <- what is a positive literal? A: it's a non-negated literal!
A definite clause is a Horn clause that contains a positive literal.

Selective Linear Definite clause resolution is the inference rule used in logic programming

Facts:
{A}

How does prolog work?

It's declarative.
from 1970s
PROgramming in LOGic
specify the problem, let the machine solve it.

an algorithm = logic + control

Sample Prolog Programs

1. Factorial Calculation:

```prolog
factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, Result1),
    Result is N * Result1.
```

2. Fibonacci Sequence:

```prolog
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, Result1),
    fibonacci(N2, Result2),
    Result is Result1 + Result2.
```

3. List Manipulation - Append:

```prolog
append([], L, L).
append([H|T], L, [H|Result]) :-
    append(T, L, Result).
```

4. List Manipulation - Reverse:

```prolog
reverse([], []).
reverse([H|T], Result) :-
    reverse(T, ReverseT),
    append(ReverseT, [H], Result).
```

5. Palindrome Check:

```prolog
palindrome(List) :-
    reverse(List, List).
```

6. Family Relationships:

```prolog
parent(john, jim).
parent(john, ann).
parent(jim, lisa).
parent(ann, lisa).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).
```

Feel free to modify and experiment with these sample programs to learn more about Prolog!

Prolog's lists with the [H|T] head-tail structure are similar to LISP list programming in terms of representing lists. In Prolog, [H|T] represents a list where H is the head (first element) and T is the tail (rest of the list). This structure allows for easy pattern matching and recursive operations on lists.

In LISP, the equivalent structure is represented using the car and cdr functions. The car function retrieves the first element of the list, while the cdr function retrieves the rest of the list. Together, they provide similar functionality to Prolog's [H|T] structure.

Both Prolog and LISP provide powerful list manipulation capabilities. However, it's important to note that LISP has a more extensive set of built-in functions and features specifically designed for working with lists, making it a more specialized language for list processing.

Sure! Here are some examples of how lists work in Prolog and LISP:

Prolog:

1. Creating a list: `[1, 2, 3, 4]`
2. Accessing the head of a list: `head([1, 2, 3, 4], H)` (H will be bound to 1)
3. Accessing the tail of a list: `tail([1, 2, 3, 4], T)` (T will be bound to [2, 3, 4])
4. Appending two lists: `append([1, 2], [3, 4], Result)` (Result will be bound to [1, 2, 3, 4])
5. Checking if a list is empty: `isEmpty([])` (returns true if the list is empty)

LISP:

1. Creating a list: `(list 1 2 3 4)`
2. Accessing the first element of a list: `(car '(1 2 3 4))` (returns 1)
3. Accessing the rest of the list: `(cdr '(1 2 3 4))` (returns (2 3 4))
4. Appending two lists: `(append '(1 2) '(3 4))` (returns (1 2 3 4))
5. Checking if a list is empty: `(null '(1 2 3 4))` (returns false if the list is not empty)

These examples demonstrate basic operations on lists in Prolog and LISP. Remember that both languages have more advanced list manipulation capabilities and built-in functions for working with lists.

The "cut" or "!" in Prolog is not something that you would write in the list of rules. It is a special built-in predicate that affects the control flow of Prolog programs. The cut predicate is denoted by the symbol "!".

Here are a few examples of how the cut predicate can be used in Prolog:

1. Cut to prune alternative solutions:

```prolog
even(X) :-
    integer(X),
    X mod 2 =:= 0,
    !.
even(X) :-
    integer(X),
    X1 is X - 1,
    even(X1).
```

In this example, the cut predicate is used to prune alternative solutions. Once a solution is found for the first rule, the cut is executed, preventing Prolog from backtracking and searching for alternative solutions.

2. Cut to control backtracking:

```prolog
member(X, [X|_]) :- !.
member(X, [_|T]) :-
    member(X, T).
```

In this example, the cut predicate is used to control backtracking. Once a match is found in the first rule, the cut is executed, preventing Prolog from backtracking and searching for additional matches.

3. Cut to improve efficiency:

```prolog
fibonacci(0, 0) :- !.
fibonacci(1, 1) :- !.
fibonacci(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, Result1),
    fibonacci(N2, Result2),
    Result is Result1 + Result2.
```

In this example, the cut predicate is used to improve efficiency. Once the base cases are matched, the cut is executed, preventing unnecessary backtracking and improving the performance of the Fibonacci calculation.

These examples demonstrate different use cases of the cut predicate in Prolog. It is important to use the cut carefully, as it can have a significant impact on the behavior and efficiency of Prolog programs.
