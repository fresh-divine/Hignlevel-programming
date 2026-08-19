# recursion and iterative comparison

## Readability
The iterative is more readable due to the fact that it makes use of simpler code and is easy to understand.

## Efficiency

The iterative version is much more efficient.

The simple recursive Fibonacci implementation repeatedly calculates the same values. For example, calculating fibonacci(5) calculates some smaller Fibonacci values more than once.

Because of this repeated work, the basic recursive version becomes very slow as n gets larger.

The iterative version calculates each value only once and keeps track of the previous two values, making it much more efficient in both time and memory.

## Real-world choice

I would use the iterative version in a real program when performance matters. The recursive version is useful for learning recursion and understanding how the Fibonacci definition translates into code, but it is not a good choice for large inputs without optimization such as memoization.

Very large input test

With a very large Fibonacci input, the recursive version can become extremely slow because it creates a large number of repeated function calls.

It can also eventually produce a RecursionError when the call depth becomes too large. The exact behavior depends on the input and Python's recursion limit.

## Very large input test

With a very large Fibonacci input, the recursive version can become extremely slow because it creates a large number of repeated function calls.

It can also eventually produce a RecursionError when the call depth becomes too large. 