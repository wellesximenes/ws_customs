import os
import time

print ('Bem vindo ao customizador do vim e bash')

time.sleep(1)
def updatebash():
    print('Instalando o OH-MY-BASH')
    os.system('apt update -y && apt install curl git -y')

    customold = os.path.exists('/tmp/customs.py')

    if customold == True:
        os.system(
            'rm -rf /tmp/customs.py')
    bashrcold = os.path.exists('~/.bashrc')

    if bashrcold == True:
        print ('Movendo conf do bash para ~/.bashrc.old')
        os.system('mv ~/.bashrc ~/.bashrc.old')

    os.system('bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)"')


    os.system("curl  -H 'Cache-Control: no-cache, no-store' https://raw.githubusercontent.com/wellesximenes/ws_customs/main/.bashrc -o ~/.bashrc ")

    print('OH-MY-BASH instalado!!!!!')


def updatenvim():
    print('Configurando o nvim')

    print('Instalando pacotes neovim')
    os.system('apt install neovim -y')
    time.sleep(2)
    
    
    
    pastabaseconf = os.path.exists('~/.config')
    
    if pastabaseconf == True:
        print ('Pasta do conf existe')
    else:
        os.system('mkdir -p ~/.config')
    
    customold = os.path.exists('/tmp/customs.py')

    if customold == True:
        os.system(
            'rm -rf /tmp/customs.py')

    nvimold = os.path.exists('/tmp/nvim.tar.xz')
    if nvimold  == True:
            print ('Removendo caches velhos')
            time.sleep(2)
            os.system('rm -rf /tmp/nvim.tar.xz')
    nvimconfold  =  os.path.exists('~/.config/nvim')

    if nvimconfold == True:
        print ('Movendo conf do nvim para ~/nvim.old')
        os.system('mv ~/.config/nvim ~/nvim.old')
    os.system(" curl -H 'Cache-Control: no-cache, no-store' https://raw.githubusercontent.com/wellesximenes/ws_customs/main/nvim.tar.xz -o /tmp/nvim.tar.xz")
    os.system('tar -xvf /tmp/nvim.tar.xz -C ~/.config/')
    os.system("curl -H 'Cache-Control: no-cache, no-store' https://raw.githubusercontent.com/wellesximenes/ws_customs/main/nvim/init.vim -o ~/.config/nvim/init.vim")
    os.system("curl -sL install-node.vercel.app/lts | bash")
    
    print('Preparando para o YouCoplete')
    os.system(' apt install build-essential cmake vim-nox python3-dev')
    os.system('nvim -c "PlugInstall"')
#    os.system('apt install mono-complete golang nodejs default-jdk npm')

#    youcompleteexist = os.path.exists('~/.local/share/nvim/plugged/YouCompleteMe')
#    if nvimold  == True:
#            print ('Removendo old Youcomplete')
#            time.sleep(2)
#            os.system('rm -rf ~/.local/share/nvim/plugged/YouCompleteMe')

 #   os.system('cd ~/.local/share/nvim/plugged && git clone https://github.com/ycm-core/YouCompleteMe && cd ~/.local/share/nvim/plugged/YouCompleteMe && git submodule update --init --recursive && python3 ~/.local/share/nvim/plugged/YouCompleteMe/install.py    ')

    print('')
    print('Quase no fim agora execute no vim  PlugInstall !!!')
    print('rodar  CocInstall coc-pyright ')
    print('')

def menu():
    opcao =0
    while opcao !=5:
        print('''
                ------Menu de servidores------

                [1] Instalar e ataualizar o OH-MY-BASH
                [2] Instalar e atualizar o nvim
                [3] Instalar Tudo!!!
                [0] Para sair      ''')
        print('')
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            updatebash()
        elif opcao == 2:
            updatenvim()
        elif opcao == 3:
            updatenvim()
            updatenvim()    
        else:
            print('BYEEE')
            opcao =5
menu()


