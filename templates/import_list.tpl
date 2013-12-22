%rebase base balance=balance, message=message

<h1>Import PrivKey List</h1>

<form method="POST">
    <div class="row">
        <div class="large-12 columns">
            <textarea class="import-list" name="privkeys">{{ privkeys }}</textarea>
        </div>
        <div class="large-12 columns">
            <input type="submit" class="button" value="Submit">
        </div>
    </div>
</form>