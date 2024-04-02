  function soloLetras(event) {
    var charCode = event.keyCode;
    if (charCode >= 65 && charCode <= 90 || charCode >= 97 && charCode <= 122 || charCode == 32) {
      return true;
    } else {
      event.preventDefault();
      return false;
    }
  }
  
  function soloNumeros(event) {
    var charCode = event.keyCode;
    if (charCode >= 48 && charCode <= 57) {
      return true;
    } else {
      event.preventDefault();
      return false;
    }
  }
