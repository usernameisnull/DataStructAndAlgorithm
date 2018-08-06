package main

/*
 *	借鉴: https://www.imooc.com/article/20582#0-tsina-1-29356-397232819ff9a47a7b7e80a40613cfe1
 *
 */
import (
	"fmt"
	"strings"
)

type Node struct{
	Data interface{}
	Next *Node   // 这里只能是指针。不是指针的话报错，Golang不支持这种嵌套
}

type SingleChain struct{
	Head *Node   // 这里如果不是引用的话，不好处理，因为Golang不好判断结构体是否为空
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

func (s *SingleChain) IsEmpty() bool{
	return s.Head == nil
}

func (s *SingleChain) String() string{

	if s.IsEmpty(){
		return "no data"
	}else{
		result := make([]string, 0)
		cursor := s.Head
		for cursor != nil{
			result = append(result, fmt.Sprintf("%v",cursor.Data))
			cursor = cursor.Next
		}
		return strings.Join(result, "->")
	}

}

func (s *SingleChain) Reverse(){
	if s.Size<=1{
		return
	}

	cursor := s.Head
	var prev *Node // 这里不要用 var prev = &Node{nil, nil}这种形式，因为这样prev!=nil是成立的
	for cursor != nil{
		current := cursor
		cursor = cursor.Next
		current.Next = prev
		prev = current
	}
	s.Head = prev
}

func main(){
	s := &SingleChain{nil,0}
	s.Add(&Node{1, nil})
	s.Add(&Node{2, nil})
	s.Add(&Node{3, nil})
	fmt.Println(s)
	fmt.Println("After reverse================")
	s.Reverse()
	fmt.Println(s)
}