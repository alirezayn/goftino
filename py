درود به همه دوستان و همکاران عزیزم در بخش پایتون
@⁨پوریا ادیب⁩ 
@⁨عارف مرادی پاشا⁩ 
@⁨علیرضا یوسف نژاد⁩ 
@⁨سعیده سید کاظمی⁩ 
@⁨shokoofeh⁩ 
برای پروژه واژه یاب این لینک رو بفرستید برای بچه هایی که میخوان کار کنن، این API کار میکنه و اوکیه 👇🏻

def GetWord(self, querySearch):
        result = requests.get("https://api.codebazan.ir/vajehyab/?text=" + querySearch)
        parser = json.loads(result.text)
        obj = {"Search": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["Query"],
               "Text": parser["props"]["pageProps"]["fallback"][querySearch + ":"]["data"]["WordBox"]["Amid"][
                   "description"]}
        return obj