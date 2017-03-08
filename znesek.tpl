%rebase('osnova.tpl')
%rebase('osnova.tpl')

<p class = "podnaslov">Izpis računa</p>

<body bgcolor = "#f3e5f5">
<div class="row">
    <div class="col s12">
		<div >
			
			<div class = "ime">
			%for os in oseba:
			<tr>
				<td>{{os['ime']}} {{os['priimek']}} </td>
			</tr>
			%end
			</div>
			
			<div class="right-align">
			%for dat in datum:
			<tr>
				<td>{{dat['datum']}}</td>
			</tr>
			%end
			</div>
			
		</div>
			

	
			
        <table class="highlight">
            <tbody class="okvir_tabela">
                <table>
					<tr class="izpis">

					</tr>

					%for storitev in storitve:
					<tr>
					<td>{{storitev['storitev']}}</td>
					<td>{{storitev['cena']}} &#8364</td>


					</tr>
					%end
					
					
					%for izdelek in izdelki:
					<tr>
					<td>{{izdelek['izdelek']}}</td>
					<td>{{izdelek['cena']}} &#8364</td> 


					</tr>
					%end
					
					

				
						
				</table>
            </tbody>
        </table>

		<div class = "znesek">
		%for znesek in znesek:
		<tr>
			<p>ZNESEK: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
			<td>{{znesek['znesek']}}</td> &#8364 </p>
		</tr>
		%end
		</div>
		
	
    </div>
</div>
