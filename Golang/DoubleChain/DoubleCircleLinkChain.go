/*
 * 双向循环链表的实现
 */
package main

import(
	"fmt"
	"strings"
)

type Element int

type Node struct {
	data Element
	next *Node
	prev *Node
}

type DoubleChain struct {
	head *Node
}

func (d *DoubleChain) IsEmpty() bool{
	return d.head == nil
}

func (d *DoubleChain) Add(e Element){
	node := &Node{data: e}
	if d.IsEmpty() {
		d.head = node
		d.head.next = node
		d.head.prev = node
	}else{
		node.next = d.head
		node.prev = d.head.prev.next
		d.head.prev.next = node
		d.head.prev = node
		d.head = node
	}
}

func (d DoubleChain) String()string{
	if d.IsEmpty(){
		return "no data"
	}else{
		cursor := d.head
		result := make([]string,0)
		for cursor.next != d.head{
			result = append(result, fmt.Sprintf("%v",cursor.data))
			cursor = cursor.next
		}
		result = append(result, fmt.Sprintf("%v",cursor.data))
		return strings.Join(result, "<->")
	}

}

func main(){
	d := DoubleChain{}
	d.Add(1)
	d.Add(2)
	d.Add(3)
	fmt.Println(d)
	fmt.Println(d.head.data, d.head.next.data, d.head.next.next.data)
}