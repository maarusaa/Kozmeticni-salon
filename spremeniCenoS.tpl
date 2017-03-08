%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Spremeni ceno</p>

<form action = '/storitve/spremeniCenoS/' method = 'POST'>
	<div class="row">
	
            <div class="input-field col s12"> 
				<i class="material-icons prefix">shopping_cart</i>
                <select name="storitev" required>
				<option value="" disabled selected>Storitev</option>
				%for storitev in kozmeticne_storitve:
					<option value = "{{storitev['id']}}">{{storitev['storitev']}}</option>
				%end
				</select>
			</div>
			
			<div class="input-field col s12">
				<i class="material-icons prefix">account_circle</i>
                <input name="cena" type="text" required class="validate">
                <label for="cena">Cena</label>
            </div>
					
		
		<div class="input-field col s12">
            <button type="submit" class="btn waves-effect waves-light zavihek" />SPREMENI</button>
        </div>
</div>
</form>