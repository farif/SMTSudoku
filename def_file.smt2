
(set-logic ALL)
(set-option :produce-models true)

; Sudoku Board is of size value (n*n x n*n) and contains n-many blocks.
(declare-const n Int)
(assert (= n 3))


(declare-fun S (Int Int) Int)

; Each row contains at most one value
;orall x,y1,y2 S(x y1) = S(x y2) => y1 = y2
(assert (forall ((x Int))
        (forall ((y1 Int))
        (forall ((y2 Int))
            (=> 
                (= (S x y1) (S x y2)) 
                (= y1 y2)
            )
        )))
)

; Each column contains at most one value
;orall y,x1,x2 S(x1 y) = S(x2 y) => x1 = x2
(assert (forall ((x1 Int))
        (forall ((x2 Int))
        (forall ((y Int))
            (=> 
                (= (S x1 y) (S x2 y)) 
                (= x1 x2)
            )
        )))
)
; Each row contains at least one value
;orall y z \exists x S(x y) = z
(assert (forall ((x Int))
        (forall ((z Int))
        (exists ((y Int))
                
                (= (S x y) z)
        )))
)
; Each column contains at least one value
;orall x z \exists y S(x y) = z
(assert (forall ((y Int))
        (forall ((z Int))
        (exists ((x Int))
                
                (= (S x y) z)
        )))
)

;-- Each row and column contains at most one value
;--orall x1,y1,x2,y2 S(x1 y1) = S(x2 y2) => x1 = x2 and y2 = x2
;-- Each row and Column contains at least one value
;--orall x,y \exists z S(x y) = z

(declare-fun Block (Int Int) Bool)
; Any row and column within the block bound are equivalent.
; A block is a group of cells. 
;orall x Block(x,x)
;orall x, y Block(x,y) => Block(y,z)
;orall x, y, z Block(x,y) and Block(y,z) => Block(x,z)
(assert (forall ((x Int)) (Block x x)))
(assert (forall ((x Int)) (forall ((y Int)) (=> (Block x y) (Block y x)))))
(assert (forall ((x Int)) (
         forall ((y Int)) (
         forall ((z Int))
                 (=> (and (Block x y) (Block y z) )
                     (Block x z)
                 )
        )))
)
; Any row and column containg same values within the block points to same cell.
; At most one in each region.
;orall x1,y1,x2,y2 S(x1,y1) =  S(x2,y2) and Block (x1 x2) and Block(y1 y2) => x1 = x2 and y1 = y2
(assert (forall ((x1 Int))
        (forall ((y1 Int))
        (forall ((x2 Int))
        (forall ((y2 Int))
            (=>
                (and
                (= (S x1 y1) (S x2 y2))
                (Block x1 x2)
                (Block y1 y2))            

                (and
                (= x1 x2)
                (= y1 y2)
                )
            )
        ))))
)      

