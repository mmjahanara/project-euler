object Euler {
    def gcd(a: Long, b: Long): Long = {
        if (a < b) gcd(b,a)
        else if (b == 0)  a
        else gcd(a-b, b) 
    }

    // least common multiple
    def lcm(a: Long, b: Long)= {
        a*b/gcd(a,b)
    } 

    def sumOfDigit(i: Number): Int = {
       val s = i.toString
       s.map(_.toInt-48).reduce(_+_)
    }
 
    def fact(i: Int): BigInt = {
      if (i == 0) 1
      else if (i==1) 1
      else List.range(2,i+1).map(BigInt(_)).reduce(_*_)
    }

    def euler001() = {
      val rg = List.range(1,1000) 
      rg.filter(x => x%3==0 || x%5 ==0).reduce(_+_)
    }
    def euler002() = {
      var a = 1; var b = 1; var c = 2; var sum = 0
      while (c <= 4000000) {
          sum = sum +c
          a = b+c; b = c+a; c=a+b; 
      }
      sum
    }
    def euler004() = {
      val a = List.range(100,1000)
      (for { i<- a; j<-a} yield i*j) filter(x=>x.toString==x.toString.reverse) max
    }
    def euler005() = {
      List.range(2L,21L).reduce(lcm(_,_))
    }
    def euler006() = {
      val n = 100
      val l = List.range(1,n+1)
      l.sum * l.sum - l.map(x=>x*x).sum
    }
    def euler013() = {
      val text = scala.io.Source.fromFile("data/13.txt");
      text.getLines().map(BigInt(_)).reduce(_+_).toString().take(10)
    }
    def euler016() = {
      sumOfDigit(BigInt(2) pow 1000)
    }
    def euler029() = {
      val r = List.range(2,101)
      ((for { a <- r; b <- r} yield BigInt(a).pow(b)) toSet) size
    }
    def euler056() = {
      val a = 1 to 100 
      (for {i <- a; j <- a} yield BigInt(i) pow j) map (sumOfDigit(_)) max
    }

    def numNotBouncy(a: Int, e: Int, l: Int) = {
      val d = Math.abs(a-e)
      fact(d+l-2)/fact(l-2)/fact(d)
    }
    def euler113() = {
      (for {a <- List.range(1,10);
            e <- List.range(0,10);
            l <- List.range(2,101)} yield numNotBouncy(a,e,l)).sum + 9
    }
    def main(args: Array[String]) {
        var a = System.currentTimeMillis()
        println (euler113())
        println ("time elapsed: " + (System.currentTimeMillis()-a) + " millisec")
    }
}
