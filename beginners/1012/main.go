package main

import (
	"fmt"
)

type shape interface {
	area() float64
	getName() string
}

type triangle struct {
	Name         string
	base, height float64
}

func (s *triangle) area() float64 {
	return s.base * s.height / 2.0
}

func (s *triangle) getName() string {
	return s.Name
}

type circle struct {
	Name   string
	radius float64
}

func (s *circle) area() float64 {
	return s.radius * s.radius * 3.14159
}

func (s *circle) getName() string {
	return s.Name
}

type trapezoid struct {
	Name                 string
	base1, base2, height float64
}

func (s *trapezoid) area() float64 {
	return ((s.base1 + s.base2) * s.height) / 2
}

func (s *trapezoid) getName() string {
	return s.Name
}

type square struct {
	Name string
	side float64
}

func (s *square) area() float64 {
	return s.side * s.side
}

func (s *square) getName() string {
	return s.Name
}

type rectangle struct {
	Name          string
	width, height float64
}

func (s *rectangle) area() float64 {
	return s.width * s.height
}

func (s *rectangle) getName() string {
	return s.Name
}

func print(shapes []shape) {
	for _, s := range shapes {
		fmt.Printf("%s: %.3f\n", s.getName(), s.area())
	}
}

func main() {

	var a, b, c float64
	fmt.Scanf("%f %f %f", &a, &b, &c)

	shapes := []shape{
		&triangle{Name: "TRIANGULO", base: a, height: c},
		&circle{Name: "CIRCULO", radius: c},
		&trapezoid{Name: "TRAPEZIO", base1: a, base2: b, height: c},
		&square{Name: "QUADRADO", side: b},
		&rectangle{Name: "RETANGULO", width: a, height: b},
	}

	print(shapes)
}
