# PEP 8

PEP 8 suggests unique styles of naming for different parts in the language. This makes it easy to distinguish which type corresponds to each name when reading code.

### Naming

- Functions, variables, and attributes should be in lowercase_underscore format.
- Protected instance attributes should be in \_leading_underscore format.
- Private instance attributes should be in \_\_double_leading_underscore format.
- Classes and exceptions should be in CapitalizedWord format.
- Module-level constants should be in ALL_CAPS format.
- Instance methods in classes should use self as the name of the first parameter (which refers to the object).
- Class methods should use cls as the name of the first parameter (which refers to the class).
- (id, str) are bad name variables

### Expressions and Statements

- Don’t check for empty values (like []) by checking the length (if len(somelist) == 0). Use if not somelist and assume empty values implicitly evaluate to False.
- Always use absolute names for modules when importing them, not names relative to the current module’s own path. For example, to import the foo module from the bar package, you should do from bar import foo, not just import foo
- If you must do relative imports, use the explicit syntax from . import foo.
