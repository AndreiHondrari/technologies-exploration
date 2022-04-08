/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t3;

-- main start

/*
 * char vs varchar behaviour of fixed-size
 */
CREATE TABLE IF NOT EXISTS t1 (
	a char(10),  -- also character(n)
	b varchar(10)  -- also varying character(n)
);

insert into t1 values
	('kek', 'lol'),
	('12345 ', '12345 '),  -- 1 space
	('12345   ', '12345   ')  -- 3 spaces
;

insert into t1(a) values ('01234567890') -- 11 chars | yields error
;

insert into t1(b) values ('01234567890') -- 11 chars
;

-- title: a vs b
select 
	a, char_length(a), format('%s_', a), 
	b, char_length(b), format('%s_', b)  
from t1;

/*
 * char vs varchar no size specified
 */
create table if not exists t2 (
	c char, -- equivalent of char(1)
	d varchar -- accepts text of any length (no errors)
);

insert into t2(c) values ('a');
insert into t2(c) values ('bc');  -- yields error
insert into t2(d) values ('a');
insert into t2(d) values ('bc');

-- title: non-fixed char vs varchar
select * from t2;

/*
 * text
 */
create table if not exists t3 (
	x text,  -- similar to varchar without size
	y varchar
);

insert into t3 values 
	('a     ', 'a     '),
	('abcde     ', 'abcde     '),
	(
		'e48f84bd-47e7-4fcd-b6fa-bbf3dfa94057     ', 
		'e48f84bd-47e7-4fcd-b6fa-bbf3dfa94057     '
	)
;

-- title: text vs varchar
select 
	x, format('%s_', x), 
	y, format('%s_', y)	
from t3;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
DROP TABLE IF EXISTS t3;
