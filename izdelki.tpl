%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">
<div class="row">
    <div class="col s12">
        <table class="highlight">
            <thead>
                <tr class="podnaslov">
                    <th>Izdelki</th>
                </tr>
            </thead>
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

