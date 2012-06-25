:set autoindent copyindent mouse=a
:syntax enable
:set shiftwidth=4

"http://vim.1045645.n5.nabble.com/Keeping-tab-indentation-of-blank-lines-tp1154263p1154269.html
:inoremap <Enter> <Enter><space><bs>
:nnoremap o o<space><bs>

"One more. Why can’t there be a simpler way?
:nnoremap O O<space><bs>
