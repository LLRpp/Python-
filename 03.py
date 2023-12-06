import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

name = '湖南'

# 读取文件中的JSON数据
f = open('./省份疫情数据.txt', 'r', encoding='utf-8')
data = f.read()
# 关闭文件
f.close()

# 将JSON数据转成Python数据（字典类型）
data_dict = json.loads(data)
# 取得疫情数据（列表类型）
province_list = data_dict['areaTree'][0]['children'][0]['children']
# 取得各市的确诊数据
data_list = list()
for province_data in province_list:
    city_name = province_data['name'] # 城市名称
    city_confirm = province_data['total']['confirm']  # 确诊人数
    data_list.append((city_name, city_confirm))

# 获取地图对象
map = Map()


map.add(name+'省各市确诊人数', data_list, name)


# 设置全局配置项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        # 是否展示色卡（默认是True）
        is_show=True,
        # 色卡是否以分块矩形展示（默认是False）
        is_piecewise=True,
        # 设置不同数量对应的颜色展示
        pieces=[
            {"min": 1, "max": 9, "Label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "labe1": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "1abe1": "99-499人", "co1or": "#FF9966"},
            {"min": 500, "max": 999, "1abe1": "499-999人", "co1or": "#FF6666"},
            {"min": 1000, "max": 9999, "1abe1": "1000-9999人", "c010r": "#CC3333"},
            {"min": 10000, "1abe1": "10000以上", "col0r": "#990033"}
        ])
)

# 生成地图
map.render()
