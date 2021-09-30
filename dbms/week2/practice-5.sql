select student_fname, student_lname
from students, members
where students.roll_no = members.roll_no and member_type = 'PG'
;