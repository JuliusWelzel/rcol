from dotenv import load_dotenv
import pandas as pd
from redcap import Project
import os
from src.rcol.instruments import fal, ehi

load_dotenv()
RC_API_KEY = os.getenv("RC_API_KEY")


# Stack all instrument DataFrames 
all_instruments = pd.concat([fal, ehi], ignore_index=True)
# print form names
print("Form names:")
print(all_instruments['form_name'].unique())

# initalize the redcap project
api_url = 'https://redcapdev.uol.de/api/'
rc_project = Project(api_url, RC_API_KEY)

# upload instruments to RedCap using the import_metadata method
rc_project.import_metadata(all_instruments, import_format='df')
