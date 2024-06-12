function toggleDropdown(event, dropdownId) {
    event.preventDefault();
    var dropdown = document.getElementById(dropdownId);
    dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
}

document.addEventListener("DOMContentLoaded", function() {
    // Exemplo de dados do usuário, que seriam carregados dinamicamente
    var userProfile = {
        name: "",
        picture: "" // Caminho da imagem
    };

    document.getElementById("profile-name").textContent = userProfile.name;
    document.getElementById("profile-picture").src = userProfile.picture;

    // Atualizar data atual
    var currentDate = new Date();
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    document.getElementById("current-date").textContent = currentDate.toLocaleDateString('pt-BR', options);

    // Carregar dados
    carregarAulas();
    carregarServicos();
});

function carregarAulas() {
    // Exemplo de dados das aulas
    var aulas = [
        { nome: "Aula 1", dia: "Segunda-feira", horario: "10:00 - 11:00", responsavel: "Professor A" },
        { nome: "Aula 2", dia: "Segunda-feira", horario: "11:00 - 12:00", responsavel: "Professor B" }
    ];

    var tabelaAulas = document.getElementById("tabela-aulas").getElementsByTagName('tbody')[0];

    aulas.forEach(function(aula) {
        var row = tabelaAulas.insertRow();
        row.insertCell(0).textContent = aula.nome;
        row.insertCell(1).textContent = aula.dia;
        row.insertCell(2).textContent = aula.horario;
        row.insertCell(3).textContent = aula.responsavel;
        var acoesCell = row.insertCell(4);
        acoesCell.innerHTML = '<button class="btn-presenca" onclick="abrirModal(\'presencaModal\', \'presencaAulaModal.html\')"><i class="fas fa-check"></i> Presença </button>' +
                              '<button class="btn-visualizar" onclick="abrirModal(\'visualizarModal\', \'visualizarAulaHomeModal.html\')"><i class="fas fa-eye"></i> Visualizar </button>';
    });
}

function carregarServicos() {
    // Exemplo de dados dos serviços
    var servicos = [
        { nome: "Serviço 1", dia: "Segunda-feira", horario: "14:00 - 15:00", responsavel: "Assistente A" },
        { nome: "Serviço 2", dia: "Segunda-feira", horario: "15:00 - 16:00", responsavel: "Assistente B" }
    ];

    var tabelaServicos = document.getElementById("tabela-servicos").getElementsByTagName('tbody')[0];

    servicos.forEach(function(servico) {
        var row = tabelaServicos.insertRow();
        row.insertCell(0).textContent = servico.nome;
        row.insertCell(1).textContent = servico.dia;
        row.insertCell(2).textContent = servico.horario;
        row.insertCell(3).textContent = servico.responsavel;
        var acoesCell = row.insertCell(4);
        acoesCell.innerHTML = '<button class="btn-presenca" onclick="abrirModal(\'presencaModal\', \'presencaServicoModal.html\')"><i class="fas fa-check"></i> Presença </button>' +
                              '<button class="btn-visualizar" onclick="abrirModal(\'visualizarModal\', \'visualizarServicoHomeModal.html\')"><i class="fas fa-eye"></i> Visualizar </button>';
    });
}

function abrirModal(modalId, iframeSrc) {
    var modal = document.getElementById(modalId);
    var iframe = modal.querySelector("iframe");
    iframe.src = iframeSrc;
    modal.style.display = "block";
}

function fecharModal(modalId) {
    var modal = document.getElementById(modalId);
    var iframe = modal.querySelector("iframe");
    iframe.src = "";
    modal.style.display = "none";
}

// oficial-home.js

// Função para obter a data atual formatada
function getCurrentDate() {
    var today = new Date();
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return today.toLocaleDateString('pt-BR', options);
}

// Função para atualizar a data na página
function updateCurrentDate() {
    var currentDateElement = document.getElementById('current-date');
    if (currentDateElement) {
        currentDateElement.textContent = getCurrentDate();
    }
}

// Chamar a função de atualização quando a página carregar
window.onload = function() {
    updateCurrentDate();
};
