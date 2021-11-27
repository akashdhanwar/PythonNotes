# pip install ipython
# ipython

# DataFrames
import pandas
df1 = pandas.DataFrame([[1,2,3],[10,20,30]])
df1 = pandas.DataFrame([[1,2,3],[10,20,30]], columns=(["Price","Age","Value"]), index=["First","Second"]) # Naming columns
df2 = pandas.DataFrame([{"Name":"Akash","Surname":"Dhanwar"},{"Name":"Jack"}])
print(df1,"\n")
print(df2,"\n")
# dir(df1)
print(df1.mean(),"\n")
print(df1.mean().mean(),"\n")
print(df1.Price,"\n")  # Price column
print(df1.Price.mean(),"\n")
print(df1.Price.max(),"\n")  


# pip3.10 install jupyter
# jupyter notebook  OR py -3.9 -m jupyter notebook OR python3.9 -m jupyter notebook
# Jupytor is used for testing as cmd and saving code parallelly

