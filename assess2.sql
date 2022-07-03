use ordersinfo;
 SELECT customer_id, MAX(purch_amt) 
FROM orders 
WHERE customer_id BETWEEN 3002 and 3007 
GROUP BY customer_id 
HAVING MAX(purch_amt)>1000;
