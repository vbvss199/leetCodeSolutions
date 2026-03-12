# Write your MySQL query statement below
SELECT user_id,COUNT(follower_id) AS followers_count FROM Followers GROUP BY user_id ORDER BY user_ID ASC

-- or below version also works
-- SELECT user_id,COUNT(*) AS followers_count FROM Followers GROUP BY user_id
