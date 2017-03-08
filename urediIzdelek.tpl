%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Uredi izdelek</p>

<form action = '/izdelki/urediIzdelek/' method = 'POST'>
	<div class="row">
	
            <div class="input-field col s12"> 
				<i class="material-icons prefix">shopping_cart</i>
                <select name="ime" required>
				<option value="" disabled selected>Izdelek</option>
				%for izdelek in kozmeticni_izdelki:
					<option value = "{{izdelek['id']}}">{{izdelek['izdelek']}}</option>
				%end
				</select>
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
            <button type="submit" class="btn waves-effect waves-light zavihek" />UREDI</button>
        </div>
</div>
</form>
