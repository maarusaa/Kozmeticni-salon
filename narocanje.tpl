%rebase('osnova.tpl')

<body bgcolor = "#f3e5f5">

<p class = "podnaslov"> Tu je spisek terminov za {{dan}}. {{mesec}}. {{leto}}</p>

<ul>
%for ura, zaposleni in termini.items():
<li> ob {{ura}} so prosti:
%for zaposlen in zaposleni:
<a href = "/narocanje/{{leto}}/{{mesec}}/{{dan}}/{{zaposlen['id']}}/">{{zaposlen['ime']}} {{zaposlen['priimek']}}</a>
%end
</li>
%end
</ul>


