
drop view if exists view1;
drop view if exists view2;

drop table if exists t1;
drop table if exists t2;

create table if not exists t1 (
    x int,
    descr text
);

create table if not exists t2 (
    a int
);

insert into t1 values
    (11, 'gandalf'),
    (22, 'GANDHI'),
    (11, 'tree'),
    (11, 'forcefield'),
    (33, 'apples'),
    (66, 'sword'),
    (44, 'magical'),
    (88, 'startdust'),
    (22, 'quadrant'),
    (55, 'freaky'),
    (44, 'equation'),
    (99, 'equation'),
    (22, 'quasimodo'),
    (11, 'perfect'),
    (77, 'broken'),
    (77, 'magnificent'),
    (33, 'insane'),
    (55, 'juggernaut'),
    (55, 'fantasy'),
    (11, 'sorcerer'),
    (22, 'ak47'),
    (11, 'akko'),
    (33, 'akama');

insert into t2 values (11), (33);

/*
 * create some views
 */

create or replace view view1
as
    select * from t1 
    where x = 11;

create or replace view view2
as
    select t1.*
    from t1 inner join t2
    on t1.x = t2.a;

/*
 * use views
 */

-- title: view1
select * from view1;

-- title: view2
select * from view2;

drop view if exists view1;
drop view if exists view2;

drop table if exists t1;
drop table if exists t2;
