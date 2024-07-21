import os
import pandas as pd
from sqlalchemy import create_engine


# Assuming your file is named 'index.txt'
file_path = "F:/repos/Code-problems-Search-Engine/Qdata/index.txt"
with open(file_path, 'r') as file:
    # Read all lines from the file
    indexlist = file.readlines()

# Using a list comprehension
new_index_list = [elem.strip('\n') for elem in indexlist]      #just removed "/n" beside every element 


# Assuming your file is named 'Qindex.txt'
file_path = "F:/repos/Code-problems-Search-Engine/Qdata/Qindex.txt"

with open(file_path, 'r') as file:
    # Read all lines from the file
    Qindexlinkslist = file.readlines()

# Using a list comprehension
new_Qindex_list = [elem.strip('\n') for elem in Qindexlinkslist]   #just removed "/n" beside every element 

# Function to read description from a folder
folder_path="F:/repos/Code-problems-Search-Engine/Qdata/"

def read_description(folder_path, file_name):
    with open(os.path.join(folder_path, file_name), 'r') as file:
        return file.read()


# Prepare data for insertion into SQL table
data = []
base_path = "F:/repos/Code-problems-Search-Engine/Qdata/"
for i, heading in enumerate(new_index_list):
    folder_num = str(i + 1)
    folder_path = os.path.join(base_path, folder_num)  # Folder names are 1, 2, 3, ...
    file_name = folder_num + '.txt'  # File names are 1.txt, 2.txt, 3.txt, ...
    description = read_description(folder_path, file_name)
    link =Qindexlinkslist[i]
    data.append((heading, description, link))

connection_string = 'mysql+pymysql://root:Rushi1234@127.0.0.1:3306/leetcodeproblems'
print(f"Connecting to database with: {connection_string}")
engine = create_engine(connection_string)

# Create DataFrame
df = pd.DataFrame(data, columns=['heading', 'description', 'link'])


#df=pd.read_sql_table("leetcode_problems",engine,columns=['heading','description','link'])
#print(df)
df.to_sql(name="leetcode_problems", con=engine, schema=None, if_exists='append', index=False)

df=pd.read_sql_table("leetcode_problems",engine,columns=['heading','description','link'])



