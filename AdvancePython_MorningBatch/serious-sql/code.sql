SELECT * FROM some_table


SELECT
  column_name_1,
  column_name_2
FROM schema_name.table_name

SELECT * FROM dvd_rentals.language;

SELECT
  language_id,
  name
FROM dvd_rentals.language;

SELECT *
FROM dvd_rentals.actor
LIMIT 10;

SELECT country
FROM dvd_rentals.country
ORDER BY country
LIMIT 5;

SELECT
  total_sales
FROM dvd_rentals.sales_by_film_category
ORDER BY 1
LIMIT 5;

SELECT country
FROM dvd_rentals.country
ORDER BY country DESC
LIMIT 5;

SELECT
  category,
  total_sales
FROM dvd_rentals.sales_by_film_category
ORDER BY total_sales
LIMIT 1;

SELECT
  payment_date
FROM dvd_rentals.payment
ORDER BY payment_date DESC
LIMIT 1;

DROP TABLE IF EXISTS sample_table;
CREATE TEMP TABLE sample_table AS
WITH raw_data (id, column_a, column_b) AS (
 VALUES
 (1, 0, 'A'),
 (2, 0, 'B'),
 (3, 1, 'C'),
 (4, 1, 'D'),
 (5, 2, 'D'),
 (6, 3, 'D')
)
SELECT * FROM raw_data;

SELECT * FROM sample_table
ORDER BY column_a, column_b;

SELECT * FROM sample_table
ORDER BY column_a DESC, column_b;

SELECT * FROM sample_table
ORDER BY column_a DESC, column_b DESC;

SELECT * FROM sample_table
ORDER BY column_b DESC, column_a;

SELECT * FROM sample_table
ORDER BY column_b, column_a DESC;

WITH test_data (sample_values) AS (
VALUES
(null),
('0123'),
('_123'),
(' 123'),
('(abc'),
('  abc'),
('bca')
)
SELECT * FROM test_data
ORDER BY 1;

WITH test_data (sample_values) AS (
VALUES
(null),
('0123'),
('_123'),
(' 123'),
('(abc'),
('  abc'),
('bca')
)
SELECT * FROM test_data
ORDER BY 1 NULLS FIRST;

WITH test_data (sample_values) AS (
VALUES
(null),
('0123'),
('_123'),
(' 123'),
('(abc'),
('  abc'),
('bca')
)
SELECT * FROM test_data
ORDER BY 1 DESC NULLS FIRST;

select city from station where city REGEXP "^[aeiou].*";

select name 
from students 
where marks > 75
order by right (name,3), ID ;
