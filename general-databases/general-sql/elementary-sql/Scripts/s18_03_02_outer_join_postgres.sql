/*
 * JOIN - combines columns from multiple tables
 */

drop table if exists t1;
drop table if exists t2;

create table if not exists t1 (
    k int, 
    y int
);

create table if not exists t2 (
    a text, 
    k int
);

insert into t1 values
    (11, 777), 
    (22, 888), 
    (33, 999), 
    (11, 1010),
    (66, 888)
;

insert into t2 values
    ('a', 55), 
    ('b', 22), 
    ('c', 11),
    ('b', 77),
    ('d', 22)
;

-- title: left outer join
select *
from t1 left outer join t2
on t1.k = t2.k;

-- title: right outer join
select * 
from t1 right outer join t2
on t1.k = t2.k;

-- title: full outer join
select * 
from t1 full outer join t2
on t1.k = t2.k;


drop table if exists t1;
drop table if exists t2;
