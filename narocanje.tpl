%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov"> Termini za {{dan}}. {{mesec}}. {{leto}}</p>


<div class="row">
    <div class="col s7">
        <table class="highlight">
            <tbody class="okvir_tabela">
                <table>
				<tr class="izpis">
				
				<th>Prosti</th>
				</tr>
				
				<td>
				%for ura, zaposleni in termini.items():
				{{ura}}:00: <br>
				%for zaposlen in zaposleni: 
				<a href = "/narocanje/{{leto}}/{{mesec}}/{{dan}}/{{ura}}/{{zaposlen['id']}}/">{{zaposlen['ime']}} {{zaposlen['priimek']}}</a><br>
				%end
				%end
				</td>
				
				
				</table>
            </tbody>
        </table>
    </div>
</div>





