
select u.unique_id as unique_id, e.name from Employees e left join EmployeeUNI u 
on e.id = u.id