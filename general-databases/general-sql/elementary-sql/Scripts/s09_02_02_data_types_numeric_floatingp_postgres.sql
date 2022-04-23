/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

CREATE TABLE IF NOT EXISTS t1 (
    d DECIMAL,
    e NUMERIC,
    f REAL,
    g DOUBLE PRECISION
);

/*
 * double - variable
 */
insert into t1(d) values
    (42),
    (42.3),
    (.9),
    (.007),
    (525215215.123456789123456789),
    (5e3),  -- 5 * 10 ^3
    (1234e-2)  -- 1234 * 10^(-2) = 1234 * 1/100;

-- title: double
select d from t1;
delete from t1;

/*
 * numeric - variable
 */
insert into t1(e) values
    (42),
    (42.3),
    (.9),
    (.007),
    (525215215.123456789123456789),
    (5e3),  -- 5 * 10 ^3
    (1234e-2)  -- 1234 * 10^(-2) = 1234 * 1/100;

-- title: numeric
select e from t1;
delete from t1;

/*
 * real - 4 bytes (6 decimal places)
 */
insert into t1(f) values
    (42),
    (42.3),
    (.9),
    (.007),
    (525215215.123456789123456789),
    (5e3),  -- 5 * 10 ^3
    (1234e-2);  -- 1234 * 10^(-2) = 1234 * 1/100

-- title: real
select f from t1;
delete from t1;

/*
 * double precision - 8 bytes (15 decimal places)
 */
insert into t1(g) values
    (42),
    (42.3),
    (.9),
    (.007),
    (525215215.123456789123456789),
    (5e3),  -- 5 * 10 ^3
    (1234e-2);  -- 1234 * 10^(-2) = 1234 * 1/100

-- title: double precision
select g from t1;
delete from t1;

/*
 * infinities and NaN
 */
insert into t1 values
    ('Infinity', 'Infinity', 'Infinity', 'Infinity'),
    ('-Infinity', '-Infinity', '-Infinity', '-Infinity'),
    ('NaN', 'NaN', 'NaN', 'NaN');

-- title: special values
select * from t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
