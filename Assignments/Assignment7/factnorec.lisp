(defun fact (n)
	(defvar fact 1)
	(defvar x 1)
	(loop
		(setq fact (* fact x))
		(setq x (+ x 1))
		(when (> x n) (return fact))
	)
) 

(princ "Enter a number : ")
(defvar num(read))
(format t "Factorial of ~a is ~a ~%" num (fact num))

