-- QUERY 1 - update the reports that have the same violation summary as at least 50 reports
WITH repeat_summary AS (SELECT violation_summary, COUNT(*)
FROM cts_forms_report 
GROUP BY violation_summary
HAVING count(*) > 50 )
UPDATE cts_forms_report
SET by_repeat_writer = true
WHERE id IN
(SELECT report.id
FROM cts_forms_report report
JOIN repeat_summary
ON report.violation_summary = repeat_summary.violation_summary
ORDER BY report.violation_summary);


-- QUERY 2 - update the reports that were submitted by individuals who have received a repeat writer email.  
-- BUG: This won't find the contact emails from reports where a user printed a Contact Complainant Template, but didn't email the individual.
UPDATE cts_forms_report
SET by_repeat_writer = true
WHERE contact_email IN (
SELECT array_to_string(regexp_matches(description, '\w+@\S+', 'g'), ';') FROM actstream_action act
WHERE act.verb = 'Contacted complainant:' 
AND act.description LIKE '%Constant Writer%');

