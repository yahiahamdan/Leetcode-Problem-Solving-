""""
response .status_code 
response.txt 
res.sjon 
rep
"""

import requests



def get_discount_price(barcode):
    url = f"https://jsonmock.hackerrank.com/api/inventory?barcode={barcode}"
    response = requests.get(url)
    if response.status_code!=200:
        return -1
    resData=response.json()
    data=resData.get('data',[])
    if not data:
        return -1
    price=data.get('price',0)
    discount=data.get('discount',0)
    discountPirce=price-(price*discount/100)
    return  discountPirce

def getMovieData(title ,year):
    url=f"https://jsonmock.hackerrank.com/api/movies/search/?Title={title}&Year={year}"
    response=requests.get(url)
    if response.status_code!=200:
        return -1
    resData=response.json()
    data=resData.get('data',[])
    if not data:
        return -1
    return data[0].get('imdbID',-1)

print(getMovieData("spiderman",2010))

