import pandas as pd
teacher=pd.DataFrame({
    'Ism':['Durbek','Sarvinoz'],
    'Familya': ['Xalilov','Toxirova'],
    'Fan': ['Suniy Intilek','Suniy Intilek'],
    'Telefon raqami': ['+998991234567','+998991234567']
    
})
print(teacher)
teacher.to_excel('teacher.xlsx',index=False,sheet_name='Sheet1')