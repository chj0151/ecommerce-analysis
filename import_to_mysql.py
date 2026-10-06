# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

# 1. 读取 CSV
df = pd.read_csv('ecommerce_sales.csv')
print('读取完成，共 {} 行'.format(len(df)))

# 2. 处理日期列
df['order_date'] = pd.to_datetime(df['order_date']).dt.date

# 3. 连接 MySQL（密码改成你自己的）
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'ecomerece_db'   # 注意：跟你 MySQL 里实际的库名保持一致

engine = create_engine(
    'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )
)

# 4. 写入 MySQL
df.to_sql('sales', con=engine, if_exists='append', index=False, chunksize=1000)
print('导入完成！')

# 5. 验证
result = pd.read_sql('SELECT COUNT(*) AS cnt FROM sales', con=engine)
print(result)