(assert (not (Block (* n n) 1)))  
(assert (Block 1 2))
(assert(not (Block 1 4)))
(assert (Block 2 3))
(assert(not (Block 4 7)))
(assert (Block 4 5))
(assert (Block 5 6))
(assert (Block 7 8))
(assert (Block 8 9))
(declare-const x11 Int)
(assert (= x11 5))
(declare-const x12 Int)
(assert (= x12 3))
(declare-const x13 Int)
(assert (<=  1 x13 9))
(declare-const x14 Int)
(assert (<=  1 x14 9))
(declare-const x15 Int)
(assert (= x15 7))
(declare-const x16 Int)
(assert (<=  1 x16 9))
(declare-const x17 Int)
(assert (<=  1 x17 9))
(declare-const x18 Int)
(assert (<=  1 x18 9))
(declare-const x19 Int)
(assert (<=  1 x19 9))
(declare-const x21 Int)
(assert (= x21 6))
(declare-const x22 Int)
(assert (<=  1 x22 9))
(declare-const x23 Int)
(assert (<=  1 x23 9))
(declare-const x24 Int)
(assert (= x24 1))
(declare-const x25 Int)
(assert (= x25 9))
(declare-const x26 Int)
(assert (= x26 5))
(declare-const x27 Int)
(assert (<=  1 x27 9))
(declare-const x28 Int)
(assert (<=  1 x28 9))
(declare-const x29 Int)
(assert (<=  1 x29 9))
(declare-const x31 Int)
(assert (<=  1 x31 9))
(declare-const x32 Int)
(assert (= x32 9))
(declare-const x33 Int)
(assert (= x33 8))
(declare-const x34 Int)
(assert (<=  1 x34 9))
(declare-const x35 Int)
(assert (<=  1 x35 9))
(declare-const x36 Int)
(assert (<=  1 x36 9))
(declare-const x37 Int)
(assert (<=  1 x37 9))
(declare-const x38 Int)
(assert (= x38 6))
(declare-const x39 Int)
(assert (<=  1 x39 9))
(declare-const x41 Int)
(assert (= x41 8))
(declare-const x42 Int)
(assert (<=  1 x42 9))
(declare-const x43 Int)
(assert (<=  1 x43 9))
(declare-const x44 Int)
(assert (<=  1 x44 9))
(declare-const x45 Int)
(assert (= x45 6))
(declare-const x46 Int)
(assert (<=  1 x46 9))
(declare-const x47 Int)
(assert (<=  1 x47 9))
(declare-const x48 Int)
(assert (<=  1 x48 9))
(declare-const x49 Int)
(assert (= x49 3))
(declare-const x51 Int)
(assert (= x51 4))
(declare-const x52 Int)
(assert (<=  1 x52 9))
(declare-const x53 Int)
(assert (<=  1 x53 9))
(declare-const x54 Int)
(assert (= x54 8))
(declare-const x55 Int)
(assert (<=  1 x55 9))
(declare-const x56 Int)
(assert (= x56 3))
(declare-const x57 Int)
(assert (<=  1 x57 9))
(declare-const x58 Int)
(assert (<=  1 x58 9))
(declare-const x59 Int)
(assert (= x59 1))
(declare-const x61 Int)
(assert (= x61 7))
(declare-const x62 Int)
(assert (<=  1 x62 9))
(declare-const x63 Int)
(assert (<=  1 x63 9))
(declare-const x64 Int)
(assert (<=  1 x64 9))
(declare-const x65 Int)
(assert (= x65 2))
(declare-const x66 Int)
(assert (<=  1 x66 9))
(declare-const x67 Int)
(assert (<=  1 x67 9))
(declare-const x68 Int)
(assert (<=  1 x68 9))
(declare-const x69 Int)
(assert (= x69 6))
(declare-const x71 Int)
(assert (<=  1 x71 9))
(declare-const x72 Int)
(assert (= x72 6))
(declare-const x73 Int)
(assert (<=  1 x73 9))
(declare-const x74 Int)
(assert (<=  1 x74 9))
(declare-const x75 Int)
(assert (<=  1 x75 9))
(declare-const x76 Int)
(assert (<=  1 x76 9))
(declare-const x77 Int)
(assert (= x77 2))
(declare-const x78 Int)
(assert (= x78 8))
(declare-const x79 Int)
(assert (<=  1 x79 9))
(declare-const x81 Int)
(assert (<=  1 x81 9))
(declare-const x82 Int)
(assert (<=  1 x82 9))
(declare-const x83 Int)
(assert (<=  1 x83 9))
(declare-const x84 Int)
(assert (= x84 4))
(declare-const x85 Int)
(assert (= x85 1))
(declare-const x86 Int)
(assert (= x86 9))
(declare-const x87 Int)
(assert (<=  1 x87 9))
(declare-const x88 Int)
(assert (<=  1 x88 9))
(declare-const x89 Int)
(assert (= x89 5))
(declare-const x91 Int)
(assert (<=  1 x91 9))
(declare-const x92 Int)
(assert (<=  1 x92 9))
(declare-const x93 Int)
(assert (<=  1 x93 9))
(declare-const x94 Int)
(assert (<=  1 x94 9))
(declare-const x95 Int)
(assert (= x95 8))
(declare-const x96 Int)
(assert (<=  1 x96 9))
(declare-const x97 Int)
(assert (<=  1 x97 9))
(declare-const x98 Int)
(assert (= x98 7))
(declare-const x99 Int)
(assert (= x99 9))
(assert (and 
(= (S 1 1) 5)
(= (S 1 2) 3)
(= (S 1 3) x13)
(= (S 1 4) x14)
(= (S 1 5) 7)
(= (S 1 6) x16)
(= (S 1 7) x17)
(= (S 1 8) x18)
(= (S 1 9) x19)
(= (S 2 1) 6)
(= (S 2 2) x22)
(= (S 2 3) x23)
(= (S 2 4) 1)
(= (S 2 5) 9)
(= (S 2 6) 5)
(= (S 2 7) x27)
(= (S 2 8) x28)
(= (S 2 9) x29)
(= (S 3 1) x31)
(= (S 3 2) 9)
(= (S 3 3) 8)
(= (S 3 4) x34)
(= (S 3 5) x35)
(= (S 3 6) x36)
(= (S 3 7) x37)
(= (S 3 8) 6)
(= (S 3 9) x39)
(= (S 4 1) 8)
(= (S 4 2) x42)
(= (S 4 3) x43)
(= (S 4 4) x44)
(= (S 4 5) 6)
(= (S 4 6) x46)
(= (S 4 7) x47)
(= (S 4 8) x48)
(= (S 4 9) 3)
(= (S 5 1) 4)
(= (S 5 2) x52)
(= (S 5 3) x53)
(= (S 5 4) 8)
(= (S 5 5) x55)
(= (S 5 6) 3)
(= (S 5 7) x57)
(= (S 5 8) x58)
(= (S 5 9) 1)
(= (S 6 1) 7)
(= (S 6 2) x62)
(= (S 6 3) x63)
(= (S 6 4) x64)
(= (S 6 5) 2)
(= (S 6 6) x66)
(= (S 6 7) x67)
(= (S 6 8) x68)
(= (S 6 9) 6)
(= (S 7 1) x71)
(= (S 7 2) 6)
(= (S 7 3) x73)
(= (S 7 4) x74)
(= (S 7 5) x75)
(= (S 7 6) x76)
(= (S 7 7) 2)
(= (S 7 8) 8)
(= (S 7 9) x79)
(= (S 8 1) x81)
(= (S 8 2) x82)
(= (S 8 3) x83)
(= (S 8 4) 4)
(= (S 8 5) 1)
(= (S 8 6) 9)
(= (S 8 7) x87)
(= (S 8 8) x88)
(= (S 8 9) 5)
(= (S 9 1) x91)
(= (S 9 2) x92)
(= (S 9 3) x93)
(= (S 9 4) x94)
(= (S 9 5) 8)
(= (S 9 6) x96)
(= (S 9 7) x97)
(= (S 9 8) 7)
(= (S 9 9) 9)
))(check-sat)
(get-value (x13))
(get-value (x14))
(get-value (x16))
(get-value (x17))
(get-value (x18))
(get-value (x19))
(get-value (x22))
(get-value (x23))
(get-value (x27))
(get-value (x28))
(get-value (x29))
(get-value (x31))
(get-value (x34))
(get-value (x35))
(get-value (x36))
(get-value (x37))
(get-value (x39))
(get-value (x42))
(get-value (x43))
(get-value (x44))
(get-value (x46))
(get-value (x47))
(get-value (x48))
(get-value (x52))
(get-value (x53))
(get-value (x55))
(get-value (x57))
(get-value (x58))
(get-value (x62))
(get-value (x63))
(get-value (x64))
(get-value (x66))
(get-value (x67))
(get-value (x68))
(get-value (x71))
(get-value (x73))
(get-value (x74))
(get-value (x75))
(get-value (x76))
(get-value (x79))
(get-value (x81))
(get-value (x82))
(get-value (x83))
(get-value (x87))
(get-value (x88))
(get-value (x91))
(get-value (x92))
(get-value (x93))
(get-value (x94))
(get-value (x96))
(get-value (x97))