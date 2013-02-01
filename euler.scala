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

    def euler001() = {
      val rg = List.range(1,1000) 
      println (rg.filter(x => x%3==0 || x%5 ==0).reduce(_+_))
    }
    def euler002() {
      var a = 1; var b = 1; var c = 2; var sum = 0
      while (c <= 4000000) {
          sum = sum +c
          a = b+c; b = c+a; c=a+b; 
      }
      println (sum)
    }
    def euler004() {
      val a = List.range(100,1000)
      println ((for { i<- a; j<-a} yield i*j) filter(x=>x.toString==x.toString.reverse) max)
    }
    def euler005() {
      println (List.range(2L,21L).reduce(lcm(_,_)))
    }
    def main(args: Array[String]) {
        var a = System.currentTimeMillis()
        euler005()
        println ("time elapsed: " + (System.currentTimeMillis()-a) + " millisec")
    }
}
