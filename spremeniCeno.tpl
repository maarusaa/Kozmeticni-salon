%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Spremeni ceno</p>

<form action = '/izdelki/spremeniCeno/' method = 'POST'>
	<div class="row">
		
	
            <div class="row">
	
            <div class="input-field col s12"> 
				<i class="material-icons prefix">shopping_cart</i>
                <select name="izdelek" required>
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
            <button type="submit" class="btn waves-effect waves-light zavihek" />SPREMENI</button>
        </div>
</div>
</form>