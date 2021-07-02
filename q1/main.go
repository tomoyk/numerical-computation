package main

// import "math/big"
/*import (
	"fmt"
	"time"
)*/

func main() {
	// start := time.Now()
	var x float32 = 1.0
	for 1+x > 1 {
		// println(x)
		x = x / 2
	}
	println("float32,", x * 2)
	// 処理
	// end := time.Now()
	// fmt.Printf("%f秒\n", (end.Sub(start)).Seconds())

	// println("Start !")
	var y float64 = 1.0
	for 1+y > 1 {
		// println(x)
		y = y / 2
	}
	println("float64,", y * 2)
}
