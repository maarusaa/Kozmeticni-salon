%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Dodaj storitev</p>

<form action = '/storitve/dodajStoritev/' method = 'POST'>
	<div class="row">
	
            <div class="input-field col s12">
				<i class="material-icons prefix">shopping_cart</i>
                <input name="ime" type="text" required class="validate">
                <label for="ime">Ime</label>
            </div>
			
			<div class="input-field col s12">
				<i class="material-icons prefix">account_circle</i>
                <input name="cena" type="text" required class="validate">
                <label for="cena">Cena</label>
            </div>
			
			<div class="input-field col s12">
				<i class="material-icons prefix">store</i>
                <input name="cas" type="text" required class="validate">
                <label for="cas">Čas izvajanja</label>
            </div>
					
			<div class="input-field col s12"> 
				<i class="material-icons prefix">shopping_cart</i>
                <select name="izvajalec" required>
				<option value="" disabled selected>Izvajalec</option>
				%for izvajalec in izvajalci:
					<option value = "{{izvajalec['id']}}">{{izvajalec['ime']}} {{izvajalec['priimek']}}</option>
				%end
				</select>
			</div>
			
		
		<div class="input-field col s12">
            <button type="submit" class="btn waves-effect waves-light zavihek" />SHRANI</button>
        </div>
</div>
</form>