/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start

create table if not exists t1 (
	a date,
	b time,
	c timestamp,
	d interval
);

/*
 * date
 */
insert into t1(a) values
	('1947-06-26'),
	('February 1, 2000'),
	('05/02/2002'),
	('1999-03-04')
;

-- title: date
select a from t1;

delete from t1;

/*
 * time
 */

insert into t1(b) values
	('12:07'),
	('13:08:45'),
	('14:09:55.768'),
	('12:07+3')
;

-- title: time
select b from t1;

delete from t1;

/*
 * timestamp
 */

insert into t1(c) values
	('1947-06-26 12:08:45'),
	('1947-06-26 12:08:45 +3:00')
;

-- title: timestamp
select c from t1;

delete from t1;

/*
 * special values
 */

insert into t1(b, c) values
	(null, 'epoch'),
	(null, 'infinity'),
	(null, '-infinity'),
	(null, 'now'),
	(null, 'today'),
	(null, 'yesterday'),
	('allballs', null)
;

-- title: special
select b, c from t1;

delete from t1;

/*
 * interval
 */

insert into t1(d) values
	('1-2'),
	('3 4:05:06')	,
	('1 year 2 months 3 days 4 hours 5 minutes 6 seconds'),
	('P1Y2M3DT4H5M6S'),
	('P0001-02-03T04:05:06')
;

-- title: interval
select d from t1;

delete from t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;
