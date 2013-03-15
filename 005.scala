object Euler {
    def gcd(a: Long, b: Long): Long = {
        if (a < b) gcd(b,a)
        else if (b == 0)  a
        else gcd(a-b, b) 
    }

    def euler005() = {
      List.range(2,21).map(_.toLong).reduce((x, y) => x*y/(gcd(x,y)))
    }

    def main(args: Array[String]) {
        var a = System.currentTimeMillis()
        println (euler005())
        println ("time elapsed: " + (System.currentTimeMillis()-a) + " millisec")
    }
}
