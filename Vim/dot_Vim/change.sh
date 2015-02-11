for file in *.cpp; do
    vim -e  -s $file < change.vim
    lpr -r tempfile
done
