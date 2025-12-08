# 🎯 DÉMARRAGE RAPIDE (3 ÉTAPES)

## Vous voulez déployer l'application maintenant ? Suivez ces 3 étapes :

### ⚡ ÉTAPE 1 : Créer le repository GitHub
1. Allez sur https://github.com/new
2. Nom : `emargement-app`
3. Cochez "Public"
4. Cliquez "Create repository"
5. **NE FERMEZ PAS LA PAGE** - gardez-la ouverte

### ⚡ ÉTAPE 2 : Uploader les fichiers

#### Option A : Glisser-déposer (plus simple)
1. Sur la page GitHub, cliquez "uploading an existing file"
2. Glissez TOUS les fichiers de ce dossier
3. Écrivez "Initial commit" en bas
4. Cliquez "Commit changes"

#### Option B : Ligne de commande
```bash
# Ouvrez un terminal dans ce dossier
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/emargement-app.git
git push -u origin main
```

### ⚡ ÉTAPE 3 : Activer GitHub Pages
1. Dans votre repository, cliquez "Settings" (en haut)
2. Dans le menu de gauche, cliquez "Pages"
3. Source : "Deploy from a branch"
4. Sélectionnez : Branch "main" + folder "/ (root)"
5. Cliquez "Save"

### ✅ C'EST TERMINÉ !

Votre application sera disponible dans 2-3 minutes à :
```
https://VOTRE_USERNAME.github.io/emargement-app/
```

---

## 📱 INSTALLATION SUR MOBILE

### Android
1. Ouvrez l'URL dans Chrome
2. Menu (⋮) → "Installer l'application"

### iPhone
1. Ouvrez l'URL dans Safari
2. Bouton Partage → "Sur l'écran d'accueil"

---

## 📋 CHECKLIST AVANT ÉVÉNEMENT

- [ ] Tester la création d'un événement
- [ ] Importer la liste des participants
- [ ] Vérifier le scanner QR (autorisations caméra)
- [ ] Exporter les données (sauvegarde de sécurité)
- [ ] Installer l'app sur votre téléphone
- [ ] Tester en mode hors ligne

---

## 🆘 PROBLÈMES ?

**La page ne s'affiche pas ?**
→ Attendez 5 minutes, puis rechargez (Ctrl+F5)

**Le scanner ne marche pas ?**
→ Autorisez l'accès à la caméra dans les paramètres

**Données perdues ?**
→ Importez votre sauvegarde JSON (Paramètres → Importer)

---

## 📖 DOCUMENTATION COMPLÈTE

Pour plus de détails, consultez :
- `README.md` - Documentation complète
- `INSTALLATION.md` - Guide détaillé
- `STRUCTURE.md` - Architecture technique

---

**Temps total : 5 minutes**

Besoin d'aide ? Vérifiez la console du navigateur (touche F12).
