%rebase('osnova.tpl')

<div class="row">
    <div class="col s4">
        <table class="highlight">
            <thead>
                <tr>
                    <th>Izdelki</th>
                </tr>
            </thead>
            <tbody>
                %for izdelek in kozmeticni_izdelki:
                <tr>
                    <td></izdelek/{{izdelek['id']}}/kozmeticni_salon">{{izdelek['izdelek']}} {{izdelek['cena']}}</td>
                </tr>
                %end
            </tbody>
        </table>
    </div>
</div>