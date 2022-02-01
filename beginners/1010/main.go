package main

import "fmt"

type product struct {
	id    int64
	qtd   int64
	price float64
}

func main() {
	var finalPrice float64
	var p product

	for range [...]int64{0, 1} {
		fmt.Scanf("%d %d %f", &p.id, &p.qtd, &p.price)
		finalPrice += float64(p.qtd) * p.price
	}

	fmt.Printf("VALOR A PAGAR: R$ %.2f\n", finalPrice)
}
