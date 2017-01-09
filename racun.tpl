%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">
<h2 class="podnaslov"> Račun </h2>


<form action="#" method="post">
    <div class="row">
		 <div class="row">

            <div class="input-field col s6">
				<i class="material-icons prefix">account_circle</i>
                <input id="ime" type="text" class="validate">
                <label for="ime">Ime</label>
            </div>

            <div class="input-field col s6">
				<i class="material-icons prefix">account_circle</i>
                <input id="priimek" type="text" class="validate">
                <label for="priimek">Priimek</label>
            </div>
		</div> 
		
		
		<div class="row">
            <div class="input-field">
				<i class="material-icons prefix">date_range</i>
                <input id="datum" type="text" class="validate">
                <label for="datum">Datum</label>
            </div>
		</div>
		
		<div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">shopping_cart</i>
                <select name="storitve" multiple>
				<option value="" disabled selected>Storitve</option>
				%for storitev in kozmeticne_storitve:
					<option value = "{{storitev['id']}}">{{storitev['storitev']}}</option>
				%end
				</select>
			</div>
		</div>
		
			
		<div class="row">
			<div class="input-field col s12"> 
				<i class="material-icons prefix">shopping_cart</i>
                <select name="izdelki" multiple>
				<option value="" disabled selected>Izdelki</option>
				%for izdelek in kozmeticni_izdelki:
					<option value = "{{izdelek['id']}}">{{izdelek['izdelek']}}</option>
				%end
				</select>
			</div>
		</div>
			
			
			
			
		<div class="input-field col s12">
            <button type="submit" class="btn waves-effect waves-light zavihek" />Izpiši</button>
        </div>
  
        

        </div>
</form>




</body>