let N = 100;
let primes = [];

function setup() {
  for (let i = 2; i < N; i++) {
    for (let j = 2; j <= i / 2 + 1; j++) {
      if (i % j == 0) {
        break;
      } else {
        primes.push(i);
        console.log(i);
      }
    }
  }
}

let Prime = class {
  constructor(n, p) {
    this.index = n;
    this.value = p;
  }
}
