"Plugins incorporados """""""""""""""""""""""""""""""""""""""""""""""""""""""
call plug#begin()
"Plug 'ycm-core/YouCompleteMe' "Autocomplete
Plug 'sheerun/vim-polyglot'   " Highlight para varias linguas
Plug 'terryma/vim-multiple-cursors' "Multiplo cursor
Plug 'morhetz/gruvbox' "Tema Dark
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } } " Facilita busca de arquivos
Plug 'junegunn/fzf.vim' " Facilita busca 
Plug 'ncm2/ncm2' "Autocompletar
Plug 'roxma/nvim-yarp' "Requisito ncm2
Plug 'ncm2/ncm2-bufword' "Autocompletar do buffer
Plug 'ncm2/ncm2-path' "Autocompletar de caminho
Plug 'dense-analysis/ale'  "Auxiliador de sintase
Plug 'jiangmiao/auto-pairs' "Completar aspas e virgulas
Plug 'tc50cal/vim-terminal' "Abrir o terminal dentro do vim
Plug 'tpope/vim-fugitive' "Plugin git vim 
Plug 'preservim/nerdtree' "Facilita abrir varias janelas
Plug 'airblade/vim-gitgutter' "Verifica mudanças no arquivo em realação ao git repositorio
Plug 'itchyny/lightline.vim' "Roda pé luminoso com indicações de status e info do arquivo
call plug#end()

"Configurações Globais """"""""""""""""""""""""""""""""""""""""""""""


set syntax=on        " Habilitar High Light
set nu               " Habilitar Exibição de numeros
set tabstop=4        " Habilitando 4 espaços por tab
set softtabstop=4    " Mostrar guia existente com 4 espaços de largura
set shiftwidth=4     " Ao recuar com '>', use 4 espaços de largura
set expandtab        " Ao pressionar tab, insira 4 espaços
set smarttab         " Tabulações no início de uma linha de acordo com o prazo de inserção
set smartindent      " Insere automaticamente um nível extra de recuo em alguns casos
set hidden           " Esconde o buffer atual quando um novo arquivo é aberto
set incsearch        " Pesquisa incremental
set ignorecase       " Ignorar maiusculo e minisculo na busca
set smartcase        " Considere maiúsculas se houver um caractere maiúsculo
set scrolloff=8      " Número mínimo de linhas a manter acima e abaixo do cursor
set colorcolumn=100  " Desenha uma linha para manter-se ciente do tamanho da linha
set signcolumn=yes   " Adicione uma coluna à esquerda. Útil para linting
set cmdheight=2      " Dê mais espaço para exibir mensagens
set updatetime=100   " Tempo em milissegundos para considerar as mudanças
set encoding=utf-8   " A codificação deve ser utf-8 para ativar os ícones de fonte
set nobackup         " Não fazer backup arquivo
set nowritebackup    " Não fazer backup arquivo
set splitright       " Crie as divisões verticais à direita
set splitbelow       " Crie as divisões horizontais abaixo
set autoread         " Atualize o vim após a atualização do arquivo de fora
"set mouse=a         " Enable mouse support
filetype on          " Detecte e defina a opção de tipo de arquivo e acione o evento FileType
filetype plugin on   " Carregue o arquivo de plug-in para o tipo de arquivo, se houver
filetype indent on   " Carregue o arquivo a identação para o tipo de arquivo, se houver
set inccommand=split " Exibe a pesquisa do substituir online na busca 
  
"Configurações do tema
colorscheme gruvbox "Sub verão do tema
set background=dark "Cor de fundo
autocmd BufEnter * call ncm2#enable_for_buffer()
set completeopt=noinsert,menuone,noselect



"Autocmd Configuração de ações """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
set completeopt=noinsert,menuone,noselect " Ativando ncm
 autocmd BufEnter * call ncm2#enable_for_buffer()



"Configurações de atalho """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
let mapleader ="\<space>"

noremap <leader>ev :vsplit ~/.config/nvim/init.vim <cr>

nnoremap <c-p> :Files<cr> "Atalho para files
nnoremap <c-f> :Ag<space>
nnoremap <leader>sv :source ~/.config/nvim/init.vim <cr>
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
