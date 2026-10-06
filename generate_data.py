# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

n_rows = 50000
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

categories = ['手机', '电脑', '家电', '服饰', '食品', '图书', '美妆', '运动']
products = {
    '手机': ['iPhone 15', '华为Mate60', '小米14', 'OPPO Find X', 'vivo X100'],
    '电脑': ['MacBook Pro', '联想拯救者', '戴尔XPS', '华硕天选', '惠普暗影精灵'],
    '家电': ['美的空调', '格力冰箱', '海尔洗衣机', '小米电视', '戴森吹风机'],
    '服饰': ['Nike外套', 'Adidas运动裤', '优衣库T恤', '李宁卫衣', '安踏跑鞋'],
    '食品': ['三只松鼠坚果', '良品铺子', '百草味', '蒙牛牛奶', '伊利酸奶'],
    '图书': ['Python编程', '算法导论', '活着', '三体', '明朝那些事儿'],
    '美妆': ['兰蔻精华', '雅诗兰黛', '完美日记', '花西子', '欧莱雅'],
    '运动': ['瑜伽垫', '哑铃', '跑步机', '篮球', '羽毛球拍']
}
regions = ['华北', '华东', '华南', '华中', '西南', '西北', '东北']
channels = ['APP', '小程序', 'PC官网', '天猫', '京东']

rows = []
for i in range(n_rows):
    category = random.choice(categories)
    product = random.choice(products[category])
    price = round(random.uniform(20, 8000), 2)
    quantity = random.randint(1, 5)
    discount = round(random.choice([1.0, 0.95, 0.9, 0.85, 0.8, 0.7]), 2)
    amount = round(price * quantity * discount, 2)
    order_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    rows.append({
        'order_id': 'ORD{}'.format(100000 + i),
        'user_id': 'U{}'.format(random.randint(1000, 9999)),
        'product_name': product,
        'category': category,
        'price': price,
        'quantity': quantity,
        'discount': discount,
        'amount': amount,
        'region': random.choice(regions),
        'channel': random.choice(channels),
        'order_date': order_date.strftime('%Y-%m-%d')
    })

df = pd.DataFrame(rows)
df.to_csv('ecommerce_sales.csv', index=False, encoding='utf-8-sig')
print('生成完成，共 {} 行'.format(len(df)))
print(df.head())
print(df.dtypes)