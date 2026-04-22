# Stat-2 (Édition L3 Biologie - V21)

Bienvenue sur le dépôt de **Stat-2**, un script Python spécialement conçu pour la calculatrice NumWorks. 

Ce programme a été pensé comme un véritable "assistant d'examen" pour les épreuves de **Statistiques 2**.

---

## Fonctionnalités Principales (La V21)

* **Générateur d'Hypothèses Formelles :** Avant chaque calcul, le programme affiche les hypothèses $H_0$ et $H_1$ avec la notation académique attendue par les correcteurs (utilisation des $\mu$ et des $\rho$).
*  **Assistant de Rédaction :** Fini les conclusions brouillonnes. Le programme génère le bloc de texte exact à recopier (ex: `F(3,16) = 13.89 >= F_seuil => REJET H0`).
   **Anti-sèche Théorique Intégrée :** Un menu entier est dédié aux questions de cours classiques :
  * Arbre de décision pour choisir le bon test.
  * Liste des conditions d'application à citer.
  * Interprétation des p-values sous le logiciel R (Shapiro, Bartlett).
  * Formules et propriétés magiques des résidus.

---

##  Tests Statistiques Inclus

Le menu principal (touches 1 à 8) couvre 100% de notre programme de TD et d'annales :
1. **Statistiques Descriptives** (Moyenne, Variance, Ecart-Type, Erreur Standard)
2. **Test $t$ de Student** pour échantillons indépendants
3. **Test $t$ de Student** pour échantillons appariés (liés)
4. **ANOVA à 1 facteur**
5. **ANOVA à 2 facteurs** (S'adapte automatiquement : tapez `1` au nombre de répétitions pour le modèle sans interaction !).
6. **$\chi^2$ (Chi-2) de Conformité / Fit** (Gestion des probabilités ou des effectifs théoriques)
7. **$\chi^2$ (Chi-2) d'Indépendance** (Tableaux croisés)
8. **Régression et Corrélation linéaire** (Équation de la droite $y=ax+b$ et test de significativité de $\rho$)

---

## Comment l'installer sur sa NumWorks ?

Pas besoin de savoir coder pour l'installer, suivez juste ces 5 étapes :

1. Branchez votre calculatrice à votre ordinateur avec un câble USB.
2. Allez sur le site officiel de NumWorks : [my.numworks.com/scripts](https://my.numworks.com/scripts). *(Connectez-vous ou créez un compte gratuit).*
3. Cliquez sur le bouton jaune **Nouveau script** et nommez-le `stat_2`.
4. Ouvrez le fichier `stat_2.py` présent sur ce GitHub, copiez **tout le texte**, et collez-le dans l'éditeur du site NumWorks (à la place du texte existant).
5. Cliquez sur le bouton **Envoyer sur la calculatrice** en bas de l'écran.

C'est prêt ! Débranchez votre calculatrice.

---

##  Mini-Tutoriel : Comment l'utiliser le jour J ?

Prenons l'exemple d'un **Test de Student (Option 2)** :
1. Allez dans l'application **Python** de la calculatrice, sélectionnez `stat_2.py` et appuyez sur **Exécuter le script**.
2. Le menu s'affiche. Tapez `2`.
3. Rentrez les valeurs du Groupe 1 en les séparant par un **espace** (ex: `12.5 14 16.2`), puis appuyez sur **EXE**. Faites pareil pour le Groupe 2.
4. **Étape HYPOTHÈSES :** L'écran se fige et affiche $H_0$ et $H_1$. Recopiez-les sur votre copie. Appuyez sur **EXE**.
5. **Étape CALCULS :** L'écran affiche les moyennes, variances, et le $t_{obs}$.
6. **Étape CONCLUSION :** Le programme vous demande le `Seuil table (t)`. Prenez votre table papier, croisez le risque (ex: 5%) avec les ddl affichés, et tapez la valeur trouvée.
7. Le programme vous affiche la **conclusion finale**. Vous n'avez plus qu'à recopier !

---

##  Avertissements & Conseils
* **Attention à la virgule :** Sur le clavier NumWorks, utilisez bien la touche `.` (point) pour les nombres décimaux, pas une virgule. *(Ex: tapez 14.5 et non 14,5)*.
* **Les tables ne sont pas incluses :** La calculatrice fait les calculs, mais vous **devez savoir lire vos tables statistiques papier** (Student, Fisher, Chi-2) pour fournir les seuils au programme à la fin des exercices. N'oubliez pas vos polycopiés !.

Bonnes révisions à tous et bon courage pour l'examen !
