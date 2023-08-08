const { Worker } = require('worker_threads');

function main() {
  const numCores = require('os').cpus().length;
  console.log(`Current number of CPU cores: ${numCores}`);

  const arrayLen = 10;
  const arrayChildrenLen = 1e8;
  const coresToBeUsed = 8; // Specify the number of CPUs you want to use
  runWithChannels(arrayLen, arrayChildrenLen, coresToBeUsed);
}

function runWithChannels(arrayLen, arrayChildrenLen, coresToBeUsed) {
  const start = performance.now();
  const arr = new Array(arrayLen);

  const jobsPerCore = Math.ceil(arrayLen / coresToBeUsed);
  let remainingWorkers = coresToBeUsed;

  function onWorkerDone() {
    remainingWorkers--;
    if (remainingWorkers === 0) {
      const end = performance.now();
      const duration = end - start;
      console.log(`Execution time: ${duration}ms`);
    }
  }

  function createWorker(workerIndex) {
    const startJob = workerIndex * jobsPerCore;
    const endJob = Math.min(startJob + jobsPerCore, arrayLen);
    
    for (let i = startJob; i < endJob; i++) {
      const worker = new Worker('./worker.js');
      worker.on('message', (message) => {
        if (message === 'done') { 
          onWorkerDone();
        }
      });

      worker.postMessage({ arr: arr[i], index: i });
    }
  }

  for (let i = 0; i < arr.length; i++) {
    arr[i] = new Array(arrayChildrenLen);
  }

  for (let i = 0; i < coresToBeUsed; i++) {
    createWorker(i);
  }
}

main();

