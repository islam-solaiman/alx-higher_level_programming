-- script that lists all cities contained in the database hbtn_0d_usa.
-- Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities where state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
