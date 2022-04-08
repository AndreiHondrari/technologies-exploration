/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

CREATE TABLE IF NOT EXISTS t1 (
	h SMALLSERIAL,
	i SERIAL,
	j BIGSERIAL,
	
	k varchar
);

/*
 * all serial fields will increment
 * themselves at each insert
 */
insert into t1(k) values
	(null), (null), (null), (null), (null);

-- title: just inserts
SELECT * FROM t1;

/*
 * updates are allowed
 */
update t1
set h = 777, i = 888, j = 999 
where i = 3;

-- title: updated serial fields
SELECT * FROM t1;

insert into t1(k) values (NULL);

-- title: insert after update
SELECT * FROM t1;


update t1
set h = 7, i = 7, j = 7, k = 'before 7'
where i = 5;

insert into t1(k) values ('after 7');

-- title: kek
SELECT * FROM t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
