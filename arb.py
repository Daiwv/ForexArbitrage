import requests
import config
payload = {"pairs" : "EURUSD,USDGBP,GBPEUR", "api_key" : config.API_KEY}
r = requests.get("https://forex.1forge.com/1.0.2/quotes", params = payload).json()
EURUSD = float(r[0]["ask"])
USDGBP = float(r[1]["ask"])
GBPEUR = float(r[2]["ask"])
def arb(c1,c2,c3):
    calc = c1*c2*c3
    profit = (calc-1)
    if calc is not 1:
        print("ARB " + str(profit))

arb(EURUSD,USDGBP,GBPEUR)
