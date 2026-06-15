# omdb_utils.py
import requests

def get_movie_details(title, api_key):

    url = f"https://www.omdbapi.com/?apikey={api_key}&t={title}"
    res = requests.get(url).json()
    print(res)
    if res.get("Response") == "True":
        result = res.get("Plot", "N/A"), res.get("Poster", "N/A")
        plot = result[0]
        poster = result[1]
        return plot, poster

    return "N/A", "N/A"
