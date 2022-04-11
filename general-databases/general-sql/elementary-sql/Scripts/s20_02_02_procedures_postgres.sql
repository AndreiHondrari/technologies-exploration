drop procedure if exists do_this;
drop table if exists t1;

create table if not exists t1 (
    kek text,
    val int
);

create or replace procedure do_this()
as $$
insert into t1 values 
    ('a', 111), 
    ('b', 222), 
    ('c', 333)
;
$$ language sql;

-- call n-times
call do_this();
call do_this();

select * from t1;


-- cleanup
drop procedure if exists do_this;
drop table if exists t1;