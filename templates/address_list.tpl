%rebase base balance=balance

<h1>Account Addresses</h1>

<table class="sortable">
    <thead>
        <tr>
            <th data-sort="string" data-sort-default="desc">Address</th>
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
