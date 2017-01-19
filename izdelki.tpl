%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">


<div class="row">
<p class = "podnaslov">Izdelki</p>
</div>
			
<div class="row">
    <div class="col s12">
        <table class="highlight">
            
			<div class="container">
				<ul>
					<li><a href="dodajIzdelek.tpl">Dodaj nov izdelek</a></li>
					<li><a href="odstraniIzdelek.tpl">Odstrani izdelek</a></li>
					<li><a href="urediCeno.tpl">Uredi ceno</a></li>
				</ul>
			</div>

			
			
			
			
            <tbody class="okvir_tabela">
                <table>
					<tr class="izpis">
					<th>Izdelek</th>
					<th>Cena (€)</th>

					</tr>

					%for izdelek in kozmeticni_izdelki:
					<tr>
					<td>{{izdelek['izdelek']}}</td>
					<td>{{izdelek['cena']}}</td>

					</tr>
					%end
				</table>
            </tbody>
        </table>
    </div>
</div>
