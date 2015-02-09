let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
map! <S-Insert> *
map  h
smap 	 i<BS>	
map <NL> j
map  k
map  l
nmap  :w
vmap  "*d
nmap d :cs find d =expand("<cword>")	
nmap i :cs find i ^=expand("<cfile>")$
nmap f :cs find f =expand("<cfile>")	
nmap e :cs find e =expand("<cword>")	
nmap t :cs find t =expand("<cword>")	
nmap c :cs find c =expand("<cword>")	
nmap g :cs find g =expand("<cword>")	
nmap s :cs find s =expand("<cword>")	
map   /
vnoremap <silent> # :call VisualSelection('b')
vnoremap <silent> * :call VisualSelection('f')
map ,c <Plug>MyCapitalize
map ,pp :setlocal paste!<cr
map ,q :e ~/buffer
noremap ,m mmHmt:%s///ge'tzt'm
map ,s? z= 
map ,sa zg
map ,sp [s
map ,sn ]s
map ,ss :setlocal spell!
map ,p :cp
map ,n :cn
map ,co ggVGy:tabnew:set syntax=qfpgg
map ,cc :botright cope
vnoremap <silent> ,r :call VisualSelection('replace')
map ,  :vimgrep // %<Right><Right><Right><Right><Right><Right><Right><Right><Right>
map ,g :vimgrep // **/*.<Left><Left><Left><Left><Left><Left><Left>
map ,cd :cd %:p:h:pwd
map ,te :tabedit =expand("%:p:h")/
map ,tm :tabmove
map ,tc :tabclose
map ,to :tabonly
map ,tn :tabnew
map ,bd :1,1000 bd!
map <silent> , :noh
nmap ,w :w!
map 0 ^
map Q gq
vmap [% [%m'gv``
vmap ]% ]%m'gv``
vmap a% [%v]%
nmap gx <Plug>NetrwBrowseX
vnoremap <silent> gv :call VisualSelection('gv')
map j gj
map k gk
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
nmap <Nul><Nul>d :vert scs find d =expand("<cword>")
nmap <Nul><Nul>i :vert scs find i ^=expand("<cfile>")$	
nmap <Nul><Nul>f :vert scs find f =expand("<cfile>")	
nmap <Nul><Nul>e :vert scs find e =expand("<cword>")
nmap <Nul><Nul>t :vert scs find t =expand("<cword>")
nmap <Nul><Nul>c :vert scs find c =expand("<cword>")
nmap <Nul><Nul>g :vert scs find g =expand("<cword>")
nmap <Nul><Nul>s :vert scs find s =expand("<cword>")
nmap <Nul>d :scs find d =expand("<cword>")	
nmap <Nul>i :scs find i ^=expand("<cfile>")$	
nmap <Nul>f :scs find f =expand("<cfile>")	
nmap <Nul>e :scs find e =expand("<cword>")	
nmap <Nul>t :scs find t =expand("<cword>")	
nmap <Nul>c :scs find c =expand("<cword>")	
nmap <Nul>g :scs find g =expand("<cword>")	
nmap <Nul>s :scs find s =expand("<cword>")	
map <F5> i{ea}
nmap <M-k> :m'<-2`>my`<mzgv`yo`z
nmap <M-j> :m'>+`<my`>mzgv`yo`z
map <C-Space> ?
vnoremap <M-k> gt
onoremap <M-k> gt
vnoremap <M-j> gT
onoremap <M-j> gT
nmap <F3> =strftime("%Y-%m-%d %a %I:%M %p")
vmap <C-Del> "*d
vmap <S-Del> "*d
vmap <C-Insert> "*y
vmap <S-Insert> "-d"*P
nmap <S-Insert> "*P
imap 	 <Plug>Jumper
imap  :wa
inoremap  u
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set autoread
set background=dark
set backspace=eol,start,indent
set cindent
set cmdheight=2
set cscopetag
set cscopeverbose
set expandtab
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set fileformats=unix,dos,mac
set guifont=Consolas:h12:cANSI
set guioptions=grLte
set guitablabel=%M\ %t
set helplang=Ch
set hidden
set history=50
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set lazyredraw
set listchars=tab:>-,trail:-
set matchtime=2
set ruler
set scrolloff=7
set shiftwidth=4
set showmatch
set showtabline=2
set smartcase
set smartindent
set smarttab
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l
set noswapfile
set switchbuf=useopen,usetab,newtab
set tabstop=4
set termencoding=utf-8
set textwidth=500
set timeoutlen=500
set viminfo=%,'100,<50,s10,h,rA:,rB:
set whichwrap=b,s,<,>,h,l
set wildignore=*.o,*~,*.pyc
set wildmenu
set window=32
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~\Desktop
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 E:\github_workspace\Python\Vim\dot_Vim\boring.vim
badd +5 E:\github_workspace\Python\Vim\a.py
badd +431 D:\Vim\_vimrc
badd +18 E:\github_workspace\Python\Vim\Myrecode.vim
badd +1 E:\github_workspace\Python\Vim\wc
badd +4 E:\github_workspace\Python\Vim\a.cpp
badd +1 E:\github_workspace\Python\Vim\b.cpp
badd +1 E:\github_workspace\Python\Vim\makefile.o
badd +1 E:\github_workspace\Python\Vim\a.cp
badd +1 E:\github_workspace\Python\Vim\c.cpp
badd +1 E:\github_workspace\Python\Vim\Books\README.md
silent! argdel *
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe '1resize ' . ((&lines * 13 + 16) / 33)
exe '2resize ' . ((&lines * 16 + 16) / 33)
exe 'vert 2resize ' . ((&columns * 49 + 49) / 99)
exe '3resize ' . ((&lines * 16 + 16) / 33)
exe 'vert 3resize ' . ((&columns * 49 + 49) / 99)
argglobal
edit D:\Vim\vim73\doc\help.txt
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=
setlocal nobuflisted
setlocal buftype=help
setlocal cindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=nc
setlocal conceallevel=2
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'help'
setlocal filetype=help
endif
setlocal foldcolumn=0
setlocal nofoldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcroql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=!-~,^*,^|,^\"
setlocal keywordprg=
set linebreak
setlocal linebreak
setlocal nolisp
set list
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal nomodifiable
setlocal nrformats=octal,hex
set number
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal readonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal smartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'help'
setlocal syntax=help
endif
setlocal tabstop=8
setlocal tags=
setlocal textwidth=78
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
wincmd w
argglobal
enew
file ~\
nnoremap <buffer> <silent> C :let g:netrw_chgwin= winnr()
nnoremap <buffer> <silent> c :exe "keepjumps lcd ".fnameescape(b:netrw_curdir)
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> <F1> :he netrw-quickhelp
imap <buffer>  <Plug>NetrwHideEdit
imap <buffer>  <Plug>NetrwRefresh
inoremap <buffer> <silent> C :let g:netrw_chgwin= winnr()
inoremap <buffer> <silent> c :exe "keepjumps lcd ".fnameescape(b:netrw_curdir)
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=delete
setlocal nobuflisted
setlocal buftype=nofile
setlocal cindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal cursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'netrw'
setlocal filetype=netrw
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,128-167,224-235,.,~,-,*,/
setlocal keywordprg=
set linebreak
setlocal linebreak
setlocal nolisp
set list
setlocal list
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal nomodifiable
setlocal nrformats=octal,hex
set number
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal readonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal smartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'netrw'
setlocal syntax=netrw
endif
setlocal tabstop=32
setlocal tags=
setlocal textwidth=500
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
lcd ~\Desktop
wincmd w
argglobal
enew
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal cindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != ''
setlocal filetype=
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,128-167,224-235
setlocal keywordprg=
set linebreak
setlocal linebreak
setlocal nolisp
set list
setlocal list
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal smartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != ''
setlocal syntax=
endif
setlocal tabstop=4
setlocal tags=
setlocal textwidth=500
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
wincmd w
2wincmd w
exe '1resize ' . ((&lines * 13 + 16) / 33)
exe '2resize ' . ((&lines * 16 + 16) / 33)
exe 'vert 2resize ' . ((&columns * 49 + 49) / 99)
exe '3resize ' . ((&lines * 16 + 16) / 33)
exe 'vert 3resize ' . ((&columns * 49 + 49) / 99)
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
