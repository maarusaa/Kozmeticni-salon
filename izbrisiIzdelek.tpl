%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov">Izbriši izdelek</p>

<form action = '/izdelki/izbrisiIzdelek/' method = 'POST'>
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
            <button type="submit" class="btn waves-effect waves-light zavihek" />IZBRIŠI</button>
        </div>
</div>
</form>
