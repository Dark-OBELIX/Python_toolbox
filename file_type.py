import os
import mimetypes
import chardet

def obtenir_extension_et_encodage(fichier):
    # Obtenir l'extension du fichier
    extension = os.path.splitext(fichier)[1]
    
    # Détecter le type MIME et l'encodage du fichier
    type_mime, _ = mimetypes.guess_type(fichier)
    
    # Détecter l'encodage avec chardet
    with open(fichier, 'rb') as f:
        result = chardet.detect(f.read())
        encodage = result['encoding']
    
    return extension, type_mime, encodage

# Exemple d'utilisation
fichier = 'C:/Users/hugol/OneDrive/Desktop/test.txt'
fichier = 'C:/Users/hugol/OneDrive/Desktop/Prosit aller 02 - Bloc PA.docx'
extension, type_mime, encodage = obtenir_extension_et_encodage(fichier)
print(f"Extension: {extension}")
print(f"Type MIME: {type_mime}")
print(f"Encodage: {encodage}")
