function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue, indcol, mostrar;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

/*  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }  
*/
  for (i = 1; i < tr.length; i++) {
	mostrar=0;
    for(indcol = 0; indcol < 2; indcol++)/*Busco en las dos primeras columnas*/
	{
		td = tr[i].getElementsByTagName("td")[indcol];
		if (td) {
		  txtValue = td.textContent || td.innerText;
		  if (txtValue.toUpperCase().indexOf(filter) > -1) {
			mostrar = 1;
		  }
		}
	}
	if (mostrar == 1){
		tr[i].style.display = "";
	} else{
		tr[i].style.display = "none";
	}
  }
}
