\# 电商销售数据分析项目



\## 项目简介

基于 5 万行电商订单数据，使用 MySQL + Python 完成多维度分析，输出业务洞察。



\## 技术栈

\- MySQL 8.0（数据存储）

\- Python 3.7 + pandas 1.3.5（数据处理）

\- matplotlib 3.5.3 / seaborn 0.12.2（可视化）

\- SQLAlchemy 1.4.46 + PyMySQL（数据库连接）



\## 数据说明

\- 数据量：50,000 行订单

\- 字段：order\_id, user\_id, product\_name, category, price, quantity, discount, amount, region, channel, order\_date

\- 时间范围：2023-01 \~ 2024-12

\- 数据来源：Python 脚本生成模拟数据



\## 分析内容

1\. 总体销售额和订单量

2\. 品类 / 地区 / 渠道维度销售分析

3\. Top 10 热销商品

4\. 月度销售趋势

5\. 用户复购分层

6\. 每个品类 Top 3 商品（窗口函数）



\## 核心发现

\- 电脑类销售额最高，客单价显著高于其他品类

\- 各渠道客单价差异不大，APP 和小程序为主要来源

\- 月度销售额波动平稳，无明显季节性

\- 大部分用户只购买 1-2 次，复购率较低



\## 文件说明

\- `generate\\\_data.py`：生成 5 万行模拟电商数据

\- `import\\\_to\\\_mysql.py`：把数据导入 MySQL

\- `analysis.sql`：所有 SQL 分析脚本

\- `visualize.py`：生成可视化图表

\- `chart\\\_1\\\_category.png`：各品类销售额

\- `chart\\\_2\\\_monthly.png`：月度销售趋势

\- `chart\\\_3\\\_channel.png`：渠道销售额占比



\## 作者

你的名字 | 2025-10

