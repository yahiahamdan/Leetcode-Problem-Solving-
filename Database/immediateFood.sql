# Write your MySQL query statement below
#write a solution to find how many orders are immediate 
select  round(sum(case when order_date=customer_pref_delivery_date then 1 else 0 end) *100/count(delivery_id),2)  as immediate_percentage   from Delivery  where (customer_id,order_date) in(  
select customer_id ,min(order_date)  from delivery 
group by customer_id
)
