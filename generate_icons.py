#!/usr/bin/env python3
"""
Script pour générer les icônes PWA pour l'application d'émargement
Nécessite: pip install Pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ Pillow n'est pas installé")
    print("Installation: pip install Pillow")
    exit(1)

def create_icon(size, filename):
    """Créer une icône avec un design simple"""
    # Créer une image avec fond bleu
    img = Image.new('RGB', (size, size), color='#2563eb')
    draw = ImageDraw.Draw(img)
    
    # Dessiner un cadre blanc
    margin = size // 8
    draw.rectangle(
        [margin, margin, size-margin, size-margin],
        outline='white',
        width=size // 20
    )
    
    # Dessiner un symbole de check
    check_margin = size // 4
    check_width = size // 15
    
    # Ligne verticale du check
    draw.line(
        [size//2, size//2, size//2, size-check_margin],
        fill='white',
        width=check_width
    )
    
    # Ligne horizontale du check
    draw.line(
        [check_margin, size//2 + size//8, size//2, size-check_margin],
        fill='white',
        width=check_width
    )
    
    # Sauvegarder
    img.save(filename, 'PNG')
    print(f"✅ Icône créée: {filename} ({size}x{size})")

def main():
    """Générer toutes les icônes nécessaires"""
    print("🎨 Génération des icônes PWA...")
    print()
    
    # Créer les icônes de différentes tailles
    sizes = [192, 512]
    
    for size in sizes:
        create_icon(size, f'icon-{size}.png')
    
    print()
    print("✅ Toutes les icônes ont été générées avec succès!")
    print()
    print("📝 Prochaines étapes:")
    print("1. Vérifiez les icônes générées")
    print("2. Si besoin, modifiez-les avec un éditeur d'images")
    print("3. Ajoutez-les à votre repository GitHub")

if __name__ == '__main__':
    main()
