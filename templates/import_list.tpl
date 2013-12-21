%rebase base balance=balance, message=message

<h1>Import PrivKey List</h1>

% if message:
<div class="row">
    <div class="large-4 medium-4 columns">
        <div data-alert class="alert-box info radius">
            {{ message }}
            <a href="#" class="close">&times;</a>
        </div>
    </div>
</div>
% end

<form method="POST">
    <div class="row">
        <div class="large-12 columns">
            <textarea class="import-list" name="privkeys"></textarea>
        </div>
        <div class="large-12 columns">
            <input type="submit" class="button" value="Submit">
        </div>
    </div>
</form>