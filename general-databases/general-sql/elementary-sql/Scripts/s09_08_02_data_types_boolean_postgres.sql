/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

create table if not exists t1 (
	a boolean
);

insert into t1 values
	('true'),
	('yes'),
	('on'),
	('1'),
	('false'),
	('no'),
	('off'),
	('0')
;

select * from t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
