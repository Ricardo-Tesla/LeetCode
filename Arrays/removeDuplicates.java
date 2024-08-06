/**
 * removeDuplicates
 */
public class removeDuplicates {
    public static int removeDuplicate(int [] nums){
        int k=1;
        
        for(int r=1;r<nums.length;r++){
            if(nums[r] != nums[r-1]){
                nums[k]=nums[r];
                k+=1;
            }
          
        }
        return k;
        
    }

    public static void main(String[] args) {
        int[] nums= {0,0,1,1,1,2,2,3,3,4};

        System.out.println(removeDuplicate(nums));
        
    }
    
}