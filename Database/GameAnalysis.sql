select round(
(select count(distinct player_id) from activity where (player_id,event_date) in 
(select player_id,date_add(min(event_date),interval 1 day) from activity  group by player_id ))
/count(distinct player_id)
,2) AS fraction
from activity