% rebase('osnova')

<h1 class="title">Pozdravljeni na strani olimpijskih iger. </h1>


<ul>
% for leto, url in leto:
    <li>
        <a href="{{ url }}">
            Olimpijske igre leta  {{leto}}
        </a>
    </li>
% end
</ul>

 Vpišite ime osebe ali del imena osebe ter preverite njene uvrstitve:

<form action="iskanjeTekmovalcev/" method="get">
<input type="text" name="tekmovalec" value="" />
<input type="submit" value="Išči tekmovalca">
</form>

Vpišite ime discipline:

<form action="iskanjeDiscipline/" method="get">
<input type="text" name="disciplina" value="" />
<input type="submit" value="Išči disciplino">
</form>

