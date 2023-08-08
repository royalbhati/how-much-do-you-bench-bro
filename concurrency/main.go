package main

import (
	"fmt"
	"os"
	"runtime"
	"strconv"
	"sync"
	"time"
)

func main(){
	coresToBeUsed := runtime.NumCPU()
	if len(os.Args) > 1 {
		coresToBeUsed, _ = strconv.Atoi(os.Args[1])
	}
	runtime.GOMAXPROCS(coresToBeUsed)
	numCores := runtime.GOMAXPROCS(0)
	fmt.Printf("Current number of CPU cores: %d\n", numCores)
   
    arrayLen:=10
    arrayChildrenLen:=1e8
    runWithChannels(arrayLen,int(arrayChildrenLen)) 
}



func runWithChannels(arrayLen int,arrayChildrenLen int) {
	start := time.Now()
	arr := make([][]int, arrayLen)
    
    notify:=make(chan bool, arrayLen)

	for i, _ := range arr {
		arr[i] = make([]int, arrayChildrenLen)
		go writeJobChannel(arr, i, &notify)
	}
    
    for i:=0;i<arrayLen;i++{
        <-notify
    }
	end := time.Now()
	duration := end.Sub(start)	
	fmt.Printf("Execution time: %s\n", duration)
}



func runWithWaitGroup(arrayLen int) {
	start := time.Now()
	arr := make([][]int, arrayLen)
	var wg sync.WaitGroup
	for i, _ := range arr {
		wg.Add(1)
		arr[i] = make([]int, 1e9)
		go writeJob(arr, i, &wg)
	}
	wg.Wait()
	end := time.Now()
	duration := end.Sub(start)
	
	fmt.Printf("Execution time: %s\n", duration)
}

func writeJob(arr [][]int, index int, wg *sync.WaitGroup) {
	fmt.Println("array ", index, " init")
	for i := 0; i < len(arr[index]); i++ {
		arr[index][i] = i
	}
	readJob(arr, index)
	fmt.Println("array ", index, " done")
	wg.Done()
}


func writeJobChannel(arr [][]int, index int, notify *chan bool) {
	// fmt.Println("array ", index, " init")
	for i := 0; i < len(arr[index]); i++ {
		arr[index][i] = i
	}
	readJob(arr, index)
    // fmt.Println("array ", index, " done")
    *notify<-true
}
func readJob(arr [][]int, index int) {
	count := 0
	for i := 0; i < len(arr[index]); i++ {
		if i%2 == 0 {
			count++
		} else {
			count--
		}
	}
}
