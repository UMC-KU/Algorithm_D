package common_Factor;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		int[] nums = new int[n];
		int max = -1;
		int min = Integer.MAX_VALUE;
		for(int i = 0; i<n; i++) {
			nums[i] = Integer.parseInt(str[i]);
			if(nums[i]>max) max = nums[i];
			if(nums[i]<min) min = nums[i];
		}
		loop1:for(int j = 1; j<= min/2; j++) {
			for(int k:nums) {
				if(k%j != 0) continue loop1;
			}
			System.out.println(j);
			
			if(j == min/2) {
				j = min;
				for(int k:nums) {
					if(k%j != 0) continue loop1;
				}
				System.out.println(j);
			}
		}
		
	}
}
