package printerQueue_1966;

import java.io.*;
import java.util.*;

public class Main {

	public static int func(int k, int m, Queue<Integer> arr, int[] nums) throws IOException{
		int index = nums.length-1;
		int count = 0;
		while(!arr.isEmpty()) {
			while(arr.peek() != nums[index]) {
				arr.add(arr.poll());
				m--;
				if(m < 0) 
					m = arr.size()-1;
			}
			if(arr.peek().intValue() == nums[index]) {
				count++;
				if(m == 0) {
					return count;
				}else {
					arr.poll();
					index--;
					m--;
				}
			}
		}
		return 0;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] str = new String[2];
		int k = 0, m = 0;
		for(int i = 0; i<n; i++) {
			str = br.readLine().split(" ");
			k = Integer.parseInt(str[0]);
			m = Integer.parseInt(str[1]);
			Queue<Integer> arr = new LinkedList<>();
			int[] nums = new int[k];
			
			String[] temp = br.readLine().split(" ");
			for(int j = 0; j<k; j++) {
				arr.add(Integer.parseInt(temp[j]));
				nums[j] = Integer.parseInt(temp[j]);
			}
			
			Arrays.sort(nums);
			bw.write(func(k, m, arr, nums)+"\n");
		}
		bw.flush();
	}
}