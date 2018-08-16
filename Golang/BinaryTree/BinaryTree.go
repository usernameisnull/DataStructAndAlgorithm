package main

import (
	"fmt"
	)

type Element string
type BinaryTree struct{
	Data Element
	Left *BinaryTree
	Right *BinaryTree
}

func (b *BinaryTree)insertLeft(e Element){
	node := &BinaryTree{Data:e, Left:nil, Right:nil}
	if b.Left == nil{
		b.Left = node
	}else{
		node.Left = b.Left
		b.Left = node
	}
}

func (b *BinaryTree)insertRight(e Element){
	node := &BinaryTree{Data:e, Left:nil, Right:nil}
	if b.Right == nil{
		b.Right = node
	}else{
		node.Right = b.Right
		b.Right = node
	}
}

func (b *BinaryTree)preorder(){
	fmt.Println(b.Data)
	if b.Left!=nil{
		b.Left.preorder()
	}
	if b.Right!=nil{
		b.Right.preorder()
	}
}

func (b *BinaryTree)postorder(){
	if b.Left!=nil{
		b.Left.postorder()
	}
	if b.Right!=nil{
		b.Right.postorder()
	}
	fmt.Println(b.Data)
}

func (b *BinaryTree)inorder(){
	if b.Left!=nil{
		b.Left.inorder()
	}
	fmt.Println(b.Data)
	if b.Right!=nil{
		b.Right.inorder()
	}
}

func (b *BinaryTree)widthFirst(){
	toVisits := []*BinaryTree{b}
	for len(toVisits)>0{
		current := toVisits[0]
		toVisits = toVisits[1:]
		fmt.Println(current.Data)
		if current.Left !=nil{
			toVisits = append(toVisits, current.Left)
		}
		if current.Right !=nil{
			toVisits = append(toVisits, current.Right)
		}
	}
}

func main(){
	//                  a
	//                 /  \
	//                b    c
	//               /\    /\
	//              d  e  f  g//
	b := BinaryTree{"a",nil,nil}
	b.insertLeft("b")
	b.insertRight("c")
	b.Left.insertLeft("d")
	b.Left.insertRight("e")
	b.Right.insertLeft("f")
	b.Right.insertRight("g")
	fmt.Println("先序遍历====================")
	b.preorder() // a b d e c f g
	fmt.Println("后序遍历====================")
	b.postorder() // d e b f g c a
	fmt.Println("中序遍历====================")
	b.inorder()   // d b e a f c g
	fmt.Println("宽度优先====================")
	b.widthFirst() // a b c d e f g

}