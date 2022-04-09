drop table if exists t1;

create table if not exists t1 (
    a integer, 
    b integer,
    k varchar,
    
    PRIMARY KEY (a, b)
);

insert into t1 values
    (1, 11, 'blabla'),
    (2, 22, 'gandalf')
;

insert into t1 values (1, 33, 'maxime');

insert into t1 
values (2, 22, 'cassidi')
on conflict on constraint t1_pkey do nothing;  -- will fail

select * from t1;


drop table if exists t1;
