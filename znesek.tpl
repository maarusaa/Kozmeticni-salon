%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">
<div class="row">
    <div class="col s12">
        <table class="highlight">
            <tbody class="okvir_tabela">
                <table>
					<tr class="izpis">
					<th>Storitev</th>
	


					</tr>

					%for storitev in storitve:
					<tr>
					<td>{{storitev['storitev']}}</td>


					</tr>
					%end
					
					

				
						
				</table>
            </tbody>
        </table>
    </div>
</div>
