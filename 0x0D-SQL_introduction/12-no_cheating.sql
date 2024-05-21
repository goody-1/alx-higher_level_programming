/* cheating is bad */

-- Script that updates the score of Bob to 10 in the second_table
-- Use only Bob's name field

  UPDATE `second_table`
	 SET score = 10
   WHERE name = 'Bob';
