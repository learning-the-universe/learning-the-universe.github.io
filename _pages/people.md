---
layout: page
permalink: /people/
title: people
description: Members of our collaboration
nav: true
nav_order: 2
---

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search..">

<table class="table table-bordered table-hover table-condensed" id = "myTable">
<thead><tr><th title="Field #1">Last</th>
<th title="Field #2">First</th>
<th title="Field #3">Institution</th>
<th title="Field #4">Working Group</th>
<th title="Field #5">Website</th>
</tr></thead>
<tbody>
    {% for row in site.data.members %}
        <tr>
            <td>{{ row.Last }}</td>
            <td>{{ row.First }}</td>
            <td>{{ row.Institution }}</td>
            <td>{{ row.Working_Group }}</td>
            {% if row.Website %}
                <td><a href="{{ row.Website }}">{{ row.Website }}</a></td>
            {% else %}
                <td></td>
            {% endif %}
        </tr>
    {% endfor %}
</tbody></table>

<script>
(function () {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("myTable");
  switching = true;
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[0];
      y = rows[i + 1].getElementsByTagName("TD")[0];
      //check if the two rows should switch place:
      if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
        //if so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
})();
</script>

<script>
function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
</script>
