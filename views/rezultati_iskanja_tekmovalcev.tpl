%rebase('osnova')

<h1 class="title">Iskanje osebe '{{niz}}':</h1>

<ul>
% for (ime, priimek, uvrstitve) in podatki:
    <li><b>{{ ime }} {{ priimek }}: </b> {{uvrstitve}}</li>
% end
</ul>