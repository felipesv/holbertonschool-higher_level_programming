-- list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
	ON tv_genres.id = tv_show_genres.show_id
WHERE tv_genres.name NOT IN (
	SELECT tv_genres.name
	FROM tv_show_genres
	INNER JOIN tv_shows
		ON tv_shows.id = tv_show_genres.show_id
		AND tv_shows.title = "Dexter"
	INNER JOIN tv_genres
		ON tv_genres.id = tv_show_genres.genre_id
	ORDER BY tv_genres.name ASC
)
ORDER BY tv_genres.name ASC;
