import requests
from Get_info.get_key import GetKeyInfo

from Get_info.versioning_event import VersioningEvent


class IMDbResult:
    
    def get_infos(moviesearch):
        url = "https://imdb-api.com/en/API/SearchMovie/"+str(GetKeyInfo.get_key())+"/"+moviesearch
        response =  requests.get(url)
        return VersioningEvent(status_code=response.status_code, content=response.json())