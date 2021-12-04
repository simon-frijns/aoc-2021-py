# Comments

## Part 1

### Approach

Parsing input, creating a nested list of all boards. For each board, create an equivalent "status" board in which we track for each digit whether it's been called.
For each number, we flip the status in each board. As soon as we find a winner, we compute the result.
Part 1 had me breaking out instantly when the first winner was found.

### Thoughts

Part 1 was done very quickly - finding the first win and breaking out instantly made this trivial.

## Part 2

### Approach

Part 2 adjusts this slightly. Easiest way I found to generalise both to a single function was to always run the entire thing, answer the 1st element of the dictionary for p1 and the last for p2.

### Thoughts

Pfff, this went through a lot of iterations, none of them particularly satisfying. Happy about two things - the way I compute sums for rows and columns (zips are lovely) and eventually finding a single way to do both parts.