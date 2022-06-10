import os
import time

print ('Bem vindo ao customizador do vim e bash')

time.sleep(1)
def updatebash():
    print('Instalando o OH-MY-BASH')

    os.system('bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)"')

    os.system('wget -O ~/.bashrc https://raw.githubusercontent.com/wellesximenes/ws_customs/main/.bashrc ')

    print('OH-MY-BASH instalado!!!!!')


def updatenvim():
    print('Configurando o nvim')

    print('Instalando pacotes necessarios')
    time.sleep(2)

    os.system('sudo apt install cmake -y')

    os.system(' wget -P /tmp  https://github.com/wellesximenes/ws_customs/blob/main/nvim.tar.gz')

    os.system('tar -xvzf /tmp/nvim.gz -C ~/.config/')
#    os.system('/home/welles/.local/share/nvim/plugged/YouCompleteMe/install.py')
    print('Quase no fim agora o PlugInstall no vim e compile o YouCompleteMe')
    print('Comando: ~/.local/share/nvim/plugged/YouCompleteMe/install.py')
def menu():
    opcao =0 
    while opcao !=5:
        print('''
                ------Menu de servidores------

                [1] Instalar e ataualizar o OH-MY-BASH
                [2] Instalar e atualizar o nvim
                [0] Para sair      ''')
        print('')
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            updatebash()
        elif opcao == 2:
            updatenvim()
        else:
            print('BYEEE')
            opcao =5
menu()            


