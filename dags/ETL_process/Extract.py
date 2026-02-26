import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
from pathlib import Path

def extraction():
  path = kagglehub.dataset_download("nudratabbas/top-100-ai-tools-2026")
  file_path = Path(path) / "top100_ai_tools_2026.csv"

  df = pd.read_csv(file_path)

  return df
