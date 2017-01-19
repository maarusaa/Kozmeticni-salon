%rebase('osnova.tpl')

<p class = "podnaslov">Izpis računa</p>

<body bgcolor = "#f3e5f5">
<div class="row">
    <div class="col s12">
		<div >
			%for os in oseba:
			<tr>
				<td>{{os['ime']}} {{os['priimek']}} </td>
			</tr>
			%end
			
			<li class="right-align">
			%for dat in datum:
			<tr>
				<td>{{dat['datum']}}</td>
			</tr>
			%end
			</li>
			
		</div>
			

	
			
        <table class="highlight">
            <tbody class="okvir_tabela">
                <table>
					<tr class="izpis">

					</tr>

					%for storitev in storitve:
					<tr>
					<td>{{storitev['storitev']}}</td>
					<td>{{storitev['cena']}}</td>


					</tr>
					%end
					
					
					%for izdelek in izdelki:
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
