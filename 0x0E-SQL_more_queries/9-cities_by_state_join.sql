/* Cities of States */

-- Script that lists all cities contained in the database hbtn_0d_usa

--	Each record should display: cities.id - cities.name - states.name
--	Results must be sorted in ascending order by cities.id
--	only one SELECT statement

    SELECT cities.id, cities.name, states.name
  	  FROM states
INNER JOIN cities
		ON states.id = cities.state_id
  ORDER BY cities.id;
