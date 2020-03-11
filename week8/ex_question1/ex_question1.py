import urllib.request
url = input("pls enter your url address if you want to download the data: \n")
file_name = "./downloaded.jpg"
urllib.request.urlretrieve(url, file_name)


#enter "http://i.guim.co.uk/img/media
# /fe1e34da640c5c56ed16f76ce6f994fa9
# 343d09d/0_174_3408_2046/master/34
# 08.jpg?width=300&quality=85&auto=
# format&fit=max&s=80a280664b70fa77e4bcb4cde3caf273"

#or enter any http:// files url.