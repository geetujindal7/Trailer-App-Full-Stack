import Movies_website
import fresh_tomatoes

#storing the informations in variables
frst_movie = Movies_website.Movie("GOLMAL AGAIN", "Ajay devgn",
                                  "https://in.bookmyshow.com/entertainment-news/wp-content/uploads/2017/10/golmaal-again.jpg",
                                  "https://www.youtube.com/watch?v=VgQUwsUHdqc")


scnd_movie = Movies_website.Movie("PADMAVAT", "Deepika padukon",
                                  "http://www.jagranimages.com/inext/padmaavat-instagram-pic-1.jpg",
                                  "https://www.youtube.com/watch?v=8YaF2m7hCx0")


third_movie = Movies_website.Movie("Tiger Zinda Hai", "salman khan",
                                   "http://www.bollywoodlife.com/wp-content/uploads/2017/11/tiger-zinda-hai-new-poster-081117.jpg",
                                   "https://www.youtube.com/watch?v=ePO5M5DE01I")


forth_movie = Movies_website.Movie("Welcome To New York", "Diljit dosanjh",
                                   "http://images.indianexpress.com/2018/01/welcome-to-new-york-poster-759.jpg",
                                   "https://www.youtube.com/watch?v=4dCJgNzgs3c")


fifth_movie = Movies_website.Movie("Welcome Back", "Akshay Kumar",
                                   "https://i.ytimg.com/vi/SIKfSPbsuyw/maxresdefault.jpg",
                                   "https://www.youtube.com/watch?v=SIKfSPbsuyw")


sixth_movie = Movies_website.Movie("Rocky Mental", "salman khan",
                                   "https://resizing.flixster.com/Ug9x4ZWjd1NsmU5ZJX7PPTiwFEM=/206x305/v1.bTsxMjQ3Mjc3NTtqOzE3NjA0OzEyMDA7NDgwOzY0MA",
                                   "https://www.youtube.com/watch?v=IQ3u9zHIuCA")


#storing the objects in list movies
movies = [frst_movie, scnd_movie, third_movie, forth_movie, fifth_movie, sixth_movie]
fresh_tomatoes.open_movies_page(movies)
