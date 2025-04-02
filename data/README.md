# 📁 Dataset: Diabetes Health Indicators

This project uses the **Diabetes Health Indicators Dataset** from Kaggle to predict a patient's diabetes status:
- `0` = No Diabetes
- `1` = Prediabetes
- `2` = Diabetes

## 📦 Dataset Source
- Kaggle Dataset: [https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

## ⚠️ Note
The raw dataset is not included in this GitHub repo due to Kaggle's terms of use.

To download the dataset yourself:

1. Go to your [Kaggle account settings](https://www.kaggle.com/account)
2. Click “Create New Token” to download `kaggle.json`
3. Move it to your `.kaggle` folder (see below)
4. Run the included Python script to download the data.

## 💻 How to Download with the Kaggle API

```bash
# Step 1: Make sure your kaggle.json file is in place
mkdir ~/.kaggle
mv /path/to/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Step 2: Install Kaggle CLI
pip install kaggle

# Step 3: Run the download script
python download_kaggle_data.py
