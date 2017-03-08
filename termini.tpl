<!DOCTYPE html>
<html>

<head>
	
	<script type="text/javascript">
		
		// Author: AlÃª Monteiro
		// Created: 2013-03-06
		// E-mail: lu.ale.monteiro@gmail.com
				
		// P.S. I'm from Brazil, so the names of the weeks and months are in Portuguese.
		
		var Calendar = function(divId) {
			
			//Store div id
			this.divId = divId;
			
			// Days of week, starting on Sunday
			this.DaysOfWeek = [
				'Nedelja',
				'Ponedeljek',
				'Torek',
				'Sreda',
				'Četrtek',
				'Petek',
				'Sobota'
			];
			
			// Months, stating on January
			this.Months = ['Januar', 'Februar', 'Marc', 'April', 'Maj', 'Junij', 'Julij', 'Avgust', 'September', 'Oktober', 'November', 'December' ];
			
			// Set the current month, year
			var d = new Date();
			
			this.CurrentMonth = d.getMonth();
			this.CurrentYear = d.getFullYear();
			
		};
		
		// Goes to next month
		Calendar.prototype.nextMonth = function() {
			if ( this.CurrentMonth == 11 ) {
				this.CurrentMonth = 0;
				this.CurrentYear = this.CurrentYear + 1;
			}
			else {
				this.CurrentMonth = this.CurrentMonth + 1;
			}
			this.showCurrent();
		};
		
		// Goes to previous month
		Calendar.prototype.previousMonth = function() {
			if ( this.CurrentMonth == 0 ) {
				this.CurrentMonth = 11;
				this.CurrentYear = this.CurrentYear - 1;
			}
			else {
				this.CurrentMonth = this.CurrentMonth - 1;
			}
			this.showCurrent();
		};
		
		// Show current month
		Calendar.prototype.showCurrent = function() {
			this.showMonth(this.CurrentYear, this.CurrentMonth);
		};
		
		// Show month (year, month)
		Calendar.prototype.showMonth = function(y, m) {
			
			var d = new Date()
				// First day of the week in the selected month
				, firstDayOfMonth = new Date(y, m, 1).getDay()
				// Last day of the selected month
				, lastDateOfMonth =  new Date(y, m+1, 0).getDate()
				// Last day of the previous month
				, lastDayOfLastMonth = m == 0 ? new Date(y-1, 11, 0).getDate() : new Date(y, m, 0).getDate();
				
			
			var html = '<table>';
			
			// Write selected month and year
			html += '<tr><td colspan="7">' + this.Months[m] + ' - ' + y + '</td></tr>';
			
			// Write the header of the days of the week
			html += '<tr>';
			for(var i=0; i < this.DaysOfWeek.length;i++) {
				html += '<td>' + this.DaysOfWeek[i] + '</td>';
			}
			html += '</tr>';
			
			// Write the days
			var i=1;
			do {
				
				var dow = new Date(y, m, i).getDay();
				
				// If Sunday, start new row
				if ( dow == 0 ) {
					html += '<tr>';
				}
				// If not Sunday but first day of the month
				// it will write the last days from the previous month
				else if ( i == 1 ) {
					html += '<tr>';
					var k = lastDayOfLastMonth - firstDayOfMonth+1;
					for(var j=0; j < firstDayOfMonth; j++) {
						html += '<td class="not-current">' + k + '</td>';
						k++;
					}
				}
				
				// Write the current day in the loop
				html += '<td><a href="/narocanje/' + y + '/' + (m + 1) + '/' + i + '/">' +  i + '</a></td>';
				
				// If Saturday, closes the row
				if ( dow == 6 ) {
					html += '</tr>';
				}
				// If not Saturday, but last day of the selected month
				// it will write the next few days from the next month
				else if ( i == lastDateOfMonth ) {
					var k=1;
					for(dow; dow < 6; dow++) {
						html += '<td class="not-current">' + k + '</td>';
						k++;
					}
				}
				
				i++;
			}while(i <= lastDateOfMonth);
			
			// Closes table
			html += '</table>';
			
			// Write HTML to the div
			document.getElementById(this.divId).innerHTML = html;
		};
		
		// On Load of the window
		window.onload = function() {
			
			// Start calendar
			var c = new Calendar("divCalendar");			
			c.showCurrent();
			
			// Bind next and previous button clicks
			getId('btnNext').onclick = function() {
				c.nextMonth();
			};
			getId('btnPrev').onclick = function() {
				c.previousMonth();
			};
		}
		
		// Get element by id
		function getId(id) {
			return document.getElementById(id);
		}
	
	</script>

	<style type="text/css">
		
		td.not-current {
			color: #777;
		}
		

		
		
		
	</style>
	
	
</head>

<body>

	%rebase('osnova.tpl')

	<body bgcolor = "#f3e5f5">
	<p class = "podnaslov">Termini</p>
	
	<div id="divCalendar">
			
	</div>
	
	<button id="btnPrev" class = "zavihek" type="button">Prejšnji</button>
	<button id="btnNext" class = "zavihek" type="button">Naslednji</button>
	
	
</body>

</html>