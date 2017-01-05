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
                    <td><a href="/izdelek/{{izdelek['id']}}/kozmeticni_salon">{{izdelek['cena']}}, {{izdelek['izdelek']}}. izdelek</a></td>
                </tr>
                %end
            </tbody>
        </table>
    </div>
</div>