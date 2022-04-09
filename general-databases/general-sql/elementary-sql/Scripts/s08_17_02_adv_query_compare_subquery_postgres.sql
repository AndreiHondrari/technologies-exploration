
drop table if exists t1;
drop table if exists t2;

create table if not exists t1 (
    a int
);

create table if not exists t2 (
    b int
);

insert into t1 values (11), (22), (33), (44), (55);

insert into t2 values (22), (44);

/*
 * subquery must have only one row and one column
 */
-- title: sole result
select a from t1
where a = (select b from t2 limit 1);

-- title: val > ANY
select a from t1
where a > ANY(select b from t2);

-- title: val in the > ALL
select a from t1
where a > all(select b from t2);

delete from t2;
insert into t2 values (9999);  -- over all the values in t1

-- title: val over > ALL
select a from t1
where a > all(select b from t2);

drop table if exists t1;
drop table if exists t2;
