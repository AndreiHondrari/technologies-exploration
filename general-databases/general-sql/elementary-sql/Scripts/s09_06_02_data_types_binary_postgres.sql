/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

create table if not exists t1 (
	a bytea,
	b bit(3)
);

/*
 * bytea
 */
insert into t1(a) values
	('\xffe3cd'),
	('\000'),
	('\047'),
	('\127')
;

-- titles: bytea
select 
	a, 
	encode(a, 'hex') as hex, 
	encode(a, 'escape') as escape
from t1;

delete from t1;

/*
 * bit string
 */
insert into t1(b) values
	('001'),
	('101')
;

-- title: bit string
select b from t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
