 % rebase('osnova')

% if napaka:
<p>Prišlo je do napake!</p>
% end

<form method="post">
Leto: <input type="text" name="leto" value="{{leto}}" /><br />
Mesto: <input type="text" name="mesto" value="{{mesto}}" /><br />
Zacetek: <input type="text" name="zacetek" value="{{zacetek}}" /><br />
Konec: <input type="text" name="konec" value="{{konec}}" /><br />
Število držav: <input type="text" name="st_drzav" value="{{st_drzav}}" /><br />



<input type="submit" value="Dodaj olimpijske igre" />
</form>
