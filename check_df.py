import os
import sys
import inspect
import re 
# Find path to pyMBE
current_dir= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path_end_index=current_dir.find("pyMBE")
pyMBE_path=current_dir[0:path_end_index]+"pyMBE"
sys.path.insert(0, pyMBE_path)


import pyMBE

pmb = pyMBE.pymbe_library()


# Here you can adjust the width of the panda columns displayed when running the code 
pmb.pd.options.display.max_colwidth = 10
pmb.pd.set_option('display.max_rows', None)



df = pmb.read_pmb_df(filename='df-new.csv')

print (df.dtypes)
print (df.head(50))


# bond = df.loc[0,'diameter'].values[0]

# print (bond, type(bond))
# numeric_value = float(re.split('\s+', bond)[0])
# unit = re.split('\s+', bond)[1]

# print (unit, type(unit))




# print (df.loc[0,'epsilon'].values[0].magnitude)

# seq= df[df['pmb_type']=='molecule'].sequence.values[0]

# for name in seq:
#       print (name)