function validareForm() {
var x = document.forms["Form1"]["fname"].value;
if (x == null || x == "") { alert("Nu este completat numele"); return false; }
else { alert("Forma a fost validata"); return true; } }
