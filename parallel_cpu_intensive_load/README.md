# BENCHMARKS

*Disclaimer*:  I'm no expert, just someone who enjoys tinkering with languages. That's what you'll discover below. Keep in mind that my methods and techniques are a work in progress as I dive deeper into learning. 



| Array Size      | GO                | Python            | JS                | 
|-----------------|-------------------|-------------------|-------------------|
| 10^4 elements   | 0.00073060525s    | 1.3s              | 0.045016845s      |
| 10^7 elements   | 0.0191138s        | 7s                | 0.367750419s      |
| 10^8 elements   | 1.53060525s       | 88.83060525s      | 20.35016845s      |


## Performance Comparison: Python, Node.js, and Go


### Python: Dealing with Larger Data
In Python, I noticed slowdowns when dealing with bigger data. I tried different approaches to make things faster. I attempted using PyPy for speed, but it didn't really help. Initially, I used simple arrays like in Node.js and Go, but that gave worse performance. I turned to NumPy for improvement, but it wasn't significantly better. In the end, using a shared buffer array made things slightly faster. I'm still learning and experimenting to speed up Python. I also tried profiling the code to find where time is spent.

### Node.js: Utilizing Workers
Switching to Node.js, I found its performance good initially. However, it struggled with larger datasets. I used the --max-old-space-size= flag to manage bigger data. Implementing workers was a bit tricky, but my experience with Node.js helped. Profiling showed that most work happened in the C++ world, thanks to the v8 engine.

### Go: Channels vs. WaitGroups
Go's performance was consistent. I started with WaitGroups but tried using channels based on a suggestion. Channels didn't show much difference in performance compared to WaitGroups.

### TODO
[x] Learn More about profiling 
[x] Cover more languages ( Rust, Zig & Elixir)

