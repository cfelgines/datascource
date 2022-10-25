from Get_info.print_info_movie import PrintInfoMovie
from PIL import Image

movieSearchTitle=input("What movie are you looking for ?")

print(PrintInfoMovie.find_rating(movieSearchTitle).content['imDb'])

print(Image.open('https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_Ratio0.6762_AL_.jpg') )