// Funcion para mostrar el Dropdown en el avatar
const avatarDropdown = document.getElementById('navbarDropdownMenuAvatar');
avatarDropdown.addEventListener('click', toggleDropdown);
function toggleDropdown(event) {
    event.preventDefault();
    const dropdownMenu = this.nextElementSibling;
    dropdownMenu.classList.toggle('show');

// Funcion para actualizar la información dinámica en el navbar
function updateDynamicInfo() {
    const messages = [
        "⏳ FASHION SALE ESTÁN POR TERMINAR | HASTA 60% OFF ⌛️",
        "ENVÍO GRATIS PARA MIEMBROS ADICLUB",
        "DOBLE PUNTOS CON ADICLUB. ENTRA YA A NUESTRO CATÁLOGO MUNDIALISTA"
    ];

    const dynamicInfo = document.getElementById("dynamic-info");
    let currentIndex = 0;

    function updateMessage() {
        dynamicInfo.textContent = messages[currentIndex];
        currentIndex = (currentIndex + 1) % messages.length;
    }

    updateMessage(); // Muestra el primer mensaje al cargar la página
    setInterval(updateMessage, 6000); // Cambia el mensaje cada 5 segundos
}

// Llama a la función de actualización después de que la página cargue
window.onload = updateDynamicInfo;
}
