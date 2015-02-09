When I read vim.pdf, this file is just for record.

*03.8*
Normal Mode:  */# --> search for a word
              \<\> --> only match for the word               

just to remember and practice , again and again

" set the origin version of the file
Ex command: set patchmode = .orig

" copy and paste text between different file
Normal Mode:  "*yy
              "*p

" Test the command 'grep' for my mac 
" *12.8* : grep -l frame_counter *.c
" Windows has 'grep' command too, but it don't know \VimBacktick{}
Vim Command: vim \VimBacktick{}grep -l frame_counter *.c\VimBacktick{}
