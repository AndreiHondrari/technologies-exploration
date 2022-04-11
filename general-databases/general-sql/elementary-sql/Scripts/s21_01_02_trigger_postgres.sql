
drop table if exists t1;
drop table if exists t2;

create table if not exists t1 (
    descr text
);

create table if not exists t2 (
    descr_copy text
);

/*
 * create a trigger
 */
create or replace function mytrigger_procedure()
returns trigger
as $$
    begin
        /*
         * notice that NEW is available
         * in this local scope.
         * 
         * Postgres automatically passes NEW and OLD
         * to the PL/pgSQL block
         */
        insert into t2 values (new.descr);
        return new;
    end;
$$ language plpgsql;

create or replace trigger mytrigger
after insert on t1
for each row
execute procedure mytrigger_procedure();

/*
 * do some inserts
 */
insert into t1 values ('gandalf'), ('maxime');

select * from t1;
select * from t2;

-- cleanup
drop trigger if exists mytrigger on t1;
drop function if exists mytrigger_procedure;

drop table if exists t1;
drop table if exists t2;
