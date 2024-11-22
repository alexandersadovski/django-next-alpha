document.addEventListener('DOMContentLoaded', () => {
    const matchModal = document.getElementById('match-modal');
    const closeModal = document.getElementById('close-modal');

    if (matchModal?.dataset.name) {
        document.getElementById('match-name').textContent = matchModal.dataset.name;
        matchModal.style.display = 'block';
    }

    closeModal?.addEventListener('click', () => {
        matchModal.style.display = 'none';
        window.location.href = matchModal.dataset.nextUrl;
    });
});
