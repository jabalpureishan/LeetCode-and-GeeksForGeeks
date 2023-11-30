select class
from
(select class,count(class) as cnt
from Courses
group by class
having cnt>=5) as class
