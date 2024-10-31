import tkinter as tk
from tkinter import messagebox
import obd

def envoyer_consigne_rpm(valeur_rpm):
    try:
        connection = obd.OBD() #protocol bug
        cmd = obd.commands.RPM
        response = connection.query(cmd)
        
        if not response.is_null():
            return f"Régime moteur actuel : {response.value} RPM"
        else:
            return "Aucune donnée disponible"
    except Exception as e:
        return f"Erreur lors de l'envoi de la consigne: {str(e)}"

def envoyer_rpm():
    valeur_rpm = rpm_entry.get()
    if valeur_rpm.isdigit():
        message = envoyer_consigne_rpm(valeur_rpm)
        messagebox.showinfo("Consigne RPM", message)
    else:
        messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide pour le régime moteur.")

def envoyer_consigne_acceleration():
    try:
        connection = obd.OBD()
        cmd = obd.commands.THROTTLE_POS
        response = connection.query(cmd)
        if not response.is_null():
            messagebox.showinfo("Position Accélérateur", f"Position actuelle : {response.value}%")
        else:
            messagebox.showinfo("Erreur", "Impossible de lire la position de l'accélérateur.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'envoi de la consigne : {str(e)}")

root = tk.Tk()
root.title("Envoi de Consignes Moteur via OBD-II")
root.geometry("400x300")

label_titre = tk.Label(root, text="Interface de Consignes Moteur", font=("Arial", 16))
label_titre.pack(pady=10)

label_rpm = tk.Label(root, text="Entrer un régime moteur (RPM):")
label_rpm.pack(pady=5)
rpm_entry = tk.Entry(root)
rpm_entry.pack(pady=5)

btn_envoyer_rpm = tk.Button(root, text="Envoyer Consigne RPM", command=envoyer_rpm, width=30)
btn_envoyer_rpm.pack(pady=10)

btn_acceleration = tk.Button(root, text="Voir Position Accélérateur", command=envoyer_consigne_acceleration, width=30)
btn_acceleration.pack(pady=10)

root.mainloop()
