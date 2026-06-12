-- Write your query below
select customers.customer_id, customer_name
from customers, orders
where orders.customer_id = customers.customer_id
and
product_name = 'A'
intersect
select customers.customer_id, customer_name
from customers, orders
where orders.customer_id = customers.customer_id
and
product_name = 'B'
except
select customers.customer_id, customer_name
from customers, orders
where orders.customer_id = customers.customer_id
and product_name = 'C'
order by customer_name
