package main

import (
	"io"
	"net/http"
	"os"

	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
)

func main() {
	e := echo.New()
	e.Use(middleware.CORS())

	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})
	e.GET("reverse", getReverse)
	e.POST("file", upload)

	e.Logger.Fatal(e.Start(":5050"))

}

func getReverse(c echo.Context) error {
	// Get team and member from the query string
	line := c.QueryParam("line")
	if line == "" {
		line = "no input, sorry"
	} else {
		line = reverse(line)
	}

	return c.String(http.StatusOK, line)
}

func reverse(s string) string {
	rs := []rune(s)
	for i, j := 0, len(rs)-1; i < j; i, j = i+1, j-1 {
		rs[i], rs[j] = rs[j], rs[i]
	}
	return string(rs)
}

func upload(c echo.Context) error {

	// Source
	file, err := c.FormFile("file")
	if err != nil {
		return err
	}
	src, err := file.Open()
	if err != nil {
		return err
	}
	defer src.Close()

	// Destination
	dst, err := os.Create(file.Filename)
	if err != nil {
		return err
	}
	defer dst.Close()

	// Copy
	if _, err = io.Copy(dst, src); err != nil {
		return err
	}

	return nil
}
