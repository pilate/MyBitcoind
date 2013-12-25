%rebase base balance=balance, message=message

<h1>Last 50 Transactions</h1>

<table class="sortable">
    <thead>
        <tr>
            <th data-sort="float" id="sortme">Time</th>
            <th data-sort="string">Address</th>
            <th data-sort="string">ID</th>
            <th data-sort="float">Amount</th>
        </tr>
    </thead>
    <tbody>
% for transaction in recent:
        <tr>
            <td data-sort-value="{{ transaction["realtimestamp"] }}">{{ transaction["realtime"] }}</td>
            <td>{{ transaction["address"] }}</td>
            <td>{{ transaction["txid"] }}</td>
            <td>
                % if transaction["category"] == "send":
                    <span style="color:red;">
                % else:
                    <span style="color:green;">
                % end
                    {{ transaction["amount"] }}
                </span>
            </td>
        </tr>
% end        
    </tbody>
</table>
