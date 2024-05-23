document.addEventListener("DOMContentLoaded", function() {
    var categoriasLink = document.getElementById("categorias");
    var submenuCategorias = document.getElementById("submenu-categorias");

    categoriasLink.addEventListener("click", function(event) {
        event.preventDefault();
        submenuCategorias.classList.toggle("show");
    });
});
