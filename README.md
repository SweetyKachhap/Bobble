# Bobble Assignment

This code is written to run in local
#Steps
1. Clone this code into local machine
2. Setup postgresql database
3. Add configurations into config file
4. Go to settings of DataInjection file and click on modifyRunConfiguration, add "config.json" in parameter
5. run DataInjection file
6. Similarly add "confi.json" to parameter of MovieApi file and run MovieApi file

# How to use API
1. In your browser hit API endpoint - /v1/movie/movieId
2. movieId is an integer which refers to the id of the movie you want to fetch
3. for example - http://127.0.0.1:5000/v1/movie/1
