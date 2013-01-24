object Euler {
    def euler001() {
      var rg = List.range(1,1000) 
      println (rg.filter(x => x%3==0 || x%5 ==0).reduce(_+_))
    }
    def main(args: Array[String]) {
        var a = System.currentTimeMillis()
        euler001()
        println ("time elapsed: " + (System.currentTimeMillis()-a) + " millisec")
    }
}
