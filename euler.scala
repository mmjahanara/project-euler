object Euler {
    val fibs: Stream[BigInt] = BigInt(0) #:: BigInt(1) #:: fibs.zip(fibs.tail).map(n => n._1 + n._2)

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

    def __getPrimeFactors(n: BigInt, x: BigInt): List[BigInt] = {
        if (x*x > n) List(n)
        else if (n % x == 0) {
           __getPrimeFactors(n/x, x) :+ x
        }
        else {
           __getPrimeFactors(n, x+(if (x==2) 1 else 2)) 
        }
    }

    def getPrimeFactors(n: BigInt): List[BigInt] = {
        __getPrimeFactors(n, BigInt(2))
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
    def euler003() = {
        getPrimeFactors(BigInt("600851475143")).max
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
    def euler008() = {
      val numbers = scala.io.Source.fromFile("data/008.txt").getLines().map(_.trim()).mkString("").map(_.toInt-48)
      (for {i <- List.range(1,numbers.length-4)} yield numbers(i)*numbers(i+1)*numbers(i+2)*numbers(i+3)*numbers(i+4)) max
    }
    def euler013() = {
      val text = scala.io.Source.fromFile("data/13.txt")
      text.getLines().map(BigInt(_)).reduce(_+_).toString().take(10)
    }
    def euler015() =  {
      fact(40)/fact(20)/fact(20)
    }
    def euler016() = {
      sumOfDigit(BigInt(2) pow 1000)
    }
    def euler020() = {
      sumOfDigit(fact(100))
    }
    def euler022() = {
      scala.io.Source.fromFile("data/022.txt").getLines().toList.apply(0).split(",").map(_.stripPrefix("\"").stripSuffix("\"")).sorted.
            zip(Stream.from(1)).map(x=>BigInt(x._1.map(_.toInt-64).sum)*BigInt(x._2)).sum
    }
    def euler025() = {
        fibs.zip(Stream.from(0)) dropWhile (x => x._1.toString.length < 1000) head
    }
    def euler029() = {
      val r = List.range(2,101)
      ((for { a <- r; b <- r} yield BigInt(a).pow(b)) toSet) size
    }
    def euler030() = {
      List.range(2,400000).filter(x=> x == x.toString.map(_.toInt-48).map(x=>x*x*x*x*x).sum).sum
    }
    def euler042() = {
      scala.io.Source.fromFile("data/words.txt").getLines().toList.apply(0).split(',').
            map(x => x.stripPrefix("\"").stripSuffix("\"")).map(x=>(x.map(_.toInt-64) sum)).
            filter(((2 to 30).scanLeft(1)(_+_)).contains(_)).length
    }
    def euler048()= {
      val s = (1 to 1000).map(x=>BigInt(x).pow(x.toInt)).sum.toString
      s.slice(s.length-10, s.length)
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
    def euler120() = {
       List.range(3,1001).map(a => List.range(1,a).map(_*2*a%(a*a)).max).sum
    }
    def main(args: Array[String]) {
        var a = System.currentTimeMillis()
        println (euler022())
        println ("time elapsed: " + (System.currentTimeMillis()-a) + " millisec")
    }
}
