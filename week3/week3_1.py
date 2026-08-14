import sys
print(sys.executable)
from ucimlrepo import fetch_ucirepo 

def main():
    print("Hello, World!")
  
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

print("Total number of records  is", len(X))
print("Total number of different flowers", y.iloc[:, 0].nunique())
print("names of all different flowers in the dataset")
for name in y.iloc[:, 0].unique():
    print(name)

if __name__ == "__main__":
    main()
    