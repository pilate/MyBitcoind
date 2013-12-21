%rebase base balance=balance

<h1>Unspent Outputs</h1>

<table class="sortable">
    <thead>
        <tr>
            <th data-sort="string">Address</th>
            <th data-sort="string">Transaction ID</th>
            <th data-sort="float" data-sort-default="desc">Amount</th>
        </tr>
    </thead>
    <tbody>
% for output in unspent:
    <tr>
        <td>{{ output["address"] }}</td>
        <td>{{ output["txid"] }}</td>
        <td>{{ output["amount"] }}</td>
    </tr>
% end        
    </tbody>
</table>
