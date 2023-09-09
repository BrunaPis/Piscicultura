document.addEventListener('DOMContentLoaded', function() {
    const cepSelect = document.getElementById('cep');



    fetch('https://viacep.com.br/ws/')
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.nome;
                option.textContent = item.nome;
                cepSelect.appendChild(option);
            });

            cepSelect.value = "{{ db.cep }}";
        })
        .catch(error => console.error('Erro ao buscar dados do estado:', error));



});