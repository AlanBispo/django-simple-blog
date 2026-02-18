# 🚀 Django Simple Blog

Um sistema de blog completo e funcional desenvolvido com **Python** e **Django**, focado na aplicação da arquitetura **MVT (Model-View-Template)**.

O projeto conta com área administrativa para gestão de conteúdo, sistema de autenticação, categorias e uma interface responsiva utilizando **Bootstrap 5**.

---

## 📸 Funcionalidades

- [x] **Listagem de Postagens:** Exibição dos posts mais recentes na home.
- [x] **Leitura de Post:** Página dedicada para ler o artigo completo.
- [x] **Sistema de Categorias:** Filtragem de posts por temas.
- [x] **Busca Reativa:** Barra de pesquisa que filtra títulos em tempo real (JavaScript).
- [x] **Área Administrativa:** Painel seguro para criar, editar e excluir posts (Django Admin).
- [x] **Autenticação:** Login e Logout para administradores.
- [x] **Design Responsivo:** Layout adaptável para mobile e desktop com Bootstrap 5.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3, Django 5+
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Banco de Dados:** SQLite (Padrão do Django)

---

## 🚀 Como rodar o projeto localmente

1. Clone o repositório para sua máquina.
2. Crie e ative o ambiente virtual
    ```
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Instale as dependências

  `pip install -r requirements.txt`

5. Configure o Banco de Dados

  `python manage.py migrate`

6. Crie um Superusuário (Admin)
OBS: Para acessar o painel e criar posts, você precisa de um usuário administrador

  `python manage.py createsuperuser`

8. Inicie o Servidor

  `python manage.py runserver`

Acesse o projeto em: http://127.0.0.1:8000/

## 🤝 Contribuição
Este é um projeto de estudo. Sinta-se à vontade para abrir Issues ou enviar Pull Requests para melhorias.
