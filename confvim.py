import os
import time

print ('Bem vindo ao customizador do vim e bash')

time.sleep(1)
def updatebash()
    print('Instalando o OH-MY-BASH')

    os.system('bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)"')

    os.system('wget -P ~/ https://raw.githubusercontent.com/wellesximenes/ws_customs/main/.bashrc ')

    print('OH-MY-BASH instalado!!!!!')


def updatenvim()
    print('Configurando o nvim')

    print('Instalando pacotes necessarios')
    time.sleep(2)

    os.system('sudo apt install cmake -y')

    os.system('bash -c wget -P /tmp  https://github.com/wellesximenes/ws_customs/blob/main/nvim.gz')

    os.system('tar -xvzf /tmp/nvim.gz -C ~/.config/')
    
    os.system('')
    

