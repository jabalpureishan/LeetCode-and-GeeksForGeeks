select user_id,max(time_stamp) as last_stamp
from (
select user_id,time_stamp
from logins
where time_stamp like '2020%'
order by time_stamp desc) as  subquery
group by user_id