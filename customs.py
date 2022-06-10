import os
import time

print ('Bem vindo ao customizador do vim e bash')

time.sleep(1)
def updatebash():
    print('Instalando o OH-MY-BASH')

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

    print('Instalando pacotes necessarios')
    time.sleep(2)
    
    customold = os.path.exists('/tmp/customs.py')

    if customold == True:
        os.system(
            'rm -rf /tmp/customs.py')
    
    os.system('sudo apt install cmake -y')
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
#    os.system('/home/welles/.local/share/nvim/plugged/YouCompleteMe/install.py')
    print('Quase no fim agora o PlugInstall no vim e compile o YouCompleteMe')
#    print('Comando: ~/.local/share/nvim/plugged/YouCompleteMe/install.py')
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


