/*
 * Drop a table if it exists
 * 
 * Observations:
 * - will run without any problems due to the IF EXISTS clause in the second drop instructions
 */

CREATE TABLE IF NOT EXISTS some_table (
	x integer
);

DROP TABLE some_table;
DROP TABLE IF EXISTS some_table;