> List is a collection of mutable, ordered items
> Difference between sort() and sorted() -> sort() does in-place, sorted() returns new list
> append() vs extend() vs + -> append() adds one item to the list, extend() adds many items to the list, and + makes a new combined list
> Tuple is a collection of immutable, ordered items. A single element tuple -> (5,). If it was (5) without comma, it would be an int.
> Most useful feature of tuple -> tuple packing and unpacking
> Set is very good for checking whether something exists
> discard() and remove() both delete item from set, but in remove(), if x is absent it will throw error. Error is not generated in discard()
> pop() in set will remove any arbitrary element
> Set only supports hashable elements like int, str, tuple. We can't make a set of list, dict or set.
> Use list when: order matters, duplicates allowed, or indexing is needed
> Use set when: uniqueness needed, removing duplicates, checking membership or mathematical set operations needed
> Dict keys should be hashable and unique. Duplicate keys overwrite.