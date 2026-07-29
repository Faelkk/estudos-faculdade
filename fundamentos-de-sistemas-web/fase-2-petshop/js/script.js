document.addEventListener("DOMContentLoaded", () => {
    const elementoDataHora = document.querySelector("#dataHoraAtual");
    const formulario = document.querySelector("#formAgendamento");

    if (elementoDataHora) {
        atualizarDataHora(elementoDataHora);
        window.setInterval(() => atualizarDataHora(elementoDataHora), 1000);
    }

    if (formulario) {
        configurarFormulario(formulario);
    }
});

/**
 * Exibe data e hora em português e demonstra o uso de uma função temporal.
 */
function atualizarDataHora(elemento) {
    const agora = new Date();
    elemento.dateTime = agora.toISOString();
    elemento.textContent = new Intl.DateTimeFormat("pt-BR", {
        dateStyle: "full",
        timeStyle: "medium"
    }).format(agora);
}

/**
 * Gera uma data local no formato aceito por input[type="date"].
 * O uso da data local evita mudanças de dia causadas pelo fuso horário.
 */
function dataLocalParaInput(data) {
    const ano = data.getFullYear();
    const mes = String(data.getMonth() + 1).padStart(2, "0");
    const dia = String(data.getDate()).padStart(2, "0");
    return `${ano}-${mes}-${dia}`;
}

function configurarFormulario(formulario) {
    const campoData = formulario.querySelector("#dataAgendamento");
    const campoHora = formulario.querySelector("#horaAgendamento");
    const opcoesModalidade = formulario.querySelectorAll('input[name="modalidade"]');
    const mensagemModalidade = document.querySelector("#mensagemModalidade");
    const resultado = document.querySelector("#resultadoAgendamento");
    const hoje = dataLocalParaInput(new Date());

    campoData.min = hoje;

    opcoesModalidade.forEach((opcao) => {
        opcao.addEventListener("change", () => {
            atualizarMensagemModalidade(opcao.value, mensagemModalidade);
        });
    });

    campoData.addEventListener("change", () => {
        ajustarHorarioDoDia(campoData, campoHora);
        validarDataEHorario(campoData, campoHora);
    });

    campoHora.addEventListener("change", () => {
        validarDataEHorario(campoData, campoHora);
    });

    formulario.addEventListener("submit", (evento) => {
        evento.preventDefault();
        validarDataEHorario(campoData, campoHora);
        formulario.classList.add("was-validated");

        if (!formulario.checkValidity()) {
            const primeiroInvalido = formulario.querySelector(":invalid");
            primeiroInvalido?.focus();
            resultado.hidden = true;
            return;
        }

        mostrarResumo(formulario, resultado);
    });
}

function atualizarMensagemModalidade(modalidade, elemento) {
    if (modalidade === "Tele-busca") {
        elemento.textContent = "Na tele-busca, utilizaremos o endereço informado no cadastro para buscar e devolver o pet.";
        return;
    }

    elemento.textContent = "Na entrega no local, o responsável deverá levar e buscar o pet no endereço do Petshop Amigo Fiel.";
}

/**
 * Aos sábados o atendimento termina às 13h; nos demais dias úteis, às 18h.
 */
function ajustarHorarioDoDia(campoData, campoHora) {
    if (!campoData.value) {
        campoHora.max = "18:00";
        return;
    }

    const dataSelecionada = new Date(`${campoData.value}T12:00:00`);
    campoHora.max = dataSelecionada.getDay() === 6 ? "13:00" : "18:00";
}

function validarDataEHorario(campoData, campoHora) {
    campoData.setCustomValidity("");
    campoHora.setCustomValidity("");

    if (!campoData.value) {
        return;
    }

    const hoje = dataLocalParaInput(new Date());
    const dataSelecionada = new Date(`${campoData.value}T12:00:00`);

    if (campoData.value < hoje) {
        campoData.setCustomValidity("Escolha hoje ou uma data futura.");
        return;
    }

    if (dataSelecionada.getDay() === 0) {
        campoData.setCustomValidity("O petshop não atende aos domingos.");
        return;
    }

    if (!campoHora.value) {
        return;
    }

    const limiteFinal = dataSelecionada.getDay() === 6 ? "13:00" : "18:00";
    if (campoHora.value < "09:00" || campoHora.value > limiteFinal) {
        campoHora.setCustomValidity(`Escolha um horário entre 09:00 e ${limiteFinal}.`);
        return;
    }

    const agendamento = new Date(`${campoData.value}T${campoHora.value}:00`);
    if (agendamento <= new Date()) {
        campoHora.setCustomValidity("Escolha um horário futuro.");
    }
}

function mostrarResumo(formulario, resultado) {
    const nomeCompleto = formulario.elements.nomeCliente.value.trim();
    const primeiroNome = nomeCompleto.split(/\s+/)[0];
    const nomePet = formulario.elements.nomePet.value.trim();
    const servico = formulario.elements.servico.value;
    const modalidade = formulario.elements.modalidade.value;
    const data = new Date(`${formulario.elements.dataAgendamento.value}T12:00:00`);
    const dataFormatada = new Intl.DateTimeFormat("pt-BR").format(data);
    const horario = formulario.elements.horaAgendamento.value;
    const mensagem = document.querySelector("#mensagemResultado");

    // textContent impede que dados digitados pelo usuário sejam interpretados como HTML.
    mensagem.textContent = `${primeiroNome}, a simulação para ${nomePet} foi registrada: ${servico}, modalidade ${modalidade}, em ${dataFormatada}, às ${horario}. Nenhum dado foi transmitido. O formulário foi preservado para permitir revisão.`;
    resultado.hidden = false;
    resultado.focus();
}
