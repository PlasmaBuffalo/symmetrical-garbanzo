(*Ex1: Write a function cube of type int -> int that returns the cube of its parameter*)
fun cube a = a*a*a;

(*Ex2: Write a function cuber of type real -> real the returns the cube of its parameter.*)
fun cuber b:real = b*b*b;

(*Ex3: Write a function min3 of type int * int * int -> int that returns the smallest of three integers.*)
fun min3 [a:int,b:int,c:int] = 
    if a<b andalso a<c then a
    else if b<a andalso b<c then b
    else c;

(*Ex14: Write a function isPrime of type int -> bool that returns true if and only if its integer parameter is a prime number. Your function need not behave well if the parameter is negative.*)
fun isPrime x:int = 












fun factorial n =
    if n <= 1 then
      1
    else
      factorial (n-1) * n;

fun aux n =
  if n > 16 then
    ()
  else (
    print (Int.toString n ^ "! = " ^ Int.toString (factorial n) ^ "\n");
    aux (n + 1)
  );
aux 0;