# Application de Gestion d'Émargement - Cyrus Herez

Application web progressive (PWA) pour gérer l'émargement des participants lors d'événements avec scan de QR codes.

## 🚀 Fonctionnalités

- ✅ Création et gestion d'événements
- 📊 Suivi en temps réel des présences
- 📷 Scan de QR codes pour émargement automatique
- 📥 Import/Export Excel des participants
- 💾 Sauvegarde automatique des données
- 📱 Application installable sur mobile (PWA)
- 🔒 Données stockées localement (confidentialité)
- 🌐 Fonctionne hors ligne

## 📦 Installation sur GitHub Pages

### Option 1 : Déploiement automatique

1. **Créer un nouveau repository sur GitHub**
   - Nom suggéré : `emargement-app`
   - Public ou Private selon vos besoins

2. **Uploader les fichiers**
   ```bash
   # Dans votre terminal
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/VOTRE_USERNAME/emargement-app.git
   git push -u origin main
   ```

3. **Activer GitHub Pages**
   - Allez dans Settings > Pages
   - Source : Deploy from a branch
   - Branch : main / (root)
   - Save

4. **Accéder à votre app**
   - URL : `https://VOTRE_USERNAME.github.io/emargement-app/`

### Option 2 : Upload manuel

1. Créer un nouveau repository
2. Aller dans "Add file" > "Upload files"
3. Glisser-déposer tous les fichiers
4. Activer GitHub Pages (voir étape 3 ci-dessus)

## 📱 Installation sur mobile

### Android
1. Ouvrir l'app dans Chrome
2. Menu (⋮) > "Ajouter à l'écran d'accueil"
3. L'icône apparaîtra sur votre écran d'accueil

### iOS (iPhone/iPad)
1. Ouvrir l'app dans Safari
2. Bouton Partage > "Sur l'écran d'accueil"
3. Confirmer l'ajout

## 📖 Guide d'utilisation

### Créer un événement

1. Cliquez sur "Créer un événement"
2. Remplissez les informations (nom, date, lieu, etc.)
3. Importez la liste des inscrits depuis un fichier Excel
4. Validez la création

### Format du fichier Excel

Le fichier doit contenir les colonnes suivantes :
- **ID d'inscription** (obligatoire) : Identifiant unique
- **Contact** : Nom du participant
- **Gérant** : Nom du gérant/responsable
- **Adresse email** : Email du participant
- **Événement** : Nom de l'événement (optionnel, détecté automatiquement)

### Scanner les QR codes

1. Ouvrir l'événement
2. Cliquer sur "Scanner QR Code"
3. Autoriser l'accès à la caméra
4. Présenter le QR code devant la caméra
5. La présence est enregistrée automatiquement

### Exporter les données

1. Dans un événement : Bouton "Exporter Excel"
2. Choisir le type d'export :
   - Tous les participants
   - Présents uniquement
   - Absents uniquement
   - Ajouts manuels

## 💾 Sauvegarde des données

### Sauvegarde automatique
- Les données sont sauvegardées automatiquement dans le navigateur
- Un backup automatique est créé à chaque modification

### Sauvegarde manuelle
1. Allez dans Paramètres (⚙️)
2. Cliquez sur "Exporter toutes les données"
3. Téléchargez le fichier JSON
4. Conservez-le en lieu sûr

### Restauration
1. Paramètres > "Importer des données"
2. Sélectionnez votre fichier de sauvegarde .json
3. Les données sont restaurées

## ⚠️ Important

### Données et confidentialité
- Toutes les données sont stockées localement dans votre navigateur
- Aucune donnée n'est envoyée sur Internet
- Les données peuvent être perdues si vous :
  - Videz le cache du navigateur
  - Désinstallez l'application
  - Changez de navigateur/appareil

### Recommandations
✅ **Exportez régulièrement vos données** (au moins après chaque événement)
✅ Conservez les exports dans un endroit sûr (Drive, Dropbox, etc.)
✅ Testez l'import/export avant un événement important
✅ Vérifiez que le scan QR fonctionne sur votre appareil

## 🔧 Maintenance

### Mise à jour de l'application
1. Téléchargez la nouvelle version
2. Remplacez les fichiers dans votre repository GitHub
3. Commit et push
4. GitHub Pages se mettra à jour automatiquement

### Résolution de problèmes

**L'application ne s'affiche pas :**
- Videz le cache du navigateur
- Vérifiez que GitHub Pages est activé
- Attendez quelques minutes après l'activation

**Le scanner QR ne fonctionne pas :**
- Vérifiez les permissions de la caméra
- Utilisez HTTPS (obligatoire pour la caméra)
- Testez sur un autre navigateur

**Données perdues :**
- Restaurez depuis votre dernière sauvegarde JSON
- Vérifiez le stockage du navigateur

## 🛠 Technologies utilisées

- React 18
- Tailwind CSS
- SheetJS (xlsx)
- html5-qrcode
- LocalStorage API
- Service Worker (PWA)

## 📝 Structure des fichiers

```
emargement-app/
├── index.html          # Application principale
├── manifest.json       # Configuration PWA
├── sw.js              # Service Worker
├── icon-192.png       # Icône 192x192 (à créer)
├── icon-512.png       # Icône 512x512 (à créer)
└── README.md          # Documentation
```

## 🎨 Icônes manquantes

Pour une PWA complète, créez deux icônes :
- `icon-192.png` : 192x192 pixels
- `icon-512.png` : 512x512 pixels

Vous pouvez utiliser des outils comme :
- [Favicon Generator](https://favicon.io/)
- [PWA Asset Generator](https://www.pwabuilder.com/)
- Photoshop / GIMP / Figma

## 📞 Support

Pour toute question ou problème :
1. Vérifiez la section "Résolution de problèmes"
2. Consultez la console du navigateur (F12)
3. Exportez vos données avant toute manipulation

## 📄 Licence

Cette application est fournie "telle quelle" sans garantie.
Usage libre pour un usage personnel ou professionnel.

---

