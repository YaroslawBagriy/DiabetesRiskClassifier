#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# download_kaggle_data.py
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Dataset info
dataset_slug = "alexteboul/diabetes-health-indicators-dataset"
download_dir = "data/"

# Make sure directory exists
os.makedirs(download_dir, exist_ok=True)

# Authenticate and download
api = KaggleApi()
api.authenticate()

print(f"📥 Downloading '{dataset_slug}' into '{download_dir}'...")
api.dataset_download_files(dataset_slug, path=download_dir, unzip=True)
print("✅ Download complete and unzipped!")

