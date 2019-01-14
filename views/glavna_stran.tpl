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


<form action="iskanje/" method="get">
<input type="text" name="tekmovalec" value="" />
<input type="submit" value="Išči tekmovalca">
</form>