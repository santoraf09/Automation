
def cadastrar():
    # Função chamada quando o botão é clicado
    def cadastrar_usuario():
        # Obtendo os dados dos campos de entrada
        n_conta = n_conta_entry.get()
        sigla = sigla_entry.get()
        nome = nome_entry.get()
        sobrenome = sobrenome_entry.get()
        nome_completo = nome_completo_entry.get()
        email = email_entry.get()
        # Função que será executada em uma thread para realizar o cadastro

        def realizar_cadastro():
            with sync_playwright() as p:
                navegador = p.chromium.launch(headless=False)
                pagina = navegador.new_page()
                try:
                    pagina.goto("LINK")
                    # preencha os detalhes de login
                    pagina.fill('xpath=/html/body/div[1]/div/div/form/div/div/div/div/div/div/div[2]/input',
                                "USUÁRIO")
                    pagina.fill('xpath=/html/body/div[1]/div/div/form/div/div/div/div/div/div/div[3]/span[2]/input[2]',
                                "SENHA*")
                    pagina.select_option('xpath=/html/body/div[1]/div/div/form/div/div/div/div/div/div/div[4]/select',
                                         "OBJETO A SER SELECIONADO")
                    pagina.click('xpath=/html/body/div[1]/div/div/form/div/div/div/div/div/div/div[5]/button')

                    pagina.click('xpath=/html/body/div[1]/div/div[1]/div/ul/li[4]/a/span')
                    pagina.click('xpath=/html/body/div[1]/div/div[1]/div/ul/li[4]/ul/li[2]/a/span')
                    pagina.click('xpath=/html/body/div[1]/div/div[2]/form/div[2]/select')
                    pagina.select_option('xpath=/html/body/div[1]/div/div[2]/form/div[2]/select', 'Todos')
                    pagina.fill('xpath=/html/body/div[1]/div/div[2]/form/div[2]/input[2]', nome_completo)
                    pagina.click('xpath=/html/body/div[1]/div/div[2]/form/div[1]/input')

                    time.sleep(1)

                    # Captura o conteúdo HTML da página
                    html_content = pagina.content()

                    # Parseie o conteúdo HTML com BeautifulSoup
                    soup = BeautifulSoup(html_content, 'html.parser')

                    # Encontre todos os elementos <a> com o atributo title igual ao nome
                    elementos_ancora = soup.find_all('a', title=nome_completo)

                    if elementos_ancora:
                        # Atualizar o rótulo com a mensagem de usuário já existente
                        status_label.config(text="Usuário já existe")
                        return
                    else:
                        # Atualizar o rótulo com a mensagem de usuário cadastrado com sucesso
                        status_label.config(text="Usuário cadastrado com sucesso!")
                        pagina.click('xpath=/html/body/div[1]/div/div[1]/div/ul/li[4]/ul/li[1]/a/span')
                        pagina.click('xpath=/html/body/div[1]/div/div[2]/form/div[2]/select')
                        pagina.select_option('xpath=/html/body/div[1]/div/div[2]/form/div[2]/select', 'USUÁRIO')
                        pagina.fill('xpath=/html/body/div[1]/div/div[2]/form/div[2]/input[1]', sigla)
                        pagina.fill('xpath=/html/body/div[1]/div/div[2]/form/div[2]/input[2]', nome_completo)
                        pagina.fill('xpath=/html/body/div[1]/div/div[2]/form/div[2]/input[6]', email)
                        pagina.click('xpath=/html/body/div[1]/div/div[2]/form/div[1]/button[1]')
                        print("Usuário cadastrado com sucesso!")
                        time.sleep(2)

                finally:
                    navegador.close()

            with sync_playwright() as p:
                navegador = p.chromium.launch(headless=False)
                pagina = navegador.new_page()
                try:
                    pagina.goto("LINK")
                    pagina.fill('xpath=/html/body/div/div[5]/div[1]/div[1]/form/table[1]/tbody/tr[4]/td[2]/input',
                                "USUÁRIO")
                    pagina.fill('xpath=/html/body/div/div[5]/div[1]/div[1]/form/table[1]/tbody/tr[5]/td[2]/input',
                                "SENHA")
                    pagina.locator(
                        'xpath=/html/body/div/div[5]/div[1]/div[1]/form/table[1]/tbody/tr[8]/td[2]/input['
                        '1]').click()
                    # Realizar Cadastro
                    pagina.locator(
                        'xpath=/html/body/div[1]/div[24]/div/div/table/tbody/tr/td/div/div/table/tbody/tr['
                        '3]/td/div/table/tbody/tr/td/div/table/tbody/tr['
                        '2]/td/div/table/tbody/tr/td/div/table/tbody/tr['
                        '2]/td['
                        '2]/div/div').click()
                    pagina.fill(
                        'xpath=/html/body/div[1]/div[25]/div[1]/table/tbody/tr[3]/td/table/tbody/tr['
                        '1]/td/div/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr['
                        '5]/td/div/div['
                        '2]/div/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td[1]/input',
                        n_conta)
                    pagina.fill(
                        'xpath=/html/body/div[1]/div[25]/div[1]/table/tbody/tr[3]/td/table/tbody/tr['
                        '1]/td/div/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr['
                        '5]/td/div/div['
                        '2]/div/table/tbody/tr[2]/td[2]/input',
                        nome)
                    pagina.fill(
                        'xpath=/html/body/div[1]/div[25]/div[1]/table/tbody/tr[3]/td/table/tbody/tr['
                        '1]/td/div/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr['
                        '5]/td/div/div['
                        '2]/div/table/tbody/tr[4]/td[2]/input',
                        sobrenome)
                    # Senha
                    pagina.fill(
                        'xpath=/html/body/div[1]/div[25]/div[1]/table/tbody/tr[3]/td/table/tbody/tr['
                        '1]/td/div/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr['
                        '7]/td/div/div['
                        '2]/div/table/tbody/tr[2]/td[2]/input',
                        "secid@123")
                    pagina.fill(
                        'xpath=/html/body/div[1]/div[25]/div[1]/table/tbody/tr[3]/td/table/tbody/tr['
                        '1]/td/div/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr['
                        '7]/td/div/div['
                        '2]/div/table/tbody/tr[3]/td[2]/input',
                        "secid@123")
                    pagina.locator(
                        'xpath=/html/body/div[1]/div[25]/div[1]/table/tbody/tr[3]/td/table/tbody/tr['
                        '1]/td/div/table/tbody/tr/td/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr['
                        '7]/td/div/div['
                        '2]/div/table/tbody/tr[4]/td[1]/input').click()
                    pagina.locator(
                        'xpath=/html/body/div[1]/div[25]/div[1]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div['
                        '2]/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/table/tbody/tr/td[2]').click()

                    pass

                finally:
                    navegador.close()

        # Iniciar o carregamento da barra de progresso
        progress_bar.start()

        # Criar e iniciar uma nova thread para realizar o cadastro
        threading.Thread(target=realizar_cadastro).start()

    # Configuração da janela
    root = Tk()
    root.title("Cadastro de Usuário")
    root.geometry("250x220")

    # Rótulos e campos de entrada
    Label(root, text="Nome da Conta:").grid(row=0, column=0)
    n_conta_entry = Entry(root)
    n_conta_entry.grid(row=0, column=1)

    Label(root, text="Sigla:").grid(row=1, column=0)
    sigla_entry = Entry(root)
    sigla_entry.grid(row=1, column=1)

    Label(root, text="Nome:").grid(row=2, column=0)
    nome_entry = Entry(root)
    nome_entry.grid(row=2, column=1)

    Label(root, text="Sobrenome:").grid(row=3, column=0)
    sobrenome_entry = Entry(root)
    sobrenome_entry.grid(row=3, column=1)

    Label(root, text="Nome Completo:").grid(row=4, column=0)
    nome_completo_entry = Entry(root)
    nome_completo_entry.grid(row=4, column=1)

    Label(root, text="Email:").grid(row=5, column=0)
    email_entry = Entry(root)
    email_entry.grid(row=5, column=1)

    # Botão de cadastro
    Button(root, text="Cadastrar", command=cadastrar_usuario).grid(row=6, columnspan=2)

    # Rótulo para exibir o status do cadastro
    status_label = Label(root, text="")
    status_label.grid(row=7, columnspan=2)

    # Barra de progresso
    progress_bar = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')
    progress_bar.grid(row=8, columnspan=2)
    progress_bar.stop()  # Parar a barra de progresso no início

    root.mainloop()


if __name__ == "__main__":
    cadastrar()
