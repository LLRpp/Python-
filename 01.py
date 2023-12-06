import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 改这里
name1 = '美国'
name2 = '日本'
name3 = '印度'

# 读取文件中的JSON数据
f_us = open('./'+name1+'.txt', 'r', encoding='utf-8')
f_jp = open('./'+name2+'.txt', 'r', encoding='utf-8')
f_in = open('./'+name3+'.txt', 'r', encoding='utf-8')
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

# 去掉文件中不规范的字符串，得到规范的JSON字符串
us_data = us_data.replace('jsonp_1629344292311_69436(', "")  # 去掉开始不规范的字符串
us_data = us_data[:-2]  # 去掉末尾不规范的字符串
jp_data = jp_data.replace('jsonp_1629350871167_29498(', "")  # 去掉开始不规范的字符串
jp_data = jp_data[:-2]  # 去掉末尾不规范的字符串
in_data = in_data.replace('jsonp_1629350745930_63180(', "")  # 去掉开始不规范的字符串
in_data = in_data[:-2]  # 去掉末尾不规范的字符串

# 将JSON字符串转换成Python数据
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# print(us_dict)
# print(jp_dict)
# print(in_dict)

# 获取key（trend）
us_trend_dict = us_dict['data'][0]['trend']
jp_trend_dict = jp_dict['data'][0]['trend']
in_trend_dict = in_dict['data'][0]['trend']

# 获取key（updateDate）
us_updateDate_dict = us_trend_dict['updateDate']
jp_updateDate_dict = jp_trend_dict['updateDate']
in_updateDate_dict = in_trend_dict['updateDate']

# 只获取2020年的数据（x轴的数据，表示日期）
us_x_data = us_updateDate_dict[:314]
jp_x_data = jp_updateDate_dict[:314]
in_x_data = in_updateDate_dict[:314]

# 获取y轴的数据
# 获取key（list）
us_list_list = us_trend_dict['list']
jp_list_list = jp_trend_dict['list']
in_list_list = in_trend_dict['list']


# 获取确诊数据（y轴的数据）
us_y_data = us_list_list[0]['data']
jp_y_data = jp_list_list[0]['data']
in_y_data = in_list_list[0]['data']

# 得到折线图对象
line = Line()
# 添加x轴数据（x轴的数据是共用的，所以只需要添加一份即可）
line.add_xaxis(us_x_data)
# 添加y轴数据（label_opts=LegendOpts(is_show=False)不显示折线图中点的数值）
line.add_yaxis(name1+'确证人数', us_y_data, label_opts=LegendOpts(is_show=False))
line.add_yaxis(name2+'确证人数', jp_y_data, label_opts=LegendOpts(is_show=False))
line.add_yaxis(name3+'确证人数', in_y_data, label_opts=LegendOpts(is_show=False))

# 设置全局配置项
line.set_global_opts(
    # 设置标题
    title_opts=TitleOpts(title='2020年'+name1[0]+name2[0]+name3[0]+'确诊人数对比', pos_left="center", pos_bottom="0%"),
    # 是否展示图例（默认是True）
    legend_opts=LegendOpts(is_show=True),
    # 是否展示工具箱（默认是False）
    toolbox_opts=ToolboxOpts(is_show=True),
    # 是否展示色卡（默认是没有该属性，一旦设置了该属性，无论是否取值都会展示不同颜色）
    # visualmap_opts=VisualMapOpts(is_show=True)

)

# 生成图表
line.render()
