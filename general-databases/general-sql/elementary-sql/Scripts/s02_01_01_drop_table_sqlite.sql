/*
 * Drop a table
 * 
 * Observations:
 * - second drop will yield an exception because the table will have been dropped in the first drop instruction
 */

CREATE TABLE IF NOT EXISTS some_table (
	x integer
);

DROP TABLE some_table;
DROP TABLE some_table;  -- this will fail