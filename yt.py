import yt_dlp

def download_video(youtube_url):
    try:
        # Options pour yt-dlp
        ydl_opts = {
            'format': 'best',  # Télécharge la meilleure qualité disponible
            'outtmpl': '%(title)s.%(ext)s'  # Nom du fichier de sortie basé sur le titre
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
            print("Téléchargement terminé!")

    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    print("utiliser ce script avec l'envirropnemetn virtuel en 3.12 !")
    video_url = input("Entrez le lien YouTube: ")
    download_video(video_url)
