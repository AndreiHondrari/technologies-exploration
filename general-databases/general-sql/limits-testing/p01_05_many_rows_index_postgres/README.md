# Index on a large table

## Overview

Supposedly indexes are useful for speeding up queries on large tables. We will
explore that theory in this test.

## Pre-steps

Run

- `python 01_setup.py` - create the table
- `python 02_insert_many_rows.py` - insert 10 million + 1 rows

Notice that the last row inserted is distinct from the previous 10 million to
help us evaluate the performance compared to the worst case scenario, where the
database engine has to iterate over all 10 million rows before finding our
match. The previous 10 million rows have a value column in the range 100, 1000,
whilst the last row has the value 9999.

## Steps

Run

- `python 03_query_conditioned.py` - will search for the value 9999. Notice that
  this query runs before we have any index created. Observe the execution time.
- `python 04_create_index.py` - will create our index on the value column
- `python 03_query_conditioned.py` - rerun the first query. Notice the execution
  time now.

At this point feel free to call `05_drop_index.py` and the other scripts (**03**
and **04**) as many times and in any order you like.

## Observations

On my machine (MacBook Pro, Intel Core i7 with 2.6 Ghz and 32G RAM memory),
running postgres in docker, I observe:

- pre-index query runs in 0.30 seconds (about 300 ms)
- index creation runs in about 5 seconds
- post-index query runs in 0.00 seconds (less than 10 ms)

I would say that's a huge increase in performance (at least a factor of 30 in
performance gain)
