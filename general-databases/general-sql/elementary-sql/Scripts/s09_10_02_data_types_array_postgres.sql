/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

create table if not exists t1 (
    a integer array
);

insert into t1 values
    ('{1, 2, 3}')
;

SELECT * FROM t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
drop type if exists somehow;
