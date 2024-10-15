import tkinter as tk
from tkinter import messagebox
import obd

# Fonction pour lire la température 
def lire_temperature_obd():
    try:
        # Connexion à l'OBD-II
        connection = obd.OBD()  
        
        # temp du liquide de refroidissement dans le CMD
        cmd = obd.commands.COOLANT_TEMP
        
        # Récupération de la réponse OBD-II
        response = connection.query(cmd)
        
        
        if not response.is_null():
            return response.value.to("celsius")  # Convertir en Celsius si nécessaire
        else:
            return "Aucune donnée disponible"
    except Exception as e:
        return f"Erreur: {str(e)}"

# afficher la température moteur
def afficher_temperature():
    temperature = lire_temperature_obd()  
    messagebox.showinfo("Température moteur", f"La température moteur est : {temperature}")

# Fonction pour lire les messages moteur
def afficher_messages_moteur():
    messages = lire_messages_moteur_obd() 
    messagebox.showinfo("Messages moteur", f"Messages moteur : {messages}")

# Exemple de fonctions pour récupérer les données depuis OBD-II (simulée)
def lire_messages_moteur_obd():
    return "Aucun message d'erreur" 

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion du moteur BMW 318d")
root.geometry("300x200")

# Ajout d'un titre
label_titre = tk.Label(root, text="Interface de Gestion Moteur", font=("Arial", 16))
label_titre.pack(pady=10)

# Ajout des boutons
btn_temperature = tk.Button(root, text="Voir Température Moteur", command=afficher_temperature, width=30)
btn_temperature.pack(pady=10)

btn_messages_moteur = tk.Button(root, text="Voir Messages Moteur", command=afficher_messages_moteur, width=30)
btn_messages_moteur.pack(pady=10)

# Lancement de l'interface graphique
root.mainloop()
