import media, fresh_tomatoes

#Instantiate Movies class with favorite movies
top_gun = media.Movies("Top Gun", "https://www.movieposter.com/posters/archive/main/15/A70-7600",
							"https://www.youtube.com/watch?v=qAfbp3YX9F0")
inception = media.Movies("Inception", "http://pm.b5z.net/i/u/6127364/i/inception_75_ezr2.jpg", 
								"https://www.youtube.com/watch?v=66TuSJo4dZM")
spiderman = media.Movies("Spider Man", "http://cdn.screenrant.com/wp-content/uploads/Original-Spider-Man-Movie-Poster.jpg", 
									"https://www.youtube.com/watch?v=FN3YaybNJ2s")
goodwill_hunting = media.Movies("Goodwill Hunting", "http://upload.wikimedia.org/wikipedia/id/6/69/Good_Will_Hunting_film.jpg",
							"https://www.youtube.com/watch?v=nH9LZOXBMUE")

movies = [top_gun, inception, spiderman, goodwill_hunting]
#Pass favorite movies as a list into open_movies_page function
fresh_tomatoes.open_movies_page(movies)