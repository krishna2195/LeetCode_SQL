# Write your MySQL query statement below
SELECT s.student_id, s.student_name, sub.subject_name ,COUNT(e.subject_name) as attended_exams
FROM Students s CROSS JOIN Subjects sub left JOIN Examinations e
USING(student_id,subject_name)
GROUP BY s.student_id, e.subject_name,sub.subject_name
ORDER BY s.student_id,sub.subject_name