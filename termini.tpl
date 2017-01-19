%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">
<h2 class="podnaslov"> Termini </h2>


<form action="#" method="post">
    <div class="row">
		 <div class="row">
		
		<div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">date_range</i>
                <select name="mesec">
				<option value="" disabled selected>Mesec</option>
				
				%for i, el in enumerate(meseci):
					<option value = "{{i+1}}">{{el}}</option>
				%end
				</select>
			</div>
		</div>
		
		<div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">date_range</i>
                <select name="dan">
				<option value="" disabled selected>Dan</option>
				
				%for i in range(1,32):
					<option value = "{{i+1}}">{{i}}</option>
				%end
				</select>
			</div>
		</div>
		
		  </div>
			
	
		<div class="row">
			<div class="input-field col s4">
				<i class="material-icons prefix">date_range</i>
                <select name="ura">
				<option value="" disabled selected>Ura</option>
				
				%for i in range(8,18):
					<option value = "{{i+1}}">{{i}}</option>
				%end
				</select>
			 </div>
			
			<div class="input-field col s4">
				<i class="material-icons prefix">shopping_cart</i>
                <select name="Storitev">
				<option value="" disabled selected>Storitev</option>
				
				%for storitev in kozmeticne_storitve:
						<option value = "{{storitev['id']}}">{{storitev['storitev']}}</option>
				%end
				</select>
			 </div>
				
			<div class="input-field col s4">
				<i class="material-icons prefix">account_circle</i>
                <select name="izvajalec">
				<option value="" disabled selected>Izvajalec</option>
				
				%for izvajalec in zaposleni: 
					<option value = "{{izvajalec['id']}}">{{izvajalec['ime']}} {{izvajalec['priimek']}}</option>
				%end
				</select>
			 </div>
				
				
			<div class="input-field col s12">
				<button type="submit" class="btn waves-effect waves-light zavihek" />Rezerviraj</button>
			</div>
				
				
			</div>
		</div>
		
		
		
	



      
</form>
