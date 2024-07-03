# Sistema Avante

Bem-vindo ao Sistema Avante! Este projeto Django é projetado para gerenciar o cadastro de usuários internos e externos, atividades e serviços com um sistema de permissões detalhado.

<br>

<div align="center">
<img src="https://github.com/Pedro-2077/Sistema_Jato/assets/139086553/7b67fc06-237b-4620-b596-78a44af57183" width="1000px"> 
</div>

<br>
<div align="center">
<img src="https://github.com/Pedro-2077/Sistema_Jato/assets/139086553/34c635e7-908b-4c72-a751-d1f33bbca13e" width="1000px"> 
</div>

## Sumário

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Gerador de Senha](#gerador-de-senha)
- [Sistema de Permissões](#sistema-de-permissões)
- [Rotas e Views](#rotas-e-views)
- [Mensagens](#mensagens)
- [Emails](#emails)
- [Validações Personalizadas](#validações-personalizadas)

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/sistema-avante.git
cd sistema-avante
pip install -r requirements.txt
```

## Configuração

### Variáveis de Ambiente

Utilizamos `python-decouple` para gerenciar as variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto e defina as seguintes variáveis:

```
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST=smtp.your-email-provider.com
```

### Banco de Dados

O projeto usa SQLite por padrão, mas você pode configurar qualquer banco de dados suportado pelo Django. No arquivo `settings.py`, ajuste as configurações do banco de dados conforme necessário.

## Funcionalidades Principais

### Cadastro e Gerenciamento de Usuários

O sistema permite o cadastro, atualização e visualização de usuários. Há diferentes tipos de usuários com permissões específicas, incluindo Administradores, Usuários Internos e Responsáveis por Atividades.

### Gerador de Senha

O sistema inclui um gerador de senha automática, que cria senhas seguras para novos usuários. As senhas são enviadas por email após o cadastro.

### Sistema de Permissões

Utilizamos a biblioteca `django-role-permissions` para gerenciar as permissões dos usuários. Há três tipos principais de usuários, cada um com um conjunto específico de permissões:

- **Administrador:** Pode cadastrar e gerenciar usuários internos e externos, atividades e inscrições.
- **Usuário Interno:** Pode cadastrar usuários externos e gerenciar inscrições.
- **Responsável por Atividades:** Pode visualizar a lista de atividades.

### Rotas e Views

#### Rotas Principais

- `/perfil/` - Visualiza todos os perfis de usuários.
- `/cadastro_usuario/` - Página para cadastro de novos usuários.
- `/login/` - Página de login.
- `/alterar_senha/` - Página para alterar a senha.
- `/update_usuario/<int:pk>/` - Atualiza os dados do usuário especificado.

#### Sistema de Login

A view de login autentica os usuários e redireciona-os para a página inicial ou para a página de alteração de senha, caso seja o primeiro login.

### Mensagens

Utilizamos o framework de mensagens do Django para fornecer feedback aos usuários sobre suas ações. As mensagens são exibidas em diferentes cores para diferentes tipos de mensagens (erro, sucesso, etc.).

### Emails

O sistema envia emails para notificar os usuários sobre suas novas contas e senhas. Durante o desenvolvimento, os emails são enviados para o console, mas no modo de produção, eles são enviados via SMTP.

### Validações Personalizadas

Incluímos validações personalizadas para garantir que os dados inseridos pelos usuários sejam válidos e consistentes.

## Conclusão

O Sistema Avante é uma solução completa para o gerenciamento de usuários e atividades, com um sistema de permissões robusto e funcionalidades práticas como geração de senha e envio de emails. Sinta-se à vontade para explorar o código e personalizá-lo conforme suas necessidades!

---

Esperamos que você ache o Sistema Avante útil e fácil de usar. Se tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue no GitHub.
