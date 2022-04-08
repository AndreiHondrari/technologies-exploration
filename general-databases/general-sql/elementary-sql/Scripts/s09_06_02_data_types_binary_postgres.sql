/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

create table if not exists t1 (
	a bytea
);

insert into t1 values
	('\xffe3cd'),
	('\000'),
	('\047'),
	('\127')
;

-- titles: binary (bytea)
select 
	a, 
	encode(a, 'hex') as hex, 
	encode(a, 'escape') as escape
from t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
