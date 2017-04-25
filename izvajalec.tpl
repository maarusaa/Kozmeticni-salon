%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">
<h2 class="podnaslov"> Rezervacija</h2>

<form action = '/narocanje/{{leto}}/{{mesec}}/{{dan}}/{{ura}}/{{id_zaposlenega}}/' method = 'POST'>
    <div class="row">
		 <div class="row">

            <div class="input-field col s6">
				<i class="material-icons prefix">account_circle</i>
                <input name="ime" type="text" required class="validate">
                <label for="ime">Ime</label>
            </div>

            <div class="input-field col s6">
				<i class="material-icons prefix">account_circle</i>
                <input name="priimek" type="text" required class="validate">
                <label for="priimek">Priimek</label>
            </div>
		</div> 
	</div>



<div class="input-field col s12"> 
				<i class="material-icons prefix">shopping_cart</i>
                <select name="storitev" required>
				<option value="" disabled selected>Storitev</option>
				%for storitev in storitve:
					<option>{{storitev['storitev']}}</option>
				%end
				</select>
			</div>



		<div class="input-field col s12">
            <button type="submit" class="btn waves-effect waves-light zavihek" />Rezerviraj</button>
        </div>
		
		
</form>