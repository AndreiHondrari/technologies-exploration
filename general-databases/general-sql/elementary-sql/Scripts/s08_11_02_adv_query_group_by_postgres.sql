/*
 *
 */

-- setup
drop table if exists t1;
create table if not exists t1 (
    x integer,
    y integer
);

insert into t1 values
    (1, 11),
    (2, 22),
    (1, 33),
    (2, 44),
    (1, 33),
    (2, 44),
    (1, 55),
    (2, 44),
    (3, 66);

-- main start

-- title: group by one column
select x from t1 where x < 500 group by x;  -- will always pick the first match for a given grouping

-- title: count for each group
select x, COUNT(*) from t1 group by x;

-- title: conditional
select x, COUNT(*) from t1 where y > 40 group by x;

-- title: avg for group
select x, ROUND(AVG(y), 2) from t1 where x < 500 group by x;

-- title: group by multiple
select x, y from t1 where x < 500 group by x, y order by x, y;

/*
 * WILL THROW ERROR
 * the reason is because it wouldn't make sense to return
 * only 1 value of one column while grouping by another.
 * 
 * Example: Let's assume we have table (a int, b int) with values
 * (1, 11), (1, 22), (2, 33)
 * 
 * if the "SELECT * FROM table GROUP BY a;" were to work
 * how would the result be for a = 1 ? In column b 
 * there are 11 and 22 for the same a = 1, 
 * which one would you should display?
 * it wouldn't make sense to display only one of them.
 */
select * from t1 group by x;

-- main end

-- cleanup
drop table if exists t1;
