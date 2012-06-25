:set autoindent copyindent mouse=a
:syntax enable
:set shiftwidth=4

"“vim” mailing list “Keeping tab indentation of blank lines”
"http://marc.info/?l=vim&m=115791432605990
:inoremap <Enter> <Enter><space><bs>
:nnoremap o o<space><bs>

"One more. Why can’t there be a simpler way?
:nnoremap O O<space><bs>
