object Euler {
    def euler001() {
      var rg = List.range(1,1000) 
      println (rg.filter(x => x%3==0 || x%5 ==0).reduce(_+_))
    }
    def euler004() {
      val a = List.range(100,1000)
      (for { i<- a; j<-a} yield i*j) filter(x=>x.toString==x.toString.reverse) max 
    }
    def main(args: Array[String]) {
        var a = System.currentTimeMillis()
        euler004()
        println ("time elapsed: " + (System.currentTimeMillis()-a) + " millisec")
    }
}
