#version 1
import tkinter as tk
from tkinter import messagebox
import obd
import threading

# Fonction pour récupérer les informations OBD-II
def lire_rpm():
    try:
        connection = obd.OBD()
        cmd = obd.commands.RPM
        response = connection.query(cmd)
        return response.value if not response.is_null() else "N/A"
    except:
        return "Erreur"

def lire_position_accelerateur():
    try:
        connection = obd.OBD()
        cmd = obd.commands.THROTTLE_POS
        response = connection.query(cmd)
        return response.value if not response.is_null() else "N/A"
    except:
        return "Erreur"

def lire_temperature_moteur():
    try:
        connection = obd.OBD()
        cmd = obd.commands.COOLANT_TEMP
        response = connection.query(cmd)
        return response.value.to("celsius") if not response.is_null() else "N/A"
    except:
        return "Erreur"

def lire_vitesse():
    try:
        connection = obd.OBD()
        cmd = obd.commands.SPEED
        response = connection.query(cmd)
        return response.value.to("kph") if not response.is_null() else "N/A"
    except:
        return "Erreur"

# Mettre à jour l'interface avec les données OBD
def mettre_a_jour_donnees():
    rpm_label_var.set(f"Régime moteur (RPM) : {lire_rpm()}")
    accel_label_var.set(f"Position de l'accélérateur (%) : {lire_position_accelerateur()}")
    temp_label_var.set(f"Température moteur (°C) : {lire_temperature_moteur()}")
    speed_label_var.set(f"Vitesse (km/h) : {lire_vitesse()}")

def boucle_donnees():
    while rafraichir_donnees:
        mettre_a_jour_donnees()
        root.update_idletasks()
        root.after(1000)  # Mettre à jour toutes les secondes

def demarrer_rafraichissement():
    global rafraichir_donnees
    rafraichir_donnees = True
    threading.Thread(target=boucle_donnees).start()

def arreter_rafraichissement():
    global rafraichir_donnees
    rafraichir_donnees = False

# Interface graphique
root = tk.Tk()
root.title("Interface Dd BMW 318d G20")
root.geometry("400x400")

rpm_label_var = tk.StringVar()
accel_label_var = tk.StringVar()
temp_label_var = tk.StringVar()
speed_label_var = tk.StringVar()

rpm_label_var.set("Régime moteur (RPM) : --")
accel_label_var.set("Position de l'accélérateur (%) : --")
temp_label_var.set("Température moteur (°C) : --")
speed_label_var.set("Vitesse (km/h) : --")

# Étiquettes pour afficher les données
rpm_label = tk.Label(root, textvariable=rpm_label_var, font=("Arial", 14))
rpm_label.pack(pady=10)

accel_label = tk.Label(root, textvariable=accel_label_var, font=("Arial", 14))
accel_label.pack(pady=10)

temp_label = tk.Label(root, textvariable=temp_label_var, font=("Arial", 14))
temp_label.pack(pady=10)

speed_label = tk.Label(root, textvariable=speed_label_var, font=("Arial", 14))
speed_label.pack(pady=10)

# Bouton pour démarrer le rafraîchissement des données
btn_start = tk.Button(root, text="Démarrer Rafraîchissement", command=demarrer_rafraichissement, width=30)
btn_start.pack(pady=10)

# Bouton pour arrêter le rafraîchissement des données
btn_stop = tk.Button(root, text="Arrêter Rafraîchissement", command=arreter_rafraichissement, width=30)
btn_stop.pack(pady=10)

rafraichir_donnees = False

root.mainloop()
