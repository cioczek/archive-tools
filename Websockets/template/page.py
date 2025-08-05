body = """
<!DOCTYPE html>
<html>
    <head>
       
        <style>
            .rounded {
               border-radius: 0px
            }
            body {
                background-color: coral;
            }
            #messages {
                max-height: 400px;
                overflow-y: auto;
                border: 1px solid #ccc;
                padding: 10px;
                background-color: #f8f9a;
            }
        </style>
        <title>Chatzão</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="p-3 mb-2 bg-secondary text-white">
        <div class=" rounded container mt-3 p-3 mb-2 bg-body text-dark ">
            <h1 align="center">Chat do Nicão 😘👍</h1>
            <p> <span id="ws-id"></span></p>

            <!-- Modal para pedir nome -->
            <div class="modal" id="nameModal" tabindex="-1">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Digite seu nome</h5>
                        </div>
                        <div class="modal-body">
                            <input type="text" class="form-control" id="nameInput" placeholder="Seu nome">
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-primary" onclick="startChat()">Entrar</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Form de mensagens -->                  
            <ul id='messages' class="mt-5 list-group"></ul>
            <br>
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" class="form-control" id="messageText" autocomplete="off"/><br>
                
                <button  class=" btn btn-primary btn-lg">Enviar</button>
            </form>

              
        </div>

        <!-- Bootstrap JS -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>

        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;

            var ws;
            var name;

            // Mostra o modal assim que a página carrega
            var nameModal = new bootstrap.Modal(document.getElementById('nameModal'));
            nameModal.show();

            function startChat() {
                name = document.getElementById("nameInput").value.trim();
                if (!name) {
                    alert("Digite um nome!");
                    return;
                }
                nameModal.hide(); // Fecha o modal

                // Abre a conexão WebSocket
                ws = new WebSocket(`ws://192.168.10.149:8000/ws/${client_id}`);
                ws.onopen = function() {
                    ws.send(name); // Envia o nome como primeira mensagem
                };
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages');
                    var message = document.createElement('li');
                    message.classList.add('list-group-item');
                    message.textContent = event.data;
                    messages.appendChild(message);
                    messages.scrollTop = messages.scrollHeight;
                };
            }

            function sendMessage(event) {
                event.preventDefault();
                var input = document.getElementById("messageText");
                if (input.value.trim() === "") return;
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
</html>
"""
