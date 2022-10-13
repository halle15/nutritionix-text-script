from inspect import classify_class_attrs
from nutritionix import Nutritionix as nx

import pyperclip
import json

inputString = "roast beef" #this is the search string 
num = 1 #this is which item in the search results will be selected, probably should update this system, oh well.

nix = nx(app_id="9f95ec82", api_key="7454625f6dfe33c6fae45d24c81302be")

inputId = nix.search(inputString, results=str(num)+":"+str(num+1)).json()["hits"][0]["_id"]


#print(json.dumps(nix.search("apple").json(), indent=4))

item = nix.item(id=inputId).json()


tCals = str(item["nf_total_fat"])
tCarbs = str(item["nf_total_carbohydrate"])
try:
    tUnsatFats = str(item["nf_polyunsaturated_fat"] + item["nf_monounsaturated_fat"])
except:
    tUnsatFats = str(0)
tSatFats = str(item["nf_saturated_fat"])
tTransFats = str(item["nf_trans_fatty_acid"])
tFats = str(item["nf_total_fat"])
tProtein = str(item["nf_protein"])
tSodium = str(item["nf_sodium"])
tSugar = str(item["nf_sugars"])
tFiber = str(item["nf_dietary_fiber"])
unitAmt = str(item["nf_serving_size_qty"])
unitName = str(item["nf_serving_size_unit"])

print("Pasted results for " + str(item["item_name"]))
pyperclip.copy(unitAmt + "\t" + unitName + '\t' + "" + "\t" + tCals + "\t" + tCarbs + "\t" + tFats + "\t" + tUnsatFats + "\t" + tSatFats + "\t" + tTransFats+ "\t" + tProtein + "\t" + tSodium + "\t" + tSugar + "\t" + tFiber)
#implement search function that finds the most likely id, then use that ID to collect everything needed like cals, etc.

#use format (t is tab) calories/Tcarbs/Ttotalfat/Tunsatfat/Ttransfat/Tprotein/Tsodium/Tsugar/TFiber