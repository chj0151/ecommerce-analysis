# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib
matplotlib.use('Agg')   # 关键：使用不弹窗的后端，直接存文件
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 中文字体（Windows 常用）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 连接数据库
engine = create_engine(
    'mysql+pymysql://root:123456@localhost:3306/ecomerece_db?charset=utf8mb4'
)

# 图1：类别销售额
df1 = pd.read_sql('''
    SELECT category, SUM(amount) AS sales
    FROM sales
    GROUP BY category
    ORDER BY sales DESC
''', engine)

plt.figure(figsize=(10, 5))
sns.barplot(data=df1, x='category', y='sales')
plt.title('各品类销售额')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart_1_category.png', dpi=100)
plt.close()

# 图2：月度趋势
df2 = pd.read_sql('''
    SELECT DATE_FORMAT(order_date, '%%Y-%%m') AS month,
           SUM(amount) AS sales
    FROM sales
    GROUP BY month
    ORDER BY month
''', engine)

plt.figure(figsize=(14, 5))
plt.plot(df2['month'], df2['sales'], marker='o')
plt.title('月度销售趋势')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart_2_monthly.png', dpi=100)
plt.close()

# 图3：渠道占比
df3 = pd.read_sql('''
    SELECT channel, SUM(amount) AS sales
    FROM sales
    GROUP BY channel
''', engine)

plt.figure(figsize=(8, 8))
plt.pie(df3['sales'], labels=df3['channel'], autopct='%1.1f%%')
plt.title('各渠道销售额占比')
plt.savefig('chart_3_channel.png', dpi=100)
plt.close()

print('图表已生成：chart_1_category.png / chart_2_monthly.png / chart_3_channel.png')