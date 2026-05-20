document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const btn = this.querySelector('input[type="submit"]');
            if (btn) {
                btn.value = "Processando...";
                btn.style.cursor = "wait";
            }
        });
    });
});