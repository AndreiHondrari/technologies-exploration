drop table if exists t1;

create table if not exists t1 (
    kek int,
    val int
);

-- this function
drop function if exists do_this;

create or replace function do_this()
returns void
as '
INSERT INTO t1 VALUES (55, 111);
' language sql;

-- that function
drop function if exists do_that;

create or replace function do_that()
returns void
as $$
INSERT INTO t1 VALUES (66, 222);
$$ language sql;

-- some function
drop function if exists do_some;

create or replace function do_some()
returns table (x int, y int)
language sql -- notice it can be specified before
as $$

insert into t1 
values (77, 333), (88, 444), (99, 555) 
returning kek, val;

$$;

-- call functions

-- title: do_this
select do_this();

-- title: do_that
select do_that();

-- title: do_some
select do_some();

-- result in t1
select * from t1;

-- cleanup
drop function if exists do_this;
drop function if exists do_that;
drop function if exists do_some;
drop table if exists t1;