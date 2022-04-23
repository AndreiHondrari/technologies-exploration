
drop table if exists t1;
drop table if exists t2;

create table if not exists t1 (
    x int
);

create table if not exists t2 (
    a text
);

insert into t1 values
    (11),
    (22),
    (33);

insert into t2 values
    ('gandalf'),
    ('maxime'),
    ('jeff');

-- title: comma join
select * from t1, t2;

-- title: join (on true)
select * from t1 join t2 on true;

-- title: cross join
select * from t1 cross join t2;


drop table if exists t1;
drop table if exists t2;
