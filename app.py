import requests

url = "https://validate-vat-number.p.rapidapi.com/"

querystring = {"vat":"IT00960910396"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "6b2ee3d95cmsh23751573ba183b7p1f1807jsn3532d5b93d13",
	"X-RapidAPI-Host": "validate-vat-number.p.rapidapi.com"
}


response = requests.get(url, headers=headers, params=querystring)

print(response.json())