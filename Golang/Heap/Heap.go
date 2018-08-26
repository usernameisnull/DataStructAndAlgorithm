package main

import (
	"fmt"
	"github.com/pkg/errors"
)

type Element int
type Heap struct{
	h []Element
	currsize int
}

func (h *Heap) buildHeap(source []Element){
	h.h = source
	h.currsize = len(source)
	for i:= h.currsize/2;i>=0;i--{
		h.maxHeapify(i)
	}
}

func (h Heap)leftChild(i int) (int, error){
	result := 2*i+1
	if result < h.currsize {
		return result, nil
	}else{
		return 0, errors.New("超过了限制")
	}
}

func (h Heap)rightChild(i int) (int, error){
	result := 2*(i+1)
	if result < h.currsize {
		return result, nil
	}else{
		return 0, errors.New("超过了限制")
	}
}

func (h *Heap) maxHeapify(node int){
	if node >= h.currsize{
		return
	}else{
		m := node
		lc, err:= h.leftChild(node)
		if err == nil && h.h[lc]>h.h[m]{
			m = lc
		}
		rc, err:= h.rightChild(node)
		if err == nil && h.h[rc]>h.h[m]{
			m = rc
		}
		if m!=node{
			temp := h.h[m]
			h.h[m] = h.h[node]
			h.h[node] = temp
			h.maxHeapify(m)
		}
	}
}

func (h *Heap)sort(){
	size := h.currsize
	for h.currsize>=1{
		temp := h.h[h.currsize-1]
		h.h[h.currsize-1] = h.h[0]
		h.h[0]=temp
		h.currsize --
		h.maxHeapify(0)
	}
	h.currsize = size
}

func (h *Heap)insert(data Element){
	h.h = append(h.h, data)
	size:=h.currsize
	for h.h[size]>h.h[size/2] {
		temp := h.h[size]
		h.h[size] = h.h[size/2]
		h.h[size/2] = temp
		size = size/2
	}
	h.currsize++
}

func main(){
	h := Heap{}
	h.buildHeap([]Element{5, 4, 6, 3, 7, 2, 8, 1})
	fmt.Println(h.h)
	//h.sort()
	//fmt.Println(h.h)
	h.insert(10)
	fmt.Println(h.h)
	h.sort()
	fmt.Println(h.h)
}