-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name genre, COUNT(*) number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
