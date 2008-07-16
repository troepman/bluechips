<%inherit file="/base.mako"/>

<h2>Settling Transfers</h2>

% if len(c.settle) == 0:
<p>No need! The books are balanced!</p>
% else:
<p>To balance the books, the following transfers need to be made:</p>

<table>
    <tr>
        <th>From</th>
        <th>To</th>
        <th>Amount</th>
    </tr>
    % for transfer in c.settle:
    <tr>
        <td>${transfer[0].username}</td>
        <td>${transfer[1].username}</td>
        <td>$${h.round_currency(transfer[2])}</td>
    </tr>
    % endfor
</table>
% endif

<h2>Add a new transaction</h2>

<ul>
    <li>${h.link_to('Expenditure for the group', h.url_for(controller='spend', action='index'))}</li>
    <li>${h.link_to('Transfer between two people', h.url_for(controller='transfer', action='index'))}</li>
</ul>