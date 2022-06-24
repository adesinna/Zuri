function caculator() {
  num1 = Number(window.prompt('Enter number'));
  condition = true;
  while (condition) {
    operation = window.prompt("Choose your operator '+', '-', '*', '/', '%'");

    num2 = Number(window.prompt('Enter another number'));

    num3 = null;
    if (operation == '+') {
      num3 = num1 + num2;


    }

    else if (operation == '-') {
      num3 = num1 - num2;

    }

    else if (operation == '*') {
      num3 = num1 * num2;
    }

    else if (operation == '/') {
      num3 = num1 / num2;

    }

    else if (operation == '%') {
      num3 = num1 % num2;
    }

    else {

      console.log('Enter the correct operation');
      caculator()
    }

    console.log(num3);
    // ask to con

    con_prompt = window.prompt('Do you want to continue? "y" or "n"')

    if (con_prompt == 'y') {
      num1 = num3;

    }
    else {
      condition = false;
    }

  }

  return `Your final answer is ${num3}`;

}

x = caculator()
console.log(x);
