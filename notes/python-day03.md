> Use for loop when: every item needs to be traversed or range-based traversal or fixed count of traversals
> Use while loop when: condition-based repetition or stop point is dynamic
> pass: keyword that acts as placeholder, used to avoid empty block syntax error
> else in for-else is executed when the loop successfully finished execution. Else won't be executed if break occurs. Useful in searching elements within a list.
> function is a named block of reusable, modular code
> By default functions return None if no return is there
> function is input -> process -> output
> function parameter is name referring to passed object
> Required parameters are listed first in the function definition, then the optional parameters with default values are listed, otherwise it will throw error
> Default arguments of mutable objects are evaluated only once i.e. only when the function is called first time, later calls use the existing mutable object already created from the first call. Always use None as a placeholder for mutable default arguments.
> Multiple values are returned as tuple