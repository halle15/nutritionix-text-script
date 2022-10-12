from inspect import classify_class_attrs
from nutritionix import Nutritionix as nx
import json

nix = nx(app_id="9f95ec82", api_key="7454625f6dfe33c6fae45d24c81302be")

inputId = "513fceb475b8dbbc21000f92"


#print(json.dumps(nix.search("apple").json(), indent=4))

item = nix.item(id=inputId).json()


tCals = item["nf_total_fat"]
tCarbs = 0
tUnsatFats = 0
tSatFats = 0
tTransFats = 0
tFats = tUnsatFats + tSatFats + tTransFats
tProtein = 0
tSodium = 0
tSugar = 0
tFiber = 0

print(tCals)
#implement search function that finds the most likely id, then use that ID to collect everything needed like cals, etc.

#use format (t is tab) calories/Tcarbs/Ttotalfat/Tunsatfat/Ttransfat/Tprotein/Tsodium/Tsugar/TFiber