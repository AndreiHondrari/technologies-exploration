/*
 * Postgres does not allow primary keys to be null
 */
drop table if exists t1;

create table if not exists t1 (
    pk integer primary key,
    x integer unique
);

insert into t1(x) values (1, 11) (2, 22), (3, 33);

SELECT * FROM t1;

drop table if exists t1;


