/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

CREATE TABLE IF NOT EXISTS t1 (
    a SMALLINT,
    b INTEGER,
    c BIGINT
);

/*
 * small int - 2 bytes
 */
insert into t1(a) values
    (-32768),
    (32767);

insert into t1(a) values 32768; -- out of range

-- title: smallint
select a from t1;
delete from t1;

/*
 * integer - 4 bytes
 */
insert into t1(b) values
    (-2147483648),
    (2147483647);

insert into t1(b) values 2147483648; -- out of range

-- title: integer
select b from t1;
delete from t1;

/*
 * bigint - 8 bytes
 */
insert into t1(c) values
    (-9223372036854775808),
    (9223372036854775807);

insert into t1(c) values 9223372036854775808; -- out of range

-- title: bigint
select c from t1;
delete from t1;


-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
