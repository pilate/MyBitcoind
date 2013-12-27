%rebase base balance=balance, message=message

<h1>Last 50 Transactions</h1>

<table class="sortable">
    <thead>
        <tr>
            <th data-sort="int" id="sortme">Time</th>
            <th data-sort="string">ID</th>
            <th>Inputs</th>
            <th>Outputs</th>
        </tr>
    </thead>
    <tbody>
% for transaction in recent:
        <tr>
            <td data-sort-value="{{ transaction["rawtime"] }}">{{ transaction["time"] }}</td>
            <td>{{ transaction["txid"] }}</td>
            <td>
                % for in_tx in transaction["inputs"]:
                    % for address in in_tx["scriptPubKey"]["addresses"]:
                        % if address in addresses:
                            <span style="color:#43AC6A;">{{ address }}</span>
                        % else:
                            {{ address }} 
                        % end
                        
                    % end
                    ({{ "{0:.8f}".format(in_tx["value"]) }})<br>
                % end
            </td>
            <td>
                % for out_tx in transaction["outputs"]:
                    % for address in out_tx["scriptPubKey"]["addresses"]:
                        % if address in addresses:
                            <span style="color:#43AC6A;">{{ address }} </span>
                        % else:
                            {{ address }} 
                        % end
                    % end
                ({{ "{0:.8f}".format(out_tx["value"]) }})<br>
                % end
            </td>
        </tr>
% end        
    </tbody>
</table>
