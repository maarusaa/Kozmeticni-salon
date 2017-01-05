%rebase('osnova.tpl')

<div class="row">
    <div class="col s4">
        <table class="highlight">
            <thead>
                <tr>
                    <th>Storitve</th>
                </tr>
            </thead>
            <tbody>
                %for storitev in kozmeticne_storitve:
                <tr>
                    <td></storitev/{{storitev['id']}}/kozmeticni_salon">{{storitev['storitev']}} {{storitev['cena']}} {{storitev['cas']}}</td>
                </tr>
                %end
            </tbody>
        </table>
    </div>
</div>