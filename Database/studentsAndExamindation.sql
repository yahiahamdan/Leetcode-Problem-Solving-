# Write your MySQL query statement below
select st.student_id ,st.student_name ,s.Subject_name,count(e.student_id) as attended_exams
from students st cross join subjects s  
left join examinations e 
on e.student_id =st.student_id and e.subject_name =s.subject_name
group by st.student_id,st.student_name,s.subject_name
order by st.student_id ,st.student_name