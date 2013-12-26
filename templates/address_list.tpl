%rebase base balance=balance, message=message

<h1>Account Addresses</h1>

<table class="sortable">
    <thead>
        <tr>
            <th data-sort="string" data-sort-default="desc">Address ({{ len(addresses) }})</th>
        </tr>
    </thead>
    <tbody>
% for address in addresses:
    <tr>
        <td>{{ address }}</td>
    </tr>
% end        
    </tbody>
</table>
