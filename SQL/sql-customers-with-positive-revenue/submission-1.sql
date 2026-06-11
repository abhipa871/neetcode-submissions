-- Write your query below
Select distinct customer_id
from customers
where customers.revenue>0 
and customers.year=2020