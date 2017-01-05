%rebase('osnova.tpl')

<body bgcolor = "#dcedc8">
<h2 class="center"> Račun </h2>


<form>
    <div class="row">

            <div class="input-field">
                <input id="ime" type="text" class="validate">
                <label for="ime">Ime</label>
            </div>

            <div class="input-field">
                <input id="priimek" type="text" class="validate">
                <label for="priimek">Priimek</label>
            </div>

            <div class="input-field">
                <input id="datum" type="text" class="validate">
                <label for="datum">Datum</label>
            </div>

			<div class="input-field col s12">
                <select multiple>
				<option value="" disabled selected>Storitve</option>
				%for storitev in kozmeticne_storitve:
					<option value = "{{storitev['id']}}">{{storitev['storitev']}}</option>
				%end
				</select>
			</div>
			
			
			<div class="input-field col s12"> 
                <select multiple>
				<option value="" disabled selected>Izdelki</option>
				%for izdelek in kozmeticni_izdelki:
					<option value = "{{izdelek['id']}}">{{izdelek['izdelek']}}</option>
				%end
				</select>
			</div>
			
			
			
			
			
		<div class="input-field col s12">
            <input type="submit" value="Izpiši" class="btn waves-effect waves-light" />
        </div>
  
        

        </div>
</form>


</body>