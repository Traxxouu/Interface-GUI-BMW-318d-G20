# BMW 318d OBD-II Interface - Gestion et Monitoring du Moteur

![Compatible](https://github.com/Traxxouu/Interface-GUI-BMW-318d-G20/IMG_0012.jpg)

Cette application Python permet de surveiller et d'envoyer des consignes au moteur d'une BMW 318d via la prise OBD-II. Elle utilise la bibliothèque `obd` pour lire les données en temps réel et `tkinter` pour créer une interface graphique.

## Fonctionnalités

- **Lecture de la température du moteur** : Affiche la température actuelle du liquide de refroidissement.
- **Affichage des messages du moteur** : Lecture des éventuels messages d'erreur moteur via l'interface OBD-II.
- **Monitoring en temps réel** : Affiche les informations en direct telles que :
  - Régime moteur (RPM)
  - Position de l'accélérateur (%)
  - Température moteur (°C)
  - Vitesse du véhicule (km/h)
- **Envoi de consignes** :
  - Envoi d'une consigne pour un régime moteur spécifique (RPM).
  - Consultation de la position actuelle de l'accélérateur.
- **Rafraîchissement en temps réel** : Les données OBD-II sont mises à jour toutes les secondes.

## Prérequis

- **Adaptateur OBD-II** : Un adaptateur compatible (Bluetooth, Wi-Fi, ou USB) connecté à la prise OBD-II de la BMW 318d.
- **Python 3.x**
- **Bibliothèques Python nécessaires** :
  - `tkinter` (inclus avec Python)
  - `obd` (pour la communication avec la prise OBD-II)

### Installation des bibliothèques

Installez la bibliothèque OBD avec `pip` :

```bash
pip install obd
```

## Utilisation

**Cloner le dépôt Git** :

   ```bash
   git clone https://github.com/Traxxouu/Interface-GUI-BMW-318d-G20.git
   cd Interface-GUI-BMW-318d-G20
   ```
