# 🚀 PaddleOCR-VL-1.5 Experiments: GPU & CPU

This repository contains demos and inference scripts for **PaddleOCR-VL-1.5 (0.9B)**. 
It offers two ways to run the model: a **Google Colab Notebook** (for GPU acceleration) and a **Python script** for local execution (CPU).

## 📂 Repository Structure

- **`PadlecOCR-V.L1.5.ipynb`** ⚡
  > **Google Colab Version (GPU).** Use this notebook to run the model with GPU acceleration. Ideal for fast inference and testing.
  
- **`install.py`** 💻
  > **Local Version (CPU).** A Python script designed to run on a local machine (e.g., laptop). Useful if you don't have a dedicated GPU.

- **`document_a_convertir.pdf` / `Results_1Q25.pdf`** 📄
  > Sample documents used for testing the parsing capabilities.

- **`output_image_test/`** 🖼️
  > Folder containing the inference results.

---

## 🛠️ How to Use

### Option 1: Run on Google Colab (GPU) 🚀
*Recommended for best performance.*

1. Upload `PadlecOCR-V.L1.5.ipynb` to your Google Drive or open it directly in [Google Colab](https://colab.research.google.com/).
2. Change the runtime type to **T4 GPU**.
3. Run the cells to install dependencies and perform inference.

### Option 2: Run Locally (CPU) 🐢
*Use this for testing on your local machine.*

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/mohammed-adachi/VLM-Document-Analysis])
   cd VLM-Document-Analysis