select d.name as doctor_name,count(p.id) as patient_count from doctors d
left join patients p on d.id=p.doctor_id
where p.treatment_date between curdate()-interval 1 week and curdate()
group by d.name 


