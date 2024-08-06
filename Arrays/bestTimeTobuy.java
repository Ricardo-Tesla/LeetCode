public class bestTimeTobuy {
    public static int maxProfit(int [] prices) {

        //initialize maximum profit
        int maxprofit=0;

        //iterate through each element in the array
        for(int i=1;i<prices.length;i++){
            if(prices[i] > prices[i-1]){
                maxprofit += (prices[i]- prices[i-1]);
            }
        }
        return maxprofit;
    }
    public static void main(String[] args) {
        int [] prices={7,6,5,4,3,2,1};
        //prices={1,2,3,4,5}
        //prices={7,1,5,3,6,4}
        
        System.out.println(maxProfit(prices));
    }
}
