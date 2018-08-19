package main

import "fmt"

type Element int
type Node struct {
	data Element
	left *Node
	right *Node
}

type BinarySearchTree struct {
	root *Node
}

func (b *BinarySearchTree)insert(data Element){
	node := &Node{data:data}
	if b.root == nil{
		b.root = node
	}else{
		current := b.root
		for{
			parent := current
			if node.data < parent.data{
				if parent.left == nil{
					parent.left = node
					return
				}else{
					current = parent.left
				}
			}else{
				if parent.right == nil{
					parent.right = node
					return
				}else{
					current = parent.right
				}
			}
		}
	}
}

func (b *BinarySearchTree) widthFirst(){
	if b.root == nil{
		fmt.Println("no data")
		return
	}
	toVisit := []*Node{b.root}
	for len(toVisit) > 0{
		var current = toVisit[0]
		toVisit = toVisit[1:]

		fmt.Println(current.data)
		if current.left != nil{
			toVisit = append(toVisit, current.left)
		}
		if current.right !=nil{
			toVisit = append(toVisit, current.right)
		}
	}
}

func main(){
/*	Example
	 8
	/ \
	3  10
	/ \  \
	1  6 14
	/ \   /
    4  7 13
*/
	t := &BinarySearchTree{}
	t.insert(8)
	t.insert(3)
	t.insert(6)
	t.insert(1)
	t.insert(10)
	t.insert(14)
	t.insert(13)
	t.insert(4)
	t.insert(7)
	// 8 3 1 6 4 7 10 14 13
	// 先打印左边的===========================
	fmt.Println(t.root.data)
	fmt.Println(t.root.left.data)
	fmt.Println(t.root.left.left.data)
	fmt.Println(t.root.left.right.data)
	fmt.Println(t.root.left.right.left.data)
	fmt.Println(t.root.left.right.right.data)
	// 再打右边的==============================
	fmt.Println(t.root.right.data)
	fmt.Println(t.root.right.right.data)
	fmt.Println(t.root.right.right.left.data)
	// 宽度优先遍历============================
	fmt.Println("宽度优先遍历====================")
	t.widthFirst()  // 8 3 10 1 6 14 4 7 13
}
