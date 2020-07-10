'''
Created on Jul 10, 2020

@author: marif
'''

Sudoku_SMT_Lib=\
"""
(set-logic ALL)
(set-option :produce-models true)

; Sudoku Board is of size value (n*n x n*n) and contains n-many blocks.
(declare-const n Int)
(assert (= n 3))


(declare-fun S (Int Int) Int)

; Each row contains at most one value
;\forall x,y1,y2 S(x y1) = S(x y2) => y1 = y2
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
;\forall y,x1,x2 S(x1 y) = S(x2 y) => x1 = x2
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
;\forall y z \exists x S(x y) = z
(assert (forall ((x Int))
        (forall ((z Int))
        (exists ((y Int))
                
                (= (S x y) z)
        )))
)
; Each column contains at least one value
;\forall x z \exists y S(x y) = z
(assert (forall ((y Int))
        (forall ((z Int))
        (exists ((x Int))
                
                (= (S x y) z)
        )))
)

;-- Each row and column contains at most one value
;--\forall x1,y1,x2,y2 S(x1 y1) = S(x2 y2) => x1 = x2 and y2 = x2
;-- Each row and Column contains at least one value
;--\forall x,y \exists z S(x y) = z

(declare-fun Block (Int Int) Bool)
; Any row and column within the block bound are equivalent.
; A block is a group of cells. 
;\forall x Block(x,x)
;\forall x, y Block(x,y) => Block(y,z)
;\forall x, y, z Block(x,y) and Block(y,z) => Block(x,z)
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
;\forall x1,y1,x2,y2 S(x1,y1) =  S(x2,y2) and Block (x1 x2) and Block(y1 y2) => x1 = x2 and y1 = y2
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
"""
