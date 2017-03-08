%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Storitve</p>

<div>
	<ul>
		<li><a href="/storitve/dodajStoritev/">Dodaj novo storitev</a></li>
		<li><a href="/storitve/spremeniCenoS/">Spremeni ceno</a></li>
		<li><a href="/storitve/spremeniIzvajalca/">Spremeni izvajalca</a></li>
		<li><a href="/storitve/odstraniStoritev/">Odstrani storitev</a></li>
	</ul>
</div>	

<div class="row">
    <div class="col s12">
        <table class="highlight">
            <tbody class="okvir_tabela">
                <table>
					<tr class="izpis">
					<th>Storitev</th>
					<th>Čas (min)</th>
					<th>Cena</th>


					</tr>

					%for storitev in kozmeticne_storitve:
					<tr>
					<td>{{storitev['storitev']}}</td>
					<td>{{storitev['cas']}}</td>
					<td>{{storitev['cena']}} &#8364</td>

					</tr>
					%end
				</table>
            </tbody>
        </table>
    </div>
</div>

