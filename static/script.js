function filtrerProduits() {
  // Récupérer la valeur sélectionnée dans la liste déroulante
  let categoriesSelection = document.getElementById("categories-select").value;

  // Récupérer toutes les lignes de la table de produits
  let lignesProduits = document.getElementsByTagName("tr");

  // Parcourir toutes les lignes de la table, en commençant par la deuxième ligne
  for (let i = 1; i < lignesProduits.length; i++) {
    let ligne = lignesProduits[i];
    let categorieColonne = ligne.getElementsByTagName("td")[0];

    // Si la catégorie sélectionnée est "Toutes les catégories", afficher toutes les lignes de produits
    if (categoriesSelection === "") {
      ligne.style.display = "";
    } else if (categorieColonne.innerHTML === categoriesSelection) {
      // Si la catégorie de la ligne correspond à la catégorie sélectionnée, afficher la ligne
      ligne.style.display = "";
    } else {
      // Sinon, masquer la ligne
      ligne.style.display = "none";
    }
  }
}