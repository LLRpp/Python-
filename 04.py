from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取文件中的数据
f = open('./data.csv', 'r', encoding='gbk')
data_lines = f.readlines()
f.close()

# 处理读取的数据
data_lines.pop(0)  # 删除第一条数据

# 将字符串数据转成Python数据（字典）
data_dict = dict()
for line in data_lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])
    try:

        data_dict[year].append([country, gdp])
    except KeyError:
        # 当为新年份时，就重新创建一个列表，然后追加元素
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline({'theme': ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取gdp前8
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    # 遍历每
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴为
        y_data.append(country_gdp[1])  # y轴为gdp

    # 获取柱状图对象，构建柱状图
    bar = Bar()
    # 让高数据在上面
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(十亿美元)', y_data, label_opts=LabelOpts(position='right'))
    # 反转x和y轴
    bar.reversal_axis()
    # 设置全局配置项
    bar.set_global_opts(
        # 设置每年一个标题
        title_opts=TitleOpts(title=f'{year}年8省GDP排行榜')
    )
    # 添加时间点
    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 生成动态GDP柱状图
timeline.render("2008-2023全国GDP前8省份.html")
