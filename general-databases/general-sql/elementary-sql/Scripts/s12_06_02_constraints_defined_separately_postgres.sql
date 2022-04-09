/*
 * defining with CONSTRAINT
 */
drop table if exists t1;

create table if not exists t1 (
    pk integer,
    x integer,
    
    constraint t1_pk primary key (pk)
);

insert into t1(pk, x) values (1, 11);
insert into t1(pk, x) values (2, 22);
insert into t1(pk, x) values (3, 33);

insert into t1(pk, x) 
values (2, 44)
on conflict 
    on constraint t1_pk 
    do nothing
;  -- should fail

select * from t1;

drop table if exists t1;

/*
 * defining without CONSTRAINT
 */
drop table if exists t2;

create table if not exists t2 (
    pk integer,
    x integer,
    
    primary key (pk)
);

insert into t2(pk, x) values (1, 11);
insert into t2(pk, x) values (2, 22);
insert into t2(pk, x) values (3, 33);
insert into t2(pk, x) 
values (2, 44)
on conflict
    on constraint t2_pkey
    do nothing
;  -- should fail

select * from t2;

drop table if exists t2;
