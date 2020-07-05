import requests,json,re,os,subprocess,time
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
data = json.loads(requests.get(url=url).json()["data"])
china = data["areaTree"][0]["children"]

data = []
for i in range(len(china)):
    data.append([china[i]["name"],china[i]["total"]["confirm"]])
map_p = Map()
map_p.set_global_opts(title_opts=opts.TitleOpts(title="实时疫情图"), visualmap_opts=opts.VisualMapOpts(max_=200))
map_p.add("确诊", data, maptype="china")
map_p.render("ncov.html")
time.sleep(2)
if os.name == "nt":
    os.startfile("ncov.html")
elif os.name == "posix":
    subprocess.Popen(["open","ncov.html"])
else:
    subprocess.Popen(["xdg-open","ncov.html"])