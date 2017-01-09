%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">
<div class="row">
    <div class="col s12">
        <table class="highlight">
            <thead>
                <tr>
                    <th class="podnaslov">Storitve</th>
                </tr>
            </thead>
            <tbody class="okvir_tabela">
                <table>
					<tr class="izpis">
					<th>Storitev</th>
					<th>Čas (min)</th>
					<th>Cena (€)</th>


					</tr>

					%for storitev in kozmeticne_storitve:
					<tr>
					<td>{{storitev['storitev']}}</td>
					<td>{{storitev['cas']}}</td>
					<td>{{storitev['cena']}}</td>

					</tr>
					%end
				</table>
            </tbody>
        </table>
    </div>
</div>

