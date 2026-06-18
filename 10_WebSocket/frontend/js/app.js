// Configuração da URL da API FastAPI
const API_URL = 'http://127.0.0.1:8000/users';

// Elementos do DOM
const userForm = document.getElementById('user-form');
const userIdInput = document.getElementById('user-id');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const formTitle = document.getElementById('form-title');
const btnSubmit = document.getElementById('btn-submit');
const btnCancel = document.getElementById('btn-cancel');
const usersContainer = document.getElementById('users-container');

// Estado da aplicação (armazena os usuários localmente para evitar fetches redundantes)
let isEditing = false;

// Inicialização
document.addEventListener('DOMContentLoaded', fetchUsers);
userForm.addEventListener('submit', handleFormSubmit);
btnCancel.addEventListener('click', resetForm);

/**
 * Busca todos os usuários (GET /users)
 */
async function fetchUsers() {
    showLoading();
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error('Erro ao buscar usuários');

        const users = await response.json();
        renderUsers(users);
    } catch (error) {
        console.error(error);
        usersContainer.innerHTML = `<div class="empty-list">Não foi possível carregar os usuários. Verifique se a API FastAPI está ativa.</div>`;
    }
}

/**
 * Renderiza os cards de usuários na tela
 */
function renderUsers(users) {
    usersContainer.innerHTML = '';

    if (users.length === 0) {
        usersContainer.innerHTML = '<div class="empty-list">Nenhum usuário cadastrado ainda.</div>';
        return;
    }

    users.forEach(user => {
        const card = document.createElement('div');
        card.className = 'user-card';
        card.innerHTML = `
            <div class="user-info">
                <h3>${escapeHTML(user.name)}</h3>
                <p><i class="fa-regular fa-envelope"></i> ${escapeHTML(user.email)}</p>
            </div>
            <div class="user-actions">
                <button class="btn btn-sm btn-edit" onclick="setupEditUser(${user.id}, '${escapeHTML(user.name)}', '${escapeHTML(user.email)}')">
                    <i class="fa-solid fa-pen"></i> Editar
                </button>
                <button class="btn btn-sm btn-delete" onclick="deleteUser(${user.id})">
                    <i class="fa-solid fa-trash-can"></i> Excluir
                </button>
            </div>
        `;
        usersContainer.appendChild(card);
    });
}

/**
 * Processa o envio do formulário (Criar ou Atualizar)
 */
async function handleFormSubmit(event) {
    event.preventDefault();

    const userData = {
        name: nameInput.value.trim(),
        email: emailInput.value.trim()
    };

    try {
        if (isEditing) {
            // Modo Edição: PUT /users/{id}
            const id = userIdInput.value;
            const response = await fetch(`${API_URL}/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });

            if (!response.ok) throw new Error('Erro ao atualizar usuário');
        } else {
            // Modo Cadastro: POST /users
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });

            if (!response.ok) throw new Error('Erro ao cadastrar usuário');
        }

        resetForm();
        fetchUsers();
    } catch (error) {
        alert(error.message);
    }
}

/**
 * Prepara o formulário para edição de um usuário
 */
function setupEditUser(id, name, email) {
    isEditing = true;
    userIdInput.value = id;
    nameInput.value = name;
    emailInput.value = email;

    formTitle.textContent = 'Editar Usuário';
    btnSubmit.innerHTML = '<i class="fa-solid fa-floppy-disk"></i> Salvar';
    btnCancel.classList.remove('hidden');

    // Rola a tela até o formulário de forma suave em dispositivos mobile
    userForm.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Remove um usuário (DELETE /users/{id})
 */
async function deleteUser(id) {
    if (!confirm('Tem certeza que deseja excluir este usuário?')) return;

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });

        if (!response.ok) throw new Error('Erro ao excluir usuário');

        // Se o usuário excluído estava sendo editado no momento, reseta o form
        if (isEditing && userIdInput.value == id) {
            resetForm();
        }

        fetchUsers();
    } catch (error) {
        alert(error.message);
    }
}

/**
 * Reseta o formulário para o estado padrão de cadastro
 */
function resetForm() {
    isEditing = false;
    userForm.reset();
    userIdInput.value = '';
    formTitle.textContent = 'Cadastrar Novo Usuário';
    btnSubmit.innerHTML = '<i class="fa-solid fa-plus"></i> Cadastrar';
    btnCancel.classList.add('hidden');
}

function showLoading() {
    usersContainer.innerHTML = '<div class="loading"><i class="fa-solid fa-spinner fa-spin"></i> Buscando dados no servidor...</div>';
}

/**
 * Segurança simples contra ataques XSS ao injetar texto no HTML
 */
function escapeHTML(str) {
    return str.replace(/[&<>'"]/g,
        tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
    );
}

const websocket = new WebSocket(
    "ws://localhost:8000/ws"
);

websocket.onopen = () => {
    console.log("Conectado ao servidor!");
};

websocket.onmessage = (event) => {
    console.log(event.data);
};

function enviarMensagem() {

    const mensagem =
        document.getElementById("mensagem").value;

    websocket.send(mensagem);
}