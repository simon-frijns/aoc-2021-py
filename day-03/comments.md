# Comments

## Part 1

### Approach

Pivot the table, count the digits in each row and compute gamma and epsilon in one pass.

### Thoughts

Can probably generalise part of this with what we do for part 2, but felt like it was clean enough this way.
I bet that you could use some basic equation to "flip" gamma around into epsilon, but didn't look into it.

## Part 2

### Approach

Recursion to dig through the columns and drop irrelevant subset after each pass, then breaking once length 1 is reached.

### Thoughts

Not too clean to use a default parameter but passing 0 when calling also felt meh. 