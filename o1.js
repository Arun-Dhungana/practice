function example() {
  // console.log(y); // ReferenceError: Cannot access 'y' before initialization
  //   const y = 10;
  console.log(y); // 10

  if (true) {
    var y = 20;
    var y = 10;
    console.log(y); // 20 (block-scoped)
  }

  console.log(y); // 10 (outer scope)
}

example();
