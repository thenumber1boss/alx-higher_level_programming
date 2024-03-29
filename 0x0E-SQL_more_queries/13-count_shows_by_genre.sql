-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.

SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
