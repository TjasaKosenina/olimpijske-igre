%rebase('osnova')

<h1 class="title">Iskanje discipline '{{niz}}':</h1>

<ul>
% for oseba in podatki:
    <li>{{ oseba }}</li>
% end
</ul>