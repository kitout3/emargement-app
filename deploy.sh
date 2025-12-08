#!/bin/bash
# Script de déploiement rapide pour GitHub Pages
# Usage: ./deploy.sh "Message de commit"

echo "🚀 Déploiement de l'application d'émargement"
echo ""

# Vérifier si Git est initialisé
if [ ! -d .git ]; then
    echo "⚠️  Git n'est pas initialisé. Initialisation..."
    git init
    git branch -M main
    echo "✅ Git initialisé"
fi

# Ajouter tous les fichiers
echo "📦 Ajout des fichiers..."
git add .

# Commit avec le message fourni ou un message par défaut
if [ -z "$1" ]; then
    MESSAGE="Mise à jour de l'application - $(date +'%Y-%m-%d %H:%M')"
else
    MESSAGE="$1"
fi

echo "💾 Commit: $MESSAGE"
git commit -m "$MESSAGE"

# Vérifier si le remote origin existe
if ! git remote | grep -q origin; then
    echo ""
    echo "⚠️  Remote 'origin' non configuré"
    echo "Veuillez exécuter:"
    echo "git remote add origin https://github.com/VOTRE_USERNAME/emargement-app.git"
    echo ""
    echo "Ou créez d'abord votre repository sur GitHub:"
    echo "https://github.com/new"
    exit 1
fi

# Push vers GitHub
echo "🌐 Envoi vers GitHub..."
git push -u origin main

echo ""
echo "✅ Déploiement terminé !"
echo ""
echo "📱 Votre application sera disponible dans 2-3 minutes à:"
echo "https://VOTRE_USERNAME.github.io/emargement-app/"
echo ""
echo "💡 N'oubliez pas d'activer GitHub Pages si ce n'est pas déjà fait:"
echo "Repository Settings → Pages → Source: main branch"
