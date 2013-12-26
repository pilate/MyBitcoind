%rebase base balance=balance, message=message

<h1>Summary</h1>

<table>
    <tbody>
        <tr>
            <td>
                Addresses
            </td>
            <td>
                {{ address_count }}
            </td>
        </tr>
        <tr>
            <td>
                Total Received
            </td>
            <td>
                {{ total_received }}฿
            </td>
        </tr>
        <tr>
            <td>
                Unspent Outputs
            </td>
            <td>
                {{ unspent_outputs }}
            </td>
        </tr>
        <tr>
            <td>
                Unspent Balance
            </td>
            <td>
                {{ balance }}฿
            </td>
        </tr>
    </tbody>
</table>