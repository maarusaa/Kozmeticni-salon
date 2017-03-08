%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Spremeni izvajalca</p>

<form action = '/storitve/spremeniIzvajalca/' method = 'POST'>
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
                <select name="izvajalec" required>
				<option value="" disabled selected>Izvajalec</option>
				%for izvajalec in izvajalci:
					<option value = "{{izvajalec['id']}}">{{izvajalec['ime']}}  {{izvajalec['priimek']}}</option>
				%end
				</select>
			</div>
			
		
		<div class="input-field col s12">
            <button type="submit" class="btn waves-effect waves-light zavihek" />SPREMENI</button>
        </div>
</div>
</form>
