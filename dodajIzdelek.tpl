%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Dodaj izdelek</p>

<form action = '/izdelki/dodajIzdelek/' method = 'POST'>
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
                <input name="zaloga" type="text" required class="validate">
                <label for="zaloga">Zaloga</label>
            </div>
			
		
		<div class="input-field col s12">
            <button type="submit" class="btn waves-effect waves-light zavihek" />SHRANI</button>
        </div>
</div>
</form>

