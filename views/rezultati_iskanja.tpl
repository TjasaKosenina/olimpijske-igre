%rebase('osnova')
Iskanje osebe '{{niz}}':

<ul>
% for (ime, priimek, uvrstitve) in podatki:
    <li>{{ ime }} {{ priimek }} {{ uvrstitve }}</li>
% end
</ul>