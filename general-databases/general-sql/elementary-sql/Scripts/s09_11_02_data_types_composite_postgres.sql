/*
 * Postgres has static typing
 */

-- setup

DROP TABLE IF EXISTS t1;

-- main start


drop type if exists Ship;
drop type if exists ShipClass;
drop type if exists Commander;

create type Commander as (
	name varchar,
	rank varchar
);

create type ShipClass as (
	title varchar,
	designation varchar
);

create type Ship as (
	name varchar,
	commander Commander,
	shipClass ShipClass
);

create table if not exists t1 (
	id serial,
	ship Ship
);

insert into t1(ship) values
	(
		row(
			'Excalibur',
			row('Jack O''Harra', 'Admiral'),
			row('Destroyer', 'Fleet 4B')
		)
	),
	
	(
		row(
			'Poseidon',
			row('Samuel Rowan', 'Operations chief'),
			row('Aircraft carrier', 'Div. 562')
		)
	),
	
	(
		row(
			'Waterhorse',
			row('Cassidi Kerst', 'Leutenant Caporal'),
			row('Frigate', '8349')
		)
	)
;

SELECT *, (ship).commander, (ship).shipClass FROM t1;

-- main end

-- cleanup

DROP TABLE IF EXISTS t1;

drop type if exists Ship CASCADE;
drop type if exists ShipClass CASCADE;
drop type if exists Commander CASCADE;
