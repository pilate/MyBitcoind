%rebase base balance=balance

<h1>Account Addresses</h1>

<table class="sortable">
    <thead>
        <tr>
            <th data-sort="string">Address</th>
            <th data-sort="float" data-sort-default="desc">Total Received</th>
        </tr>
    </thead>
    <tbody>
% for address_obj in addresses:
    <tr>
        <td>{{ address_obj["address"] }}</td>
        <td>{{ address_obj["amount"] }}</td>
    </tr>
% end        
    </tbody>
</table>
