 <script>
        document.getElementById("buscarCEP").addEventListener("click", function() {
            const cep = document.getElementById("cep").value;
            const cidadeInput = document.getElementById("cidade");

            // Fazer a solicitação à API do CEP
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        // Preencher o campo de cidade com os dados da API
                        cidadeInput.value = data.localidade;
                        // Preencha outros campos do formulário conforme necessário
                    } else {
                        alert("CEP não encontrado.");
                    }
                })
                .catch(error => {
                    console.error("Erro na solicitação da API: ", error);
                });
        });
    </script>






