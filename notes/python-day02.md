> Python is dynamically typed language -> variable declaration is not mandatory, type checking is done at runtime
> Difference between equality(==) and identity(is) -> equality checks whether object have equal value/content, whereas identity checks whether objects are referring to same exact object
> Difference between append() and + -> append mutates existing list whereas + creates a new list
> Shallow copy vs deep copy -> shallow copy is when only outer object gets copied, but nested objects are still the same (happens like in list.copy()), whereas deepcopy is when nested objects are also created as separate objects (import copy -> copy.deepcopy(list))
> Read a.copy() as shallow copy of a
> Immutables -> int, bool, float, str, tuple, frozenset, bytes
> Mutables -> list, dict, set, custom class instances
> There can be mutable objects within immutable objects/containers. for instance a tuple of lists. the lists within the tuple can be modified.
> Del removes name/reference but not the object itself. the object will be there as long as some name/reference is binding the object.
> Python golden sentence -> names refer to objects, some objects can change in-place; some cannot.
> Truthiness -> Python can treat many values in their boolean context, like 0, 0.0, (), [], None, "", or any kind of blank value is treated as False. Any other value is treated as True.
> Short-circuiting -> Python does not evaluate the other condition of 'and' if the first condition is false, and if the first condition is True in case of 'or'
> and/or sometimes return actual values rather than boolean. For instance -> print(0 or 5) // prints 5. print(10 and 20) // prints 20 (10 is truthy so it went till second operand where it found 20 which is truthy too, so prints 20)
> String is sequence of characters. Sequence enables slicing, indexing and ordering.
> String is immutable because Dictionaries and set rely on hash of the keys, since string cannot be changed so its hash values are calculated once and stored for lifetime. If the strings were changable, the hash values would change, potentially losing the item inside set or dictionary.
> In slice[start:end] -> start value is included, end is excluded in the range of values
> By default input() always takes in value as a string