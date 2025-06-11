#dim=[20,30,'mg mg','kyaw kyaw'] #series
#dic={'keys':'value'} #DataFrame
import pandas as pd
data= {
    'A':[1,2,3],
    'B':[4,5,6]
    }

excel_data=pd.read_excel("C:\\Users\\Yu Yu Wai\\OneDrive\\Documents\\GitHub\\Pandas\\tutorial\\abc.xlsx")

df=pd.DataFrame(excel_data[["First Name","Last Name"]])
#print(df.info())
print(df.describe())


