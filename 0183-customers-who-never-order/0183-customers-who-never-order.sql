SELECT name AS Customers
FROM customers
Where id NOT IN(SELECT customerId FROM orders);
