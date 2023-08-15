const { parentPort } = require('worker_threads');

function readJob(arr, index) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (i % 2 === 0) {
      count++;
    } else {
      count--;
    }
  }
}

parentPort.on('message', ({ arr, index }) => {
  // console.log(`array ${index} init`);
  for (let i = 0; i < arr.length; i++) {
    arr[i] = i;
  }
  readJob(arr, index);
  parentPort.postMessage('done');
});

