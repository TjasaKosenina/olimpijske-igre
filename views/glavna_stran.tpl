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

Vpišite ime discipline ter preverite prvouvrščene:

<form action="iskanjeDiscipline/" method="get">
<input type="text" name="disciplina" value="" />
<input type="submit" value="Išči disciplino">
</form>



<ul>
    % if get('prijavljen', False):
    <li>
        <a href="dodaj_OI/">Dodaj olimpijske igre</a>
    </li>
    <li>
        <a href="odjava/">Odjavi se</a>
    </li>
    % end
</ul>

% if not get('prijavljen', False):
<form action="prijava/" method="post">
<input type="text" name="uporabnisko_ime" value="" />
<input type="password" name="geslo" value="" />
<input type="submit" value="Prijavi se">
</form>
<form action="registracija/" method="post">
<input type="text" name="uporabnisko_ime" value="" />
<input type="password" name="geslo" value="" />
<input type="submit" value="Registriraj se">
</form>
% end
