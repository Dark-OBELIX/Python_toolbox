app = QApplication(sys.argv)
dialog = QFileDialog()  # Définissez la boîte de dialogue comme une variable globale

def get_docx_file():
    dialog.setFileMode(QFileDialog.ExistingFiles)
    dialog.setFilter(QDir.Files)

    if dialog.exec_():
        file_name = dialog.selectedFiles()
        if file_name[0].endswith('.docx'):
            return True, str(file_name[0])
        else:
            print("Erreur : Le fichier sélectionné n'est pas un docx")
            return False, ""
    else:
        print("Erreur : Pas de fichier sélectionné")
        return False, ""


def get_txt_file():
    dialog.setFileMode(QFileDialog.ExistingFiles)
    dialog.setFilter(QDir.Files)

    if dialog.exec_():
        file_name = dialog.selectedFiles()
        if file_name[0].endswith('.txt'):
            return True, str(file_name[0])
        else:
            print("Erreur : Le fichier sélectionné n'est pas un fichier texte (.txt)")
            return False, ""
    else:
        print("Erreur : Pas de fichier sélectionné")
        return False, ""

############################################################

importOk, doc_path = get_docx_file()
#importOk, doc_path = get_txt_file()

if importOk:
    print(doc_path)
