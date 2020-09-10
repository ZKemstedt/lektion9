-- 1. Write a SQL statement to display all the information of all salesmen
select * 
from salesman;

-- 6. Write a SQL statement to display specific columns like name and 
-- commission for all the salesmen.
select name, commission 
from salesman;

-- 7. Write a query to display the columns in a specific order like order
-- date, salesman id, order number and purchase amount from for all the orders
select ord_date, salesman_id, ord_no, purch_amt 
from orders 
order by salesman_id;

-- 9. Write a SQL statement to display names and city of salesman, who 
-- belongs to the city of Paris. 
select name, city 
from salesman 
where city='Paris';

-- 10. Write a SQL statement to display all the information for those
-- customers with a grade of 200.
select * 
from customer 
where grade=200;

-- 11. Write a SQL query to display the order number followed by order date
-- and the purchase amount for each order which will be delivered by the 
-- salesman who is holding the ID 5001.
select ord_no, ord_date, purch_amt
from orders
where salesman_id=5001;

-- 12. Write a SQL query to display the Nobel prizes for 1970.
select year, subject, winner
from nobel_win
where YEAR=1970;

-- 13. Write a SQL query to know the winner of the 1971 prize for Literature.
select winner
from nobel_win
where subject='Literature' and year=1971;

-- 14. Write a SQL query to display the year and subject that won
--  'Dennis Gabor' his prize.
select year, subject
from nobel_win
where winner='Dennis Gabor';

-- 15. Write a SQL query to give the name of the 'Physics' 
-- winners since the year 1950. 
select winner
from nobel_win
where subject='Physics' and year>=1950;

-- 16. Write a SQL query to Show all the details 
-- (year, subject, winner, country) of the Chemistry prize winners between 
-- the year 1965 to 1975 inclusive.
select *
from nobel_win
where subject='Chemistry' and year<=1975 and year>=1965;