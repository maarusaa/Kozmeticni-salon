<!DOCTYPE html>
<html>
<head>
	<title>Kozmetični salon</title>
    <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<script src="http://cdnjs.cloudflare.com/ajax/libs/moment.js/2.5.1/moment.min.js"></script>

	
	<style>
		.zavihek {
			width: 24%;
			background: #9c27b0;
			color: white;
			font-family: "Informal Roman";
		}
		.naslov {
			color: #9c27b0;
			font-family: "Informal Roman";
		}
		.podnaslov {
			color: #9c27b0;
			font-family: "Informal Roman";
			font-size: 250%;
		}
		.izpis {
		color: #ba68c8;
		text-align: center;
		padding: 14px 16px;
		text-decoration: none;

		}
		
		.okvir_tabela{
			display: inline-block;
			position: relative;
			top:100px;
		}
		
		td {
			padding-left: 20px;
			padding-right: 20px;
			padding-top: 20px;
			color:black;
		}	
		
		tr:nth-child(even){background-color: #e1bee7}
		
		table {
			border-collapse:collapse;
			color: black;
		}
		
		
		html, body{
		  margin:0;
		  padding:0;
		  height: 100%;
		}
		#scheduler {
		  border-width: 0;
		  height: 100%;
		}

		
	</style>
	



</head>

<body>
    <div class="container">
        {{!base}}
    </div>

    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"></script>
    <script type="text/javascript">
		$(document).ready(function() {
			$('select').material_select();
		});
		 $(document).ready(function(){
			$('.materialboxed').materialbox();
		});
		    $(document).ready(function(){
			$('.slider').slider({full_width: true});
		});
	</script>
</body>
</html>


