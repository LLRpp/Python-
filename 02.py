import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

name = '湖南'
# 获取地图对象
map = Map()


# 读取文件中的JSON数据
f = open('./中国疫情数据.txt.', 'r', encoding='utf-8')
data = f.read()
# 关闭文件
f.close()

# 将JSON数据转成Python数据（字典类型）
data_dict = json.loads(data)


# 取得各省的疫情数据（列表类型）
province_list = data_dict['areaTree'][0]['children']


# 取得各省的确证数据（）
data_list = list()
for province_data in province_list:
    province_name = province_data['name']  # 省份名称
    province_confirm = province_data['total']['confirm']  # 确诊人数
    data_list.append((province_name, province_confirm))

# 添加数据
map.add('各省份确诊人数', data_list, "china")




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
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"}
        ])
)

# 生成地图
map.render()
