/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

CREATE TABLE IF NOT EXISTS t1 (
	value money
);

insert into t1 values 
	(-92233720368547758.08),
	(92233720368547758.07),
	(42.99)
;

select * from t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
