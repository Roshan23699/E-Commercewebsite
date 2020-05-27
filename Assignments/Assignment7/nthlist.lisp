(defparameter *n* '(2 4 6 5 7))

(defun lis(l f) 
    (nth f l)
)
(princ "Which element of index do you want? : ")
(defvar a(read))
(format t "~a item from list is ~a ~%" a (lis *n* (- a 1)))
