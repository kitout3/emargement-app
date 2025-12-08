# 📊 GUIDE DU FORMAT EXCEL

## 🎯 Format de fichier Excel pour l'import de participants

### ✅ Colonnes acceptées

L'application accepte plusieurs variantes de noms de colonnes pour plus de flexibilité :

#### **ID d'inscription** (OBLIGATOIRE) ⚠️
Variantes acceptées :
- `ID d'inscription`
- `Id d'inscription`
- `ID Inscription`
- `Id Inscription`
- `ID_inscription`
- `id_inscription`
- `ID`
- `id`

#### **Contact / Nom** (Recommandé)
Variantes acceptées :
- `Contact`
- `Nom`
- `Nom complet`
- `contact`
- `nom`

#### **Email** (Recommandé)
Variantes acceptées :
- `Adresse email (Contact) (Relation)`
- `Adresse email`
- `Email`
- `E-mail`
- `Mail`
- `email`
- `mail`

#### **Gérant / Responsable** (Optionnel)
Variantes acceptées :
- `Gérant (Contact) (Relation)`
- `Gérant`
- `Responsable`
- `gerant`
- `responsable`

#### **Événement** (Optionnel)
Si présent, le nom de l'événement sera détecté automatiquement
- `Événement`
- `Evenement`

---

## 📋 EXEMPLE DE FICHIER EXCEL

### Structure minimale (obligatoire)
```
| ID d'inscription | Contact      |
|------------------|--------------|
| ABC123           | Jean Dupont  |
| ABC124           | Sophie Bernard |
```

### Structure complète (recommandée)
```
| ID d'inscription | Contact        | Événement           | Gérant (Contact) (Relation) | Adresse email (Contact) (Relation) |
|------------------|----------------|---------------------|-----------------------------|------------------------------------|
| ABC123           | Jean Dupont    | Formation React 2025| Marie Martin                | jean.dupont@example.com            |
| ABC124           | Sophie Bernard | Formation React 2025| Pierre Durand               | sophie.bernard@example.com         |
| ABC125           | Marc Lefebvre  | Formation React 2025| Julie Moreau                | marc.lefebvre@example.com          |
```

---

## 📥 FICHIERS D'EXEMPLE DISPONIBLES

Téléchargez le fichier Excel d'exemple avec 5 participants :
**exemple-participants.xlsx**

Ce fichier contient :
- ✅ Tous les en-têtes au bon format
- ✅ 5 exemples de participants
- ✅ Format prêt à être modifié

---

## 🔧 COMMENT PRÉPARER VOTRE FICHIER

### Option 1 : Partir de l'exemple
1. Téléchargez `exemple-participants.xlsx`
2. Ouvrez-le dans Excel
3. Remplacez les données d'exemple par vos vrais participants
4. Gardez les en-têtes tels quels
5. Sauvegardez

### Option 2 : Créer votre propre fichier
1. Créez un nouveau fichier Excel
2. **Première ligne** : Les en-têtes (voir ci-dessous)
3. **Lignes suivantes** : Vos participants (un par ligne)
4. Sauvegardez au format `.xlsx`

**En-têtes recommandés :**
```
ID d'inscription | Contact | Événement | Gérant (Contact) (Relation) | Adresse email (Contact) (Relation)
```

### Option 3 : Adapter votre fichier existant
Si vous avez déjà un fichier avec d'autres noms de colonnes :
1. Renommez vos colonnes pour qu'elles correspondent aux variantes acceptées
2. Au minimum, assurez-vous d'avoir une colonne `ID d'inscription`
3. Les autres colonnes seront détectées automatiquement

---

## ⚠️ ERREURS COURANTES ET SOLUTIONS

### ❌ "Aucun participant trouvé"

**Cause :** Pas de colonne `ID d'inscription` ou colonne vide

**Solution :**
1. Vérifiez que la première ligne contient `ID d'inscription`
2. Vérifiez que les cellules de cette colonne ne sont pas vides
3. Supprimez les lignes vides au début du fichier

### ❌ "Le fichier Excel est vide"

**Cause :** Le fichier ne contient pas de données ou est corrompu

**Solution :**
1. Ouvrez le fichier dans Excel pour vérifier qu'il contient des données
2. Assurez-vous qu'il y a au moins 2 lignes (en-têtes + 1 participant)
3. Sauvegardez-le à nouveau au format `.xlsx`

