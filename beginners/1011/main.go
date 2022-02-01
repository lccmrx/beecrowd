package main

import (
	"fmt"
	"math"
)

const (
	PI = 3.14159
)

func main() {
	var radius float64
	fmt.Scanln(&radius)

	result := (4.0 / 3.0) * PI * (math.Pow(radius, 3))

	fmt.Printf("VOLUME = %.3f\n", result)
	return
}
