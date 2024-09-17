/*document.addEventListener("DOMContentLoaded", function() {
    var categoriasLink = document.getElementById("categorias");
    var submenuCategorias = document.getElementById("submenu-categorias");

    categoriasLink.addEventListener("click", function(event) {
        event.preventDefault();
        submenuCategorias.classList.toggle("show");
    });
});
*/

document.addEventListener("DOMContentLoaded", function() {
    var agendamentosLink = document.querySelector(".amenu[href='#']");
    var submenu = agendamentosLink.nextElementSibling;

    agendamentosLink.addEventListener("click", function(event) {
        event.preventDefault();
        submenu.classList.toggle("show");
    });
});

