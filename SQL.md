-- 1. Get all statuses, not repeating, alphabetically ordered
SELECT DISTINCT status
FROM tasks
ORDER BY status ASC;

-- 2. Get the count of all tasks in each project, order by tasks count descending
SELECT p.id, p.name, COUNT(t.id) AS task_count
FROM projects p
LEFT JOIN tasks t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY task_count DESC;

-- 3. Get the count of all tasks in each project, order by project names
SELECT p.id, p.name, COUNT(t.id) AS task_count
FROM projects p
LEFT JOIN tasks t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.name ASC;

-- 4. Get the tasks for all projects having the name beginning with "N"
SELECT t.*
FROM tasks t
JOIN projects p ON t.project_id = p.id
WHERE p.name LIKE 'N%';

-- 5. Get the list of all projects containing 'a' in the middle of the name, showing tasks count.
-- Includes projects without tasks and tasks with project_id = NULL
SELECT p.id, p.name, COUNT(t.id) AS task_count
FROM projects p
LEFT JOIN tasks t ON t.project_id = p.id
WHERE p.name LIKE '_a%'
GROUP BY p.id, p.name
ORDER BY p.name ASC;

-- 6. Get the list of tasks with duplicate names, ordered alphabetically
SELECT name, COUNT(*) AS count
FROM tasks
GROUP BY name
HAVING COUNT(*) > 1
ORDER BY name ASC;

-- 7. Get the list of tasks having several exact matches of both name and status from project 'Delivery', order by matches count
SELECT t.name, t.status, COUNT(*) AS matches
FROM tasks t
JOIN projects p ON t.project_id = p.id
WHERE p.name = 'Delivery'
GROUP BY t.name, t.status
HAVING COUNT(*) > 1
ORDER BY matches DESC;

-- 8. Get the list of project names having more than 10 tasks in status 'completed', ordered by project_id
SELECT p.name, p.id, COUNT(t.id) AS completed_count
FROM projects p
JOIN tasks t ON t.project_id = p.id
WHERE t.status = 'completed'
GROUP BY p.id, p.name
HAVING COUNT(t.id) > 10
ORDER BY p.id ASC;