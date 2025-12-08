# 📁 Structure du Projet - Application d'Émargement

## Fichiers du projet

```
emargement-app/
│
├── 📄 index.html              # Application principale (tout-en-un)
│   └── Contient: React, interface utilisateur, logique métier
│
├── 📄 manifest.json           # Configuration PWA
│   └── Permet l'installation comme app mobile
│
├── 📄 sw.js                   # Service Worker
│   └── Gère le cache et le mode hors ligne
│
├── 🖼️ icon-192.png            # Icône 192x192 (PWA)
├── 🖼️ icon-512.png            # Icône 512x512 (PWA)
│
├── 📝 README.md               # Documentation complète
├── 📝 INSTALLATION.md         # Guide de déploiement rapide
├── 📝 STRUCTURE.md            # Ce fichier
│
├── 🐍 generate_icons.py       # Script pour régénérer les icônes
└── 📝 .gitignore              # Fichiers à ignorer par Git
```

## 🔑 Fichiers essentiels pour GitHub Pages

Les fichiers **absolument nécessaires** sont :
1. ✅ `index.html` - L'application elle-même
2. ✅ `manifest.json` - Pour PWA
3. ✅ `sw.js` - Pour mode hors ligne
4. ✅ `icon-192.png` - Icône principale
5. ✅ `icon-512.png` - Icône haute résolution

## 📝 Fichiers de documentation

Ces fichiers sont recommandés mais optionnels :
- `README.md` - Documentation détaillée
- `INSTALLATION.md` - Guide de déploiement
- `STRUCTURE.md` - Ce fichier

## 🛠️ Fichiers utilitaires

- `generate_icons.py` - Pour régénérer les icônes si besoin
- `.gitignore` - Configuration Git

## 🎯 Fonctionnement

### Architecture de l'application

```
┌─────────────────────────────────────┐
│         index.html (Frontend)       │
├─────────────────────────────────────┤
│  • React Components                 │
│  • Tailwind CSS (styling)           │
│  • XLSX (Excel import/export)       │
│  • html5-qrcode (QR scanner)        │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│    LocalStorage (Base de données)   │
├─────────────────────────────────────┤
│  • Événements                       │
│  • Participants                     │
│  • Backups automatiques             │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│      Service Worker (sw.js)         │
├─────────────────────────────────────┤
│  • Cache des fichiers               │
│  • Mode hors ligne                  │
│  • Mises à jour automatiques        │
└─────────────────────────────────────┘
```

### Flux de données

1. **Création d'événement**
   ```
   Utilisateur → Formulaire → LocalStorage → Interface mise à jour
   ```

2. **Import Excel**
   ```
   Fichier Excel → XLSX.js → Parsing → LocalStorage → Affichage
   ```

3. **Scan QR**
   ```
   QR Code → html5-qrcode → ID Participant → Update LocalStorage → Confirmation
   ```

4. **Export Excel**
   ```
   LocalStorage → Formatage → XLSX.js → Téléchargement fichier
   ```

## 💾 Stockage des données

### LocalStorage Structure

```javascript
// Clés utilisées
{
  'emargement_events': [...],           // Liste des événements
  'emargement_backup': {...},           // Backup automatique
  'emargement_last_sync': '2025-01-01', // Dernière sauvegarde
  'participants_[EVENT_ID]': [...],     // Participants par événement
  'participants_[EVENT_ID]_backup': [...] // Backup des participants
}
```

### Format des événements

```javascript
{
  id: "1234567890",
  name: "Formation React 2025",
  date: "2025-01-15T10:00:00",
  lieu: "Paris",
  capacite: 50,
  description: "...",
  createdAt: "2025-01-01T08:00:00"
}
```

### Format des participants

```javascript
{
  id_client: "ABC123",
  contact: "Jean Dupont",
  gerant: "Marie Martin",
  email: "jean@example.com",
  source: "import", // ou "manuel"
  present: true,
  datePresence: "2025-01-15T10:30:00",
  modeValidation: "qr" // ou "manuel"
}
```

## 🚀 Comment ça marche ?

### 1. Chargement initial
```
1. index.html est chargé
2. Service Worker s'enregistre
3. React s'initialise
4. Données chargées depuis LocalStorage
5. Interface affichée
```

### 2. Mode hors ligne
```
1. Service Worker intercepte les requêtes
2. Si en cache → retourne depuis le cache
3. Si pas en cache → tente le réseau
4. Si réseau échoue → mode hors ligne
```

### 3. Sauvegarde automatique
```
À chaque modification:
1. Données sauvegardées dans LocalStorage
2. Backup créé automatiquement
3. Timestamp de dernière modification
```

## 🔒 Sécurité et confidentialité

- ✅ Toutes les données restent sur l'appareil
- ✅ Pas de serveur externe
- ✅ Pas de tracking
- ✅ HTTPS obligatoire (via GitHub Pages)
- ⚠️ Sauvegardez régulièrement (export JSON)

## 📱 PWA (Progressive Web App)

### Avantages
- Installation sur l'écran d'accueil
- Icône d'application native
- Plein écran (sans barre d'adresse)
- Mode hors ligne
- Notifications (non implémenté actuellement)

### Configuration
- `manifest.json` : métadonnées de l'app
- `sw.js` : gestion du cache
- Icônes : 192x192 et 512x512 px

## 🔄 Mise à jour de l'application

Pour mettre à jour :
1. Modifiez `index.html`
2. Changez le numéro de version dans `sw.js` :
   ```javascript
   const CACHE_NAME = 'emargement-v2'; // ← Incrémentez
   ```
3. Commit et push sur GitHub
4. GitHub Pages se met à jour automatiquement

## 🎨 Personnalisation

### Changer les couleurs
Dans `index.html`, modifiez les classes Tailwind :
```html
<!-- Bleu actuel : bg-blue-600 -->
<!-- Pour vert : bg-green-600 -->
<!-- Pour rouge : bg-red-600 -->
```

### Changer le logo
Remplacez `icon-192.png` et `icon-512.png` par vos propres icônes.

### Ajouter des fonctionnalités
Modifiez le code React dans `index.html` entre les balises `<script type="text/babel">`.

## 📊 Performances

### Taille des fichiers
- index.html : ~35 KB (non compressé)
- manifest.json : 1 KB
- sw.js : 2 KB
- icon-192.png : ~3 KB
- icon-512.png : ~8 KB

**Total : ~49 KB** (très léger !)

### Chargement
- Premier chargement : ~1-2 secondes
- Chargements suivants : ~0.1 seconde (cache)
- Mode hors ligne : instantané

## 🧪 Tests recommandés

Avant déploiement :
- [ ] Créer un événement
- [ ] Importer un fichier Excel
- [ ] Scanner un QR code
- [ ] Exporter en Excel
- [ ] Installer sur mobile
- [ ] Tester hors ligne
- [ ] Sauvegarder/Restaurer

## 📞 Support

En cas de problème :
1. Vérifiez la console (F12)
2. Testez dans un navigateur différent
3. Videz le cache (Ctrl+F5)
4. Vérifiez les permissions (caméra)

## 🎓 Ressources techniques

### Technologies utilisées
- React 18.2
- Tailwind CSS 3.x
- SheetJS (xlsx) 0.18.5
- html5-qrcode 2.3.8

### API du navigateur
- LocalStorage API
- Service Worker API
- MediaDevices API (caméra)
- File API

### Standards web
- PWA Manifest (W3C)
- Service Workers (W3C)
- ES6+ JavaScript

---

**Version du document : 1.0**
**Dernière mise à jour : Décembre 2025**
