(defun fact (n)
  (if (= n 0)
      1
      (* n (fact (- n 1))) 
  ) 
)
	
(princ "Enter a number : ")
(defvar num(read))
(format t "Factorial of ~a is ~a ~%" num (fact num))
