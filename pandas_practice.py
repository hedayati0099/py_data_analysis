import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv('data.csv' ,sep=',',error_bad_lines=False)


for col in df.columns:
    print(df[col].describe(),'\n\n')

print('---------------------------------------------------------------')

u_bed = pd.unique(df['Bedrooms'])
u_bath = pd.unique(df['Bathrooms'])
print('The distinct number of bedrooms and bathrooms is : ','\n\n',u_bath,'\n\n',u_bed)
print('-----------------------------------------------------------------')

#drop the column

df.drop(columns="Location",inplace=True)
print('Location column was droped')
#inplace = False -->  that make a copy of data frame.
# if inplace = True do operation inplace and return None.
print('------------------------------------------------------------------')

# Rename the columns

print("Columns will be renamed ...",'\n')
df.rename(columns={"MLS":"Listening"} , inplace=True)
print("After rename : " , df.columns)
print('---------------------------------------------------------------------')

# editing the Price/SQ.Ft column 

df["Price/SQ.Ft"] = df["Price/SQ.Ft"].str.replace('$',' ',regex=True)
df["Price/SQ.Ft"] = pd.to_numeric(df["Price/SQ.Ft"])
print('the Price/SQ.Ft column was edited.')

#Plot this column

n , bins , patches = plt.hist(df["Price/SQ.Ft"] , 10 , facecolor='green')
plt.show()
print('----------------------------------------------------------------------')

#Applying Only on variables with NaN values

for col in df.columns[df.isnull().any(axis=0)]:     
    df[col].fillna(df[col].mean(),inplace=True)
        
print('The NaN characters in each column were filled with averages.')
print('-------------------------------------------------------------------------')

# the most expensive -->  df["Price"].max() is 5499000
# cheapest -->  df["Price"].min()  is 26500 

new_values = {"Price":{26500 : "cheapest = 26500", 5499000 : "the most expensive = 5499000"}}
df.replace(new_values,inplace=True)
print('New values replaced')
print('----------------------------------------------------------------------------')

print("The End Of This Program")
