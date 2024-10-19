import pandas as pd
import json

# JSON faylini o'qish
with open('data.json', 'r') as f:
    data = json.load(f)

# DataFrame yaratish
teacher = pd.DataFrame(data)

# DataFrame'ni chiqarish
print(teacher)

# DataFrame'ni Excel fayliga saqlash
teacher.to_excel('teacher.xlsx', index=False, sheet_name='Sheet1')
