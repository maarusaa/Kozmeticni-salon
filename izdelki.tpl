%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">



<p class = "podnaslov">Izdelki</p>

<div>
	<ul>
		<li><a href="/izdelki/dodajIzdelek/">Dodaj nov izdelek</a></li>
		<li><a href="/izdelki/spremeniCeno/">Spremeni ceno</a></li>
		<li><a href="/izdelki/spremeniZalogo/">Spremeni zalogo</a></li>
		<li><a href="/izdelki/izbrisiIzdelek/">Izbriši izdelek</a></li>
	</ul>
</div>	

	
<div class="row">
    <div class="col s12">
		<table class="highlight">
            <tbody class="okvir_tabela">
                <table>
					<tr class="izpis">
					<th>Izdelek</th>
					<th>Cena</th>
					<th>Zaloga</th>

					</tr>

					%for izdelek in kozmeticni_izdelki:
					<tr>
					<td>{{izdelek['izdelek']}}</td>
					<td>{{izdelek['cena']}} &#8364</td>
					<td>{{izdelek['zaloga']}}</td>

					</tr>
					%end
				</table>
            </tbody>
        </table>
    </div>
</div>
