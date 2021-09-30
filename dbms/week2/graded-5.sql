select faculty_fname, faculty_lname
from faculty, departments
where faculty.department_code = departments.department_code and department_name = 'Computer Science'
;
