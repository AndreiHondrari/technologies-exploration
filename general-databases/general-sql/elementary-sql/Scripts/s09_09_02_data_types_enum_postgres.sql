/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

drop type if exists somehow;

create type somehow 
as enum ('like-this', 'like-that', 'noway');

create table if not exists t1 (
    a somehow,
    b varchar
);

insert into t1 values
    ('like-this', 'gandalf'),
    ('like-this', 'maxime'),
    ('like-that', 'gnocchi'),
    ('noway', 'chuck');

select * from t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
drop type if exists somehow;
