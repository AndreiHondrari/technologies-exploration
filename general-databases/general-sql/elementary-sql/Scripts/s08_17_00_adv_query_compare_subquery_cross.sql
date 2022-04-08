/*
 * OBSERVATION - SOLELY EXPLANATORY (DON'T RUN)
 * 
 * Explains difference between Sqlite and Postgres
 * when performing 
 * WHERE x operator (subquery)
 */


create table if not exists t1 (
    a int
);

create table if not exists t2 (
    b int
);


/*
 * In Sqlite this will work by 
 * comparing a to all values in subquery
 * 
 * In Postgres the subquery is supposed to return
 * only one column and one row.
 * Running a comparison against multiple rows
 * relies on operators ANY/SOME/ALL
 */
select a from t1
where a > (select b from t2);


/*
 * just in case you did call the script ..cleaning up
 */
drop table if exists t1;
drop table if exists t2;
