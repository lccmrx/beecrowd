package main

import "fmt"

func main() {
	fmt.Scanln(nil)

	var salary, sales float64

	fmt.Scanln(&salary)
	fmt.Scanln(&sales)

	fmt.Printf("TOTAL = R$ %.2f\n", salary+(sales*0.15))
	return
}
