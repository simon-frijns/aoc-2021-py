# Comments

## Part 1

### Approach

Zipping the list with itself offset by 1. 

### Thoughts

Straightforward as is to be expected from first few days. Initially summed booleans, changed this to a count as it seems cleaner.

## Part 2

### Approach

Using a rolling window to compute all sums of three, before calling the function from part 1 on the resulting sums list.

### Thoughts

Insight from other people's code is that you do not need to sum. A rolling window fundamentally just means "add 1 remove 1, FIFO":
```
current_window = [a, b, c]
next_window = [b, c, d]
current_window < next_window == [a, b, c] < [b, c, d] == a < d
```
