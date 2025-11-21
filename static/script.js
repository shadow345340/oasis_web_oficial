document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const formMessage = document.getElementById('formMessage');

    formMessage.textContent = 'Enviando mensaje...';
    formMessage.style.color = '#3498db'; // Azul

    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error de red o del servidor.');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            formMessage.textContent = '¡Gracias! Tu mensaje ha sido guardado con éxito.';
            formMessage.style.color = 'green';
            form.reset();
        } else {
            formMessage.textContent = data.message || 'Hubo un error al guardar el mensaje.';
            formMessage.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        formMessage.textContent = 'Hubo un error de conexión. Inténtalo de nuevo más tarde.';
        formMessage.style.color = 'red';
    });
});