package main

/*
 *	借鉴: https://www.imooc.com/article/20582#0-tsina-1-29356-397232819ff9a47a7b7e80a40613cfe1
 *
 */
import "fmt"

type Node struct{
	Data interface{}
	Next *Node
}

type SingleChain struct{
	Head *Node
	Size int
}

func (s *SingleChain) Add(data *Node){
	if s.Size == 0{
		s.Head = data
		s.Size++
		return
	}

	cursor := s.Head
	for cursor.Next != nil{
		cursor = cursor.Next
	}
	cursor.Next = data
	s.Size++
}

func (s *SingleChain) Show(){
	cursor := s.Head
	for cursor !=nil{
		fmt.Println(cursor.Data)
		cursor = cursor.Next
	}
}

func main(){
	s := &SingleChain{nil,0}
	s.Add(&Node{1, nil})
	s.Add(&Node{2, nil})
	s.Add(&Node{3, nil})

	s.Show()
}