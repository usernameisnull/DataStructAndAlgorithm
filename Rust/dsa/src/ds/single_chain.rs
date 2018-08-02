// 借鉴: https://raw.githubusercontent.com/buchenglei/rustdsl/master/src/base/list.rs
#[test]
fn test_list() {
    let mut list: List<i32> = List::new(1);
    list.push_back(2);
    list.push_back(3);
    list.push_back(4);
    list.push_back(5);

    assert_eq!(5, list.len());

    {
        // data test
        let mut p = &list;
        let mut i = 1;
        loop {
            assert_eq!(i, p.value);

            match p.next {
                Some(ref n) => p = n,
                None => break
            }

            i += 1;
        }
    }

    list = list.push_front(6);
    assert_eq!(6, list.value);
}

struct List<T> {
    value: T,
    next: Option<Box<List<T>>>
}

impl<T> List<T> {

    // 创建一个新的链表
    fn new(value: T) -> List<T> {
        List {
            value: value,
            next: Option::None,
        }
    }

    fn push_front(self, value: T) -> List<T> {
        let mut node: List<T> = List::new(value);
        node.next = Some(Box::new(self));
        node
    }

    fn len(&self) -> u32 {
        let mut i = 0u32;
        let mut p = self;

        loop {
            match p.next {
                Some(ref n) => {
                    i += 1;
                    p = n;
                },
                None => {
                    i += 1;
                    break
                },
            }
        }

        i

    }

    // put a node to end of list
    fn push_back(&mut self, value: T){
        if let Some(ref mut n) = self.next {
            //self.next.unwrap().push_back(value);
            n.push_back(value);
        } else {
            self.next = Some(Box::new(List::new(value)));
        }
    }

}