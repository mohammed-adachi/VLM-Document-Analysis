import os
import warnings

# Désactiver les avertissements inutiles
warnings.filterwarnings("ignore")
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

from paddleocr import PaddleOCRVL

print("🚀 Chargement du modèle PaddleOCR-VL-1.5...")
ocr_pipeline = PaddleOCRVL() 
print("✅ Modèle chargé avec succès !")

# --- MODIFICATION ICI : Mettez le nom de votre image ---
image_file = "image.png"  # <--- Remplacez par le nom de votre image (ex: facture.png)

if os.path.exists(image_file):
    print(f"🖼️ Analyse de l'image : {image_file}")
    
    # Lancement de la prédiction
    result = ocr_pipeline.predict(image_file)
    
    # Dossier de sauvegarde
    save_path = "./output_image_test"
    
    # Sauvegarde des résultats
    for res in result:
        res.save_to_json(save_path)
        res.save_to_markdown(save_path)
        # Optionnel : Sauvegarder l'image avec les boîtes détectées
        res.save_to_img(save_path)
        
    print(f"💾 Résultats sauvegardés dans : {save_path}")

else:
    print(f"❌ Erreur : Le fichier '{image_file}' est introuvable.")
    print("👉 Assurez-vous que l'image est dans le même dossier que ce script.")