### ❌ "Erreur lors de l'import"

**Cause :** Format de fichier incorrect

**Solution :**
1. Vérifiez que c'est bien un fichier `.xlsx` ou `.xls`
2. Pas de `.csv` ou `.txt`
3. Réenregistrez depuis Excel au format "Classeur Excel (.xlsx)"

### ❌ Les accents ne s'affichent pas bien

**Cause :** Problème d'encodage

**Solution :**
1. Dans Excel : Fichier → Options → Avancé → Général
2. Vérifiez l'encodage UTF-8
3. Ou recréez le fichier à partir de l'exemple fourni

---

## 🎓 ASTUCES ET BONNES PRATIQUES

### ✅ ID d'inscription
- **Unique** : Chaque participant doit avoir un ID différent
- **Format** : Lettres, chiffres, tirets, underscores acceptés
- **Exemples** : `ABC123`, `PART-2025-001`, `INS_456`
- ⚠️ Pas de doublons : les doublons seront supprimés automatiquement

### ✅ Contact / Nom
- Format libre
- Peut contenir espaces et accents
- Exemple : `Jean-Marie Dupont`

### ✅ Email
- Format email standard : `nom@domaine.com`
- L'application ne vérifie pas la validité
- Peut rester vide si non disponible

### ✅ Gérant
- Format libre
- Peut être vide
- Utile pour identifier qui gère le contact

### ✅ Événement
- Si présent sur la première ligne, sera utilisé comme nom d'événement
- Sinon, vous devrez saisir le nom manuellement
- Peut être identique sur toutes les lignes

---

## 🔍 DÉBOGAGE

### Activer les logs de debug

Lorsque vous importez un fichier, ouvrez la console du navigateur (F12) pour voir les détails :

```
📊 Nombre de lignes trouvées: 5
📋 Colonnes détectées: ["ID d'inscription", "Contact", "Événement", ...]
✅ Événement détecté: Formation React 2025
✅ Participants extraits: 5
```

Ces informations vous aideront à comprendre ce qui est détecté ou non.

---

## 📊 LIMITES ET RECOMMANDATIONS

### Nombre de participants
- **Recommandé** : < 1000 participants par événement
- **Maximum technique** : Limité par la mémoire du navigateur (~10 000)
- **Performance optimale** : 100-500 participants

### Taille du fichier
- **Recommandé** : < 5 MB
- **Maximum** : ~50 MB (mais peut être lent)

### Format de cellules
- **Texte** : Tous les champs sont convertis en texte
- **Formules** : Les formules Excel seront évaluées
- **Dates** : Seront converties en texte
- **Nombres** : Seront convertis en texte

---

## 📖 EXEMPLES DE SCÉNARIOS

### Scénario 1 : Export depuis votre système
Vous avez un export CSV de votre système d'inscription :

1. Ouvrez le CSV dans Excel
2. Renommez les colonnes selon le format accepté
3. Sauvegardez au format `.xlsx`
4. Importez dans l'application

### Scénario 2 : Liste manuelle
Vous créez la liste manuellement :

1. Partez du fichier `exemple-participants.xlsx`
2. Supprimez les exemples
3. Ajoutez vos participants ligne par ligne
4. Sauvegardez et importez

### Scénario 3 : Plusieurs événements
Vous avez plusieurs événements :

1. Créez un fichier par événement
2. Ou utilisez la colonne `Événement` pour différencier
3. Importez chaque fichier dans l'événement correspondant

---

## 🆘 SUPPORT

Si vous rencontrez toujours des problèmes :

1. **Vérifiez** que vous utilisez le dernier `index.html`
2. **Testez** avec le fichier `exemple-participants.xlsx` fourni
3. **Consultez** la console navigateur (F12) pour voir les erreurs
4. **Vérifiez** que votre fichier s'ouvre bien dans Excel

---

## ✅ CHECKLIST AVANT IMPORT

Avant d'importer votre fichier, vérifiez :

- [ ] Le fichier est au format `.xlsx` ou `.xls`
- [ ] La première ligne contient les en-têtes
- [ ] Il y a une colonne `ID d'inscription` (ou variante)
- [ ] Chaque participant a un ID unique
- [ ] Il n'y a pas de lignes vides au début
- [ ] Le fichier s'ouvre correctement dans Excel
- [ ] Les accents s'affichent correctement

---

**Date : Décembre 2025**
**Version : 1.1 - Support étendu des formats